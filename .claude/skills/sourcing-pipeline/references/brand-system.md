# Viktilabs Markensystem & Mockup-Prompts

## Visuelle DNA (aus echten Produktbildern abgeleitet)

- **Logo:** „+viktilabs" — Kleinschreibung, mit führendem „+", in **Pfirsich/Creme**.
- **Hintergrund:** je Produkt eine **eigene, kräftige Vollton-Farbwelt** als Gradient (oben dunkler → unten heller), mit einem **großen, schwach sichtbaren „V"-Wasserzeichen** und einer **zweifarbigen horizontalen Boden-Linie** (Produkt steht auf einer „Fläche").
- **Label, zweizonig:** obere, hellere Zone trägt das Logo; untere, gesättigte Block-Zone trägt den **großen, fetten Uppercase-Produktnamen** in weißer Sans-Serif, darunter eine **dünne GOLDENE Linie**, darunter ein **Untertitel**.
- **Weitere Label-Elemente:** ein **rundes Siegel/Badge**, eine **Feature-Zeile** (z. B. „Bio | Vegan | Laborgeprüft"), Füllmenge („Inhalt: e 150 g Pulver"), beim Glas ein **seitliches Nährwert-/Textpanel**.
- **Typo:** fette, geometrische Sans, Uppercase-Produktnamen, Goldlinie als wiederkehrendes Signatur-Element.

## Verpackungsformen (zwingend)

| Darreichungsform | Verpackung | Echtes Referenzprodukt |
| --- | --- | --- |
| Pulver / Churna | **Doypack** (matter Standbeutel) | Kollagen-Hydrolysat (türkis) |
| Kapseln / Presslinge | **Braunglas + schwarzer Schraubdeckel** | OPC (rot/pink) |

Farbwelt pro Produkt frei wählen, aber zur Funktion passend (z. B. Morgen = Sonnenaufgangs-Gold, Abend = Plum/Twilight). Innerhalb einer Linie zwei Farbwelten als Paar lesbar machen (gemeinsamer Goldstrich + gleiches Logo).

## Prompt-Baukasten (Front-Mockup)

Edit-Endpoint (`gen_openai_edit.py`) mit passendem Referenzbild, oder Nano Banana (`gen_gemini.py`). Schema:

> „Redesign this exact [Doypack pouch | brown-glass jar] into a NEW product while keeping the SAME brand identity, label architecture, photographic style and composition: same '+viktilabs' lowercase peach wordmark, same two-zone label (lighter upper zone, darker saturated lower block), the SAME big bold uppercase white product name with a thin GOLD underline, a subtitle, [a small round seal + bottom fill-weight line + feature line | a side nutrition panel]. Keep the signature solid-color background with the large faint 'V' watermark and the two-tone horizontal floor line. Change ONLY: recolor to a <FARBWELT> palette. Print this German text, spelled correctly: name '<NAME>', subtitle '<UNTERTITEL>', [bottom 'Inhalt: e 150 g Pulver', feature line '<...>']. Photorealistic, premium, sharp legible label text."

Hinweise:
- **Umlaute im Label-Text meiden** (`fuer`, `Laborgeprueft`) — sie rendern oft falsch. Für den Druck ohnehin egal (Grafik setzt Typo nach).
- **Lifestyle/Detail:** das fertige Front-Bild als Referenz geben + Szene beschreiben → Label bleibt konsistent.
- **Duo-/Bundle-Shot:** beide Front-Bilder als Referenzen, Gradient-Backdrop, der die zwei Farbwelten verbindet (z. B. Gold→Plum für Tag→Nacht). Dauert lang → Hintergrund.

## Erprobte Beispiele (haben funktioniert)

- **MORGENGOLD** (Pulver/Doypack, Sonnenaufgangs-Gold): Untertitel „Morgen-Churna Golden Milk mit Kurkuma & Ingwer", Feature „Ayurveda-Ritual | Bio | Vegan | Laborgeprueft", „Inhalt: e 150 g Pulver".
- **NACHTGOLD** (Kapsel/Braunglas, Abend-Plum): Top-Zeile „Abend-Komplex fuer Frauen", Untertitel „Magnesium-Bisglycinat + Shatavari + Brahmi".

Beide als spiegelbildliches Tag/Nacht-Paar einer Linie (Aronal/Elmex-Logik): gemeinsamer „…GOLD"-Namensstamm, Gold- vs. Plum-Welt.

## Immer mitliefern
„Mockup = Konzept/Moodboard, **keine Druckvorlage** — Etikett-Typo & Pflichtangaben setzt die Grafik anschließend sauber."
