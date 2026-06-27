# 10 – Vimeo-Transkript-Integration (verbessert Schritt 1)

> Zieht über die **Vimeo-API** die Transkripte (Text-Tracks/VTT) der Kongress-Vorträge und macht daraus durchsuchbaren Volltext für den **Repeated-Claims-Miner** (Schritt 1 der Pipeline / `09` Schritt 1). Stand: 2026-06-27.

## Warum das Schritt 1 verbessert
Bisher basiert das Claims-Mining auf den **Mastertabellen** in Drive (kuratierte Auszüge). Mit den **Volltext-Transkripten** jedes Vortrags sucht der Miner über das **gesamte gesprochene Wort** — d. h. wiederkehrende Experten-Aussagen zu Supplementen werden vollständig und mit O-Ton-Belegen erfasst, nicht nur dort, wo sie schon in eine Tabelle eingetragen wurden. Das erhöht Trefferzahl, Belegtiefe und Häufigkeits-Genauigkeit erheblich.

## So liefert die Vimeo-API Transkripte
- Endpoint: `GET https://api.vimeo.com/videos/{video_id}/texttracks`
- Auth: Header `Authorization: Bearer {TOKEN}` und `Accept: application/vnd.vimeo.*+json;version=3.4`
- Antwort: `data[]` mit Feldern u. a. `active`, `type` (`captions`/`subtitles`), `language`, **`link`** (URL zur **VTT**-Datei), `link_expires_time` (Link ist zeitlich befristet → sofort herunterladen).
- Auto-generierte Vimeo-Transkripte erscheinen ebenfalls als Text-Track (Caption). Die VTT-`link`-URL ist signiert und wird **ohne** Auth-Header geladen.
- **Scopes:** Personal Access Token mit `private` + `video_files` (für Captions privater Videos zwingend).
- **Limitierung:** Für „nur mit Link"-Videos kann der Zugriff eingeschränkt sein; eigene/Team-Videos mit gültigem Token funktionieren. Rate-Limits beachten (das Skript macht 429-Backoff).

Quellen: [Vimeo API – Text Track Response](https://developer.vimeo.com/api/reference/response/text-track) · [Vimeo Help – Download transcripts via API](https://help.vimeo.com/hc/en-us/articles/17480150130833-How-to-access-and-download-video-transcripts-via-API) · [Vimeo API 3.4 Reference](https://developer.vimeo.com/api/reference/v/3.4) · [Authentication/Scopes](https://developer.vimeo.com/api/authentication)

## Token-Setup (sicher — niemals im Chat/Repo)
1. App anlegen: https://developer.vimeo.com/apps → *Create App*.
2. *Generate Access Token* mit Scopes **private, video_files**.
3. Token sicher hinterlegen:
   - lokal: `export VIMEO_ACCESS_TOKEN="..."`
   - in n8n: als **Credential** (Header Auth), nicht im Workflow-JSON.

## Variante A — Schnell: das Skript
[`tools/vimeo_transcripts.py`](tools/vimeo_transcripts.py) (nur Python-Standardbibliothek):

```bash
export VIMEO_ACCESS_TOKEN="..."           # niemals committen
# ein Kongress = ein Vimeo-Ordner (Project-ID):
python3 tools/vimeo_transcripts.py --folder 12345678 --lang de,en --out ./transkripte
# oder alle Videos:  --all   | oder einzelne:  --video 11111111 22222222
```
Ergebnis: je Video `./transkripte/<id>__<slug>.txt` (bereinigter Klartext: Zeitstempel/Cue-Nummern/NOTE entfernt, Auto-Caption-Dubletten gekappt) + `_manifest.json` (Status je Video). Die `.txt` kommen nach Google Drive in den Kongress-Ordner → der Claims-Miner (Schritt 1) läuft darüber.

> Den Ordner `transkripte/` und Tokens nicht ins Repo committen (siehe `.gitignore`-Hinweis unten).

## Variante B — Dauerhaft: n8n-Workflow „Vimeo-Transkript-Sync"
Auf dem Haus-Stack (n8n · Drive · Claude), passend zum bestehenden „Kongress-Extraktion"-Muster:

```
[Trigger: manuell / Cron / Asana-Status "Transkripte ziehen"]
   │  Input: Vimeo-Folder-ID des Kongresses
   ▼ [HTTP Request: GET /me/projects/{folder}/videos?per_page=100  (Header-Auth-Credential)]
   ▼ [Loop über Videos]
       ├─ [HTTP: GET /videos/{id}/texttracks]
       ├─ [Function: besten Track wählen (active > Sprache de/en)]
       ├─ [HTTP: GET {track.link}  → VTT]  (Link ist befristet!)
       ├─ [Function: VTT → Klartext (Zeitstempel/Dubletten raus)]
       └─ [Google Drive: ablegen unter /Kongresse/{Kongress}/transkripte/{id}.txt]
   ▼ [Asana: Status "Transkripte bereit" + Drive-Link]
   ▼ [optional sofort: Claude-Extraktion = Schritt 1 (Repeated-Claims-Miner)]
```
**Error-Handling** wie im Haus-Standard: 3 Retries/Backoff (inkl. 429), bei Final-Failure Slack-Alert + Asana-Comment; Token nur als Credential.

## Verdrahtung in Schritt 1 (Repeated-Claims-Miner)
Der Claims-Miner bekommt damit **zwei** Quellen je Kongress: (1) Mastertabellen (kuratiert) **+** (2) Vimeo-Volltext-Transkripte. Extraktions-Prompt-Erweiterung:
> „Extrahiere wiederkehrende Experten-Aussagen zu Supplementen/Botanicals **aus den Volltext-Transkripten** (Quelle: Vimeo {video_id}). Gib je Aussage: Wirkstoff, Indikation, **wörtliches Zitat + Sprecher + Video-ID/Zeitbezug**, und zähle die Häufigkeit über alle Vorträge."

So werden Häufigkeit und Beleglage (O-Ton) deutlich belastbarer als aus den Tabellen allein.

## Sicherheit / Datenschutz
- Token = Geheimnis: nur als Env-Var/n8n-Credential, nie ins Repo/Chat. `transkripte/`, `*.env`, Tokens in `.gitignore`.
- Transkripte können personenbezogene/urheberrechtlich geschützte Inhalte enthalten → intern behandeln; nur für die interne Analyse nutzen.

## Nächster Schritt
Sag mir die **Vimeo-Folder-ID** (oder den Kongress), dann passe ich die Aufruf-Parameter an und erweitere den Schritt-1-Extraktions-Prompt der `sourcing-pipeline`-Skill um die Transkript-Quelle. Den Token bitte **nur** in eurer Umgebung/n8n hinterlegen — ich brauche ihn nicht zu sehen.
