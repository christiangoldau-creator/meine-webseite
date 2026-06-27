#!/usr/bin/env python3
"""
vimeo_transcripts.py — Zieht Transkripte (Text-Tracks/VTT) von Vimeo-Videos
und legt sie als bereinigten Klartext ab. Speist Schritt 1 (Repeated-Claims-
Mining) der Sourcing-Pipeline.

NUR Standardbibliothek (urllib) — läuft ohne pip-Install.

SETUP (Token NIEMALS in den Chat/ins Repo):
  1. Vimeo-App anlegen: https://developer.vimeo.com/apps  -> "Create App"
  2. Personal Access Token generieren mit Scopes: private, video_files
     (für Captions/Transkripte privater Videos zwingend)
  3. Token als Umgebungsvariable setzen:  export VIMEO_ACCESS_TOKEN="..."

NUTZUNG:
  # alle eigenen Videos:
  python3 vimeo_transcripts.py --all --out ./transkripte
  # ein Vimeo-Ordner (Project), z.B. ein Kongress:
  python3 vimeo_transcripts.py --folder 12345678 --out ./transkripte
  # einzelne Videos:
  python3 vimeo_transcripts.py --video 11111111 22222222 --out ./transkripte
  # bevorzugte Sprachen (Default de,en):
  python3 vimeo_transcripts.py --all --lang de,en --out ./transkripte

OUTPUT:
  <out>/<video_id>__<slug>.txt        bereinigter Transkript-Klartext
  <out>/_manifest.json                Übersicht (id, titel, sprache, status)
"""
import argparse, json, os, re, sys, time, urllib.request, urllib.error, urllib.parse

API = "https://api.vimeo.com"
ACCEPT = "application/vnd.vimeo.*+json;version=3.4"
TOKEN = os.environ.get("VIMEO_ACCESS_TOKEN", "")


def api_get(path_or_url, params=None):
    """GET gegen die Vimeo-API mit Bearer-Token, mit 429-Backoff."""
    url = path_or_url if path_or_url.startswith("http") else API + path_or_url
    if params:
        sep = "&" if "?" in url else "?"
        url += sep + urllib.parse.urlencode(params)
    for attempt in range(5):
        req = urllib.request.Request(url, headers={
            "Authorization": "Bearer " + TOKEN,
            "Accept": ACCEPT,
        })
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:  # Rate limit -> warten
                wait = int(e.headers.get("Retry-After", 2 ** attempt))
                time.sleep(wait); continue
            raise
    raise RuntimeError("Zu viele Rate-Limit-Fehler: " + url)


def list_videos(args):
    """Liefert [{id, name}] je nach Modus."""
    if args.video:
        return [{"id": v, "name": v} for v in args.video]
    if args.folder:
        path = "/me/projects/%s/videos" % args.folder
    else:
        path = "/me/videos"
    out, page = [], 1
    while True:
        data = api_get(path, {"per_page": 100, "page": page,
                              "fields": "uri,name,duration"})
        for v in data.get("data", []):
            vid = v["uri"].rsplit("/", 1)[-1]
            out.append({"id": vid, "name": v.get("name", vid)})
        if not data.get("paging", {}).get("next"):
            break
        page += 1
    return out


def pick_track(tracks, langs):
    """Beste Caption/Transkript-Spur wählen: aktiv > Sprachpräferenz > erste."""
    if not tracks:
        return None
    def score(t):
        s = 0
        if t.get("active"):
            s += 100
        lang = (t.get("language") or "").lower()
        for i, want in enumerate(langs):
            if lang.startswith(want):
                s += 50 - i
                break
        if t.get("type") in ("captions", "subtitles"):
            s += 5
        return s
    return sorted(tracks, key=score, reverse=True)[0]


def download(url):
    with urllib.request.urlopen(url, timeout=120) as r:  # VTT-Link ist signiert, kein Auth-Header
        return r.read().decode("utf-8", errors="replace")


def vtt_to_text(vtt):
    """WEBVTT -> Klartext: Zeitstempel/Cue-Nummern/NOTE entfernen, Dubletten kürzen."""
    lines, prev = [], None
    for raw in vtt.splitlines():
        line = raw.strip()
        if not line or line == "WEBVTT" or "-->" in line:
            continue
        if line.startswith(("NOTE", "STYLE", "REGION")):
            continue
        if re.fullmatch(r"\d+", line):           # Cue-Index
            continue
        line = re.sub(r"<[^>]+>", "", line)      # Inline-Tags entfernen
        if line and line != prev:                # aufeinanderfolgende Dubletten (Auto-Caption) kappen
            lines.append(line); prev = line
    return " ".join(lines)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60] or "video"


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--all", action="store_true", help="alle eigenen Videos")
    g.add_argument("--folder", help="Vimeo-Project/Folder-ID")
    g.add_argument("--video", nargs="+", help="einzelne Video-IDs")
    ap.add_argument("--out", default="./transkripte")
    ap.add_argument("--lang", default="de,en")
    args = ap.parse_args()

    if not TOKEN:
        sys.exit("FEHLER: Umgebungsvariable VIMEO_ACCESS_TOKEN nicht gesetzt.")

    langs = [x.strip().lower() for x in args.lang.split(",") if x.strip()]
    os.makedirs(args.out, exist_ok=True)
    videos = list_videos(args)
    print("Gefundene Videos: %d" % len(videos))

    manifest = []
    for i, v in enumerate(videos, 1):
        vid, name = v["id"], v["name"]
        entry = {"id": vid, "titel": name, "status": "", "sprache": None, "datei": None}
        try:
            tracks = api_get("/videos/%s/texttracks" % vid).get("data", [])
            t = pick_track(tracks, langs)
            if not t or not t.get("link"):
                entry["status"] = "kein Transkript/Text-Track"
            else:
                text = vtt_to_text(download(t["link"]))
                if len(text) < 40:
                    entry["status"] = "Transkript leer/zu kurz"
                else:
                    fn = "%s__%s.txt" % (vid, slug(name))
                    with open(os.path.join(args.out, fn), "w", encoding="utf-8") as f:
                        f.write("# %s (Vimeo %s)\n\n%s\n" % (name, vid, text))
                    entry.update(status="ok", sprache=t.get("language"), datei=fn)
        except Exception as e:
            entry["status"] = "Fehler: %s" % e
        manifest.append(entry)
        print("[%d/%d] %s -> %s" % (i, len(videos), vid, entry["status"]))
        time.sleep(0.3)  # API schonen

    with open(os.path.join(args.out, "_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    ok = sum(1 for m in manifest if m["status"] == "ok")
    print("Fertig: %d/%d Transkripte gespeichert in %s" % (ok, len(manifest), args.out))


if __name__ == "__main__":
    main()
