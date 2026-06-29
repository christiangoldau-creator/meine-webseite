#!/usr/bin/env python3
"""Repariert UTF-8 -> cp1252 -> UTF-8 Doppel-Encoding (PowerShell-Mojibake) + BOM.

Wenn eine HTML-Datei versehentlich per PowerShell Set-Content geschrieben wurde, sind
Umlaute zerschossen ("UnvertrÃ¤glichkeiten") und ein BOM ist gesetzt. Dieses Script
dreht das zurueck. ACHTUNG: an Emoji-Stellen (z. B. Bytefolgen mit 0x8F wie ☀️) ist die
Korruption verlustbehaftet -> dort die Datei lieber sauber neu schreiben.

Nutzung: python fix_mojibake.py <datei1.html> [datei2.html ...]
"""
import sys

MARKERS = ("Ã", "â€", "Â")


def fix_once(path):
    b = open(path, "rb").read()
    s = b.decode("utf-8", errors="replace").replace("﻿", "")  # BOM weg
    if not any(m in s for m in MARKERS):
        return False
    try:
        fixed = s.encode("cp1252")
    except UnicodeEncodeError as e:
        print("  cp1252-Fehler (Emoji-Stelle? -> neu schreiben):", e); return False
    open(path, "wb").write(fixed)
    return True


for path in sys.argv[1:]:
    passes = 0
    while passes < 3 and fix_once(path):
        passes += 1
    s = open(path, "rb").read().decode("utf-8", errors="replace")
    rest = [m for m in MARKERS if m in s]
    print("%s -> %d Pass(es), Rest-Mojibake: %s" % (path, passes, rest or "keins"))
