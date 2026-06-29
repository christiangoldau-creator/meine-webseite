#!/usr/bin/env python3
"""Bildgenerierung via OpenAI gpt-image-2 OHNE Referenz (z. B. Lifestyle-Szenen). Nur stdlib.

Nutzung:
  export OPENAI_API_KEY=...
  export OPENAI_IMAGE_MODEL=gpt-image-2     # optional
  python gen_openai.py <out.png> "<prompt>" [size]
  # size default 1024x1536
Fuer markentreue Packshots besser scripts/gen_openai_edit.py (mit Referenzbild) nutzen.
"""
import os, sys, json, base64, urllib.request, urllib.error

KEY = os.environ["OPENAI_API_KEY"]
MODEL = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-2")
URL = "https://api.openai.com/v1/images/generations"


def gen(out, prompt, size="1024x1536"):
    body = json.dumps({"model": MODEL, "prompt": prompt, "size": size,
                       "quality": "high", "n": 1}).encode()
    req = urllib.request.Request(URL, data=body, headers={
        "Authorization": "Bearer " + KEY, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=400) as r:
            d = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        print("FEHLER %s: %s" % (e.code, e.read().decode()[:600])); return False
    with open(out, "wb") as f:
        f.write(base64.b64decode(d["data"][0]["b64_json"]))
    print("OK ->", out); return True


if __name__ == "__main__":
    out, prompt = sys.argv[1], sys.argv[2]
    size = sys.argv[3] if len(sys.argv) > 3 else "1024x1536"
    sys.exit(0 if gen(out, prompt, size) else 1)
