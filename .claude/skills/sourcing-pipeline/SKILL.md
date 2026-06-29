---
name: sourcing-pipeline
description: >
  Unternehmensfähigkeit „Sourcing-Pipeline" — von der Kongress-Erkenntnis bis zum Produkt im Shop, für
  Viktilabs / Veda360 / Medumio. IMMER nutzen, wenn jemand aus Kongressinhalten neue Supplement-Produkte entwickeln will:
  Vimeo-Kongress-Transkripte ziehen, Repeated-Claims-Mining, Produktideen/Konzepte bewerten,
  Regulatorik-/Novel-Food-/HWG-Check, EU-Lohnhersteller & RFQ, Produzierbarkeit/Rezeptur/BOM, sowie
  Produkt-Design (markentreue Mockups) und Produkt-Detailseiten (PDP) erstellen. Auch auslösen bei:
  „Sourcing-Pipeline", „Claims-Mining aus Kongress", „welches Supplement sollen wir machen",
  „Produktidee für Veda360/Wechseljahre", „RFQ an Hersteller", „Produkt-Mockup / Packaging / Doypack /
  Kapselglas für Viktilabs", „Produktseite / USPs für ein neues Supplement". Greift auch ohne das Wort
  „Pipeline", sobald es um Sortimentsentwicklung aus Kongressen für diese Marken geht.
---

# Supplement Sourcing Pipeline (Zero to Hero)

Strukturierte Fähigkeit, aus den Medumio/Veda360-**Kongressen** heraus neue **Viktilabs**-Supplements zu
entwickeln — von der Kongress-Erkenntnis bis zum verkaufsfertigen Produkt im Shop. Architektur auf dem
vorhandenen Stack: Asana (Single Source of Truth) · Google Drive · n8n · Claude API.

## Wissensbasis (zuerst auf Claude-Server entwickelt, Daten auf GitHub)

Die Fähigkeit wurde ursprünglich auf dem Claude-Server entwickelt; die Daten/Dokumente liegen auf **GitHub**:
`github.com/christiangoldau-creator/meine-webseite` → Ordner **`supplement-sourcing-zero-to-hero/`**
(Branch `claude/supplement-sourcing-github-unk0l9`), lokal geklont unter
`C:\Users\state\meine-webseite\supplement-sourcing-zero-to-hero\`.
Vor inhaltlicher Arbeit das relevante Doc lesen — Übersicht & Mapping:
[`references/pipeline-overview.md`](references/pipeline-overview.md). Neue Analysen/Outputs als nummeriertes
Doc dort ablegen (gleicher Stil) und committen/pushen, Design-Assets nach `design/`.

## Setup (maschinenspezifisch — pro Rechner einmal einrichten, pro Bash-Lauf laden)

- **API-Keys** (Vimeo, OpenAI, Gemini) liegen in einem **lokalen Secrets-Ordner** — nicht im Repo, nicht in Git, nicht synchronisiert. Drei Dateien: `vimeo key.txt`, `OPENAI-API KEY.txt`, `GEMINI-API KEY.txt`. Auf einem neuen Rechner manuell hinterlegen. Pfad je Rechner setzen und pro Lauf laden (Shell-State persistiert nicht):
  ```bash
  SECRETS="<dein-lokaler-secrets-ordner>"
  export VIMEO_ACCESS_TOKEN="$(tr -d ' \r\n' < "$SECRETS/vimeo key.txt")"
  export OPENAI_API_KEY="$(tr -d ' \r\n' < "$SECRETS/OPENAI-API KEY.txt")"
  export GEMINI_API_KEY="$(tr -d ' \r\n' < "$SECRETS/GEMINI-API KEY.txt")"
  ```
  Keys **nie** in Chat/Repo. (Auf dem ursprünglichen Laptop lag der Ordner unter `…\OneDrive\Dokumente\Claude\secrets\` — das ist maschinenspezifisch, nicht verlassen.)
- **Python 3** muss installiert sein (Skripte = reine stdlib, kein pip). Interpreter-Pfad je Rechner ermitteln; ggf. ist der PATH-`python` unter Windows nur ein Store-Platzhalter → vollen Pfad zur echten `python.exe` nutzen.
- **Repo** je Rechner an beliebigem Ort klonen; Pfadangaben in den Docs sind relativ zum Repo-Ordner zu lesen.

## Die Pipeline in einem Satz

```
90 Kongresse → Repeated-Claims-Miner → Opportunity-Backlog
  → G1 Idee → G2 Business Case → G3 REGULATORIK (Frühfilter)
  → RFQ/Hersteller → Muster/Stabilität → Etikett/Compliance → BVL-Anzeige
  → Produktion → PRODUKTDESIGN (Mockups + Produktseite) → Launch (Kongress→Mail→Shop)
```

## Stufen

1. **Transkripte ziehen** — Vimeo-Kongress-Ordner → bereinigter Klartext via `tools/vimeo_transcripts.py` im Repo (`--folder <id> --out ./transkripte`). Token = `VIMEO_ACCESS_TOKEN`.
2. **Wirkstoff-Recherche & Claims-Mining** — über alle Transkripte fan-out (mehrere Agenten, je ein Batch): Substanz↔Indikation-Paare strukturiert extrahieren, Re-Upload-Dubletten herausrechnen, frequenzgerankter Opportunity-Backlog; ergänzt um vertiefte **Recherche zu den Wirkstoffen** (Markt, Evidenz, Wettbewerb, Amazon/Bücher, Web). Docs 01 + 11.
3. **Produktideen & Bewertung** — Konzepte ableiten, adversarial prüfen (GO/CAUTION/KILL), Format-/Margen-Vergleich. Doc 02.
4. **Regulatorik (G3-Frühfilter)** — Ampel je Botanical: Novel Food, AM-Abgrenzung (Dosis), Verbots-/Warnstoffe (z. B. **Ashwagandha = ROT**), Schwermetalle, HWG/HCVO. Doc 05. **Claim-unabhängige Grenzen gelten immer.**
5. **Lohnhersteller (europaweit) & RFQ** — EU-weite Lohnhersteller-Recherche/Listen + versandfertige RFQ + RFQ-Automation (Gmail→n8n→Claude→Asana). Docs 04/06/08.
6. **Produzierbarkeit** — gesperrte Spezifikation, Rohstoff-BOM, Grenzwerte/CoA. Docs 07/12.
7. **Produktdesign — Produktdetailseite + Mock-Ups** — fester Teil der Produktionskette: am Ende braucht jedes Produkt eine PDP, und darauf gehören die Mock-Ups. Siehe unten. Outputs nach `design/`.
8. **Launch** — Funnel Kongress → E-Mail → Shop.

## Stufe 7 — Produktdesign

Zwei Teilaufgaben; Detail-Anleitungen:
- **Mockups**: [`references/brand-system.md`](references/brand-system.md) — echtes Viktilabs-Label-System, Verpackungsregeln, Prompt-Baukasten, erprobte Beispiele.
- **Produktseiten (PDP)**: [`references/product-page-template.md`](references/product-page-template.md) — Shop-Aufbau, Copy-Module, Claim-Regel, Artifact-Rendering.

### Mockups — Kern
- **Form zuerst klären → Verpackung folgt zwingend:** Pulver/Churna = **Doypack**; Kapseln/Presslinge = **Braunglas + schwarzer Deckel**.
- Viktilabs ist **farbsatt** (Gradient-Farbwelt je Produkt, „+viktilabs"-Logo in Pfirsich, zweizoniges Label, **Goldlinie**, Siegel, großes „V"-Wasserzeichen, Boden-Linie) — **nicht** minimalistisch-weiß. Immer mit echten Referenzbildern (von viktilabs.de, `_1500x.webp`) arbeiten.
- **Modell:** zuerst **Nano Banana** testen (`scripts/gen_gemini.py`, `gemini-2.5-flash-image`); braucht Gemini-Guthaben — bei 429 „credits depleted"/Free-Tier → Fallback **gpt-image-2** (`scripts/gen_openai_edit.py`, Edit mit passendem Referenzbild). Verfügbarkeit ändert sich → jedes Mal kurz prüfen.
- Bildserie je Produkt: Front (Edit auf Referenz) · Lifestyle/Detail (Front-Bild als Referenz) · optional Duo/Bundle (beide Fronts als Referenz, dauert lang → Hintergrund).
- Immer dazusagen: **Mockup = Konzept, keine Druckvorlage** (Umlaute im Label vermeiden, `fuer` statt `für`).

### Produktseite — Kern
- Aufbau wie echter Viktilabs-Shop (Hero/Buy-Box · Gut zu wissen · Inhaltsstoffe · Verzehr-Cards · Wirkung & Studien · Labor · Kombination · Mission · Vergleich · FAQ), Tonalität „Du". Module: `references/product-page-template.md`.
- **Claim-Regel:** Vermarktung über **Aufklärung** (Kongress/Mail), nicht über Produkt-Claims. Nur **zugelassene** Angaben (praktisch v. a. **Magnesium**); pflanzliche Bestandteile → Standard-Disclaimer „dürfen aus rechtlichen Gründen keine Wirkangaben machen" + Verweis Kongress/Studien. Keine Heilversprechen (HWG/HCVO).
- Als **Artifact** rendern: HTML mit eigenem `<style>`, System-Sans, Bild als `data:`-URI.

### ⚠️ KRITISCHER Gotcha (Design-Stufe)
HTML/Text **nie** per PowerShell `Get-/Set-Content` injizieren — zerstört UTF-8-Umlaute („UnvertrÃ¤glichkeiten") + setzt BOM. Bild-data-URI **immer** mit `scripts/inject_image.py` (Python, UTF-8-sicher) einsetzen. Reparatur korrumpierter Dateien: `scripts/fix_mojibake.py` (außer Emoji-Stellen → neu schreiben). Bild verkleinern per PowerShell System.Drawing (Binär) ist OK.

## Scripts (gebündelt)
- `scripts/gen_gemini.py <out> <prompt> [refs...]` — Nano Banana (mit Referenzbildern).
- `scripts/gen_openai_edit.py <out> <prompt> <size> <refs...>` — gpt-image-2 Edit (Style-Transfer, markentreu).
- `scripts/gen_openai.py <out> <prompt> [size]` — gpt-image-2 Generierung ohne Referenz (Lifestyle).
- `scripts/inject_image.py <html> <datauri.txt> [token]` — UTF-8-sichere data-URI-Injektion.
- `scripts/fix_mojibake.py <html...>` — repariert PowerShell-Mojibake/BOM.
