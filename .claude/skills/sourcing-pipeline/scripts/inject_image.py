#!/usr/bin/env python3
"""UTF-8-sicheres Einsetzen einer Bild-data-URI in einen HTML-Platzhalter __HERO__.

NIEMALS PowerShell Get-/Set-Content dafuer nutzen (zerstoert Umlaute + setzt BOM).
Dieses Script liest/schreibt explizit UTF-8 ohne BOM.

Vorbereitung der data-URI (Bild zuvor auf ~760px verkleinern, JPEG q84) -> in Textdatei:
  data:image/jpeg;base64,XXXX
Nutzung:
  python inject_image.py <seite.html> <datauri.txt> [PLATZHALTER]
"""
import sys

html = sys.argv[1]
b64file = sys.argv[2]
token = sys.argv[3] if len(sys.argv) > 3 else "__HERO__"

with open(b64file, "r", encoding="utf-8") as f:
    uri = f.read().strip()
with open(html, "r", encoding="utf-8") as f:
    c = f.read()
n = c.count(token)
c = c.replace(token, uri)
with open(html, "w", encoding="utf-8") as f:  # kein BOM
    f.write(c)
print("injected: %d Platzhalter ersetzt, KB=%d" % (n, len(c) // 1024))
