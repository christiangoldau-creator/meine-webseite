#!/usr/bin/env python3
"""Bildgenerierung via Gemini (Nano Banana) mit optionalen Referenzbildern. Nur stdlib.

Nutzung:
  export GEMINI_API_KEY=...            # aus secrets-Datei laden
  export GEMINI_IMAGE_MODEL=gemini-2.5-flash-image   # optional; auch gemini-3-pro-image
  python gen_gemini.py <out.png> "<prompt>" [ref1.jpg ref2.jpg ...]

Bei 429 "prepayment credits depleted" / Free-Tier-Limit 0 -> Gemini-Projekt hat kein
Bildkontingent; auf scripts/gen_openai_edit.py (gpt-image-2) ausweichen.
"""
import os, sys, json, base64, mimetypes, urllib.request, urllib.error

KEY = os.environ["GEMINI_API_KEY"]
MODEL = os.environ.get("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image")
URL = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent?key=%s" % (MODEL, KEY)


def part_img(path):
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    mime = mimetypes.guess_type(path)[0] or "image/jpeg"
    return {"inline_data": {"mime_type": mime, "data": data}}


def gen(out, prompt, refs):
    parts = [{"text": prompt}] + [part_img(r) for r in refs]
    body = json.dumps({
        "contents": [{"parts": parts}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }).encode()
    req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            d = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        print("FEHLER %s: %s" % (e.code, e.read().decode()[:800])); return False
    for p in d.get("candidates", [{}])[0].get("content", {}).get("parts", []):
        blob = p.get("inlineData") or p.get("inline_data")
        if blob:
            with open(out, "wb") as f:
                f.write(base64.b64decode(blob["data"]))
            print("OK ->", out); return True
    print("Kein Bild in Antwort:", json.dumps(d)[:800]); return False


if __name__ == "__main__":
    out, prompt = sys.argv[1], sys.argv[2]
    sys.exit(0 if gen(out, prompt, sys.argv[3:]) else 1)
