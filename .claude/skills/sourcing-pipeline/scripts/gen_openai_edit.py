#!/usr/bin/env python3
"""OpenAI gpt-image-2 Edit (Style-Transfer von Referenzbildern). Nur stdlib.

Restyled ein vorhandenes Produktbild in ein neues Produkt und haelt dabei Markenidentitaet,
Label-Architektur, Foto-Stil und Komposition. Pro Format das passende Referenzbild geben
(Doypack->Doypack, Braunglas->Braunglas). Mehrere Referenzen (z. B. Duo-Shot) moeglich,
dauern aber laenger (ggf. im Hintergrund laufen lassen).

Nutzung:
  export OPENAI_API_KEY=...
  export OPENAI_IMAGE_MODEL=gpt-image-2        # optional
  python gen_openai_edit.py <out.png> "<prompt>" <size> <ref1> [ref2 ...]
  # size z. B. 1024x1536 (Hochformat), 1024x1024, 1536x1024
"""
import os, sys, json, base64, uuid, mimetypes, urllib.request, urllib.error

KEY = os.environ["OPENAI_API_KEY"]
MODEL = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-2")
URL = "https://api.openai.com/v1/images/edits"


def multipart(fields, files):
    boundary = "----vk" + uuid.uuid4().hex
    crlf = b"\r\n"; body = b""
    for k, v in fields.items():
        body += b"--" + boundary.encode() + crlf
        body += ('Content-Disposition: form-data; name="%s"' % k).encode() + crlf + crlf
        body += str(v).encode() + crlf
    for k, path in files:
        fn = os.path.basename(path)
        mime = mimetypes.guess_type(path)[0] or "image/jpeg"
        with open(path, "rb") as f:
            data = f.read()
        body += b"--" + boundary.encode() + crlf
        body += ('Content-Disposition: form-data; name="%s"; filename="%s"' % (k, fn)).encode() + crlf
        body += ("Content-Type: %s" % mime).encode() + crlf + crlf
        body += data + crlf
    body += b"--" + boundary.encode() + b"--" + crlf
    return body, "multipart/form-data; boundary=" + boundary


def gen(out, prompt, size, refs):
    fields = {"model": MODEL, "prompt": prompt, "size": size, "quality": "high"}
    files = [("image[]", r) for r in refs]
    body, ctype = multipart(fields, files)
    req = urllib.request.Request(URL, data=body, headers={
        "Authorization": "Bearer " + KEY, "Content-Type": ctype})
    try:
        with urllib.request.urlopen(req, timeout=560) as r:
            d = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        print("FEHLER %s: %s" % (e.code, e.read().decode()[:800])); return False
    with open(out, "wb") as f:
        f.write(base64.b64decode(d["data"][0]["b64_json"]))
    print("OK ->", out); return True


if __name__ == "__main__":
    out, prompt, size = sys.argv[1], sys.argv[2], sys.argv[3]
    sys.exit(0 if gen(out, prompt, size, sys.argv[4:]) else 1)
