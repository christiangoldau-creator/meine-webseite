# Gemini-Deep-Research-Brief: EU-Lohnhersteller-Sweep

> Zum Reinkopieren in **Gemini Deep Research** (passt zum bestehenden Gemini-Pfad der Pipeline). Liefert eine breite, strukturierte EU-Hersteller-Liste, die du anschließend mit unserer Recherche (`06`) zusammenführst. Stand: 2026-06-27.

---

## Prompt (alles ab hier kopieren)

**Rolle & Ziel:** Du bist ein Beschaffungs-Researcher. Erstelle eine möglichst vollständige Liste von **Auftragsfertigern / Lohnherstellern (Private Label) für Nahrungsergänzungsmittel in Europa**, die für eine deutsche Supplement-Marke (Viktilabs) in Frage kommen. Recherchiere gründlich über mehrere Quellen und gib am Ende eine strukturierte Tabelle aus.

**Was produziert werden soll (Eignung danach bewerten):**
- Primär: aromatisierte **Bio-Pulvermischung / Churna** (Triphala-, Amla-, Kurkuma-Pulver – Vollfrucht/Gewürz, keine Extrakte), 150-g-Gebinde.
- Zusätzlich gewünschte Formate: **Kapseln, Tee/Kräutermischungen, Öle, Tinkturen/Tropfen** sowie weitere ayurvedische Botanicals (Shatavari, Brahmi/Bacopa, Boswellia).

**Regionen:** ganz Europa – DACH, Benelux, Nordics, Süd- (IT, ES, PT, GR) und Osteuropa (PL, CZ, SK, SI, HU, RO, BG, HR, Baltikum).

**Quellen, die du auswerten sollst:**
1. Ausstellerverzeichnisse der Fachmessen: **Vitafoods Europe, Fi Europe & Hi (Food/Health Ingredients), SupplySide, Biofach (Bio), Hi&Fi, Anuga FoodTec**.
2. B2B-Verzeichnisse: **Europages, Wer liefert was (wlw), Wonnda, Kompass, lohnhersteller.com**.
3. Direkte Hersteller-Websites (Begriffe: „contract manufacturing", „private label supplements", „Lohnhersteller Nahrungsergänzungsmittel", „own brand", „white label").

**Für jeden Hersteller folgende Spalten:**
| Firma | Land/Ort | Formate (Kapsel/Pulver-Churna/Tee/Öl/Tinktur) | MOQ (Startwert) | Zertifizierungen (GMP, ISO 22000, IFS, HACCP, Bio/Öko-Kontrollstelle) | Rezepturentwicklung/White-Label (ja/nein) | Eignung für Bio-Churna & ayurvedische Botanicals | Schadstoff-/CoA-Kompetenz (Schwermetalle/Pestizide) | Website-URL |

**Qualitätskriterien (wichtig):** Ayurveda-Rohware ist schadstoffkritisch – priorisiere Hersteller mit dokumentierter **Schwermetall-/Pestizid-Prüfung (CoA), GMP/IFS und Bio-Zertifizierung**. Markiere Anbieter mit echter **Pulver/Churna-, Tee- oder Öl-/Tinktur-Kompetenz** und mit **niedrigem MOQ** besonders.

**Bereits bekannte Partner (NICHT als neu listen, nur erwähnen falls relevant):** BHI Biohealth International, German's Best, GMPP, Goerlich Pharma, Kasimir und Lieselotte, Nexum Production, Ourvita Germany, Pure Flavour, TINY Trade (alle DE); HKS Health Solutions, Trisolve (AT); BIO PAK Nutraceuticals (SI).

**Output:** (1) Gesamttabelle mit allen gefundenen NEUEN Herstellern (Ziel: 40–60), (2) eine Kurz-Empfehlung der Top-10 für ein Bio-Churna, (3) vollständige Quellenliste mit URLs. Wenn Angaben unsicher sind, kennzeichne sie als „zu bestätigen".

---

## Nach dem Gemini-Lauf
Exportiere das Ergebnis als Markdown nach Google Drive (analog zum bestehenden Gemini-Pfad) und gib mir den Link / den Text — ich führe es mit unserer parallelen Recherche und der bestehenden 12er-Liste in `06-hersteller-eu.md` zu einer deduplizierten Master-Liste mit Scoring zusammen.
