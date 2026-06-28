# 08 – Versandfertige Hersteller-Anfrage (RFQ): Goldene-Milch-Churna

> Direkt verwendbare Anfrage an EU-Lohnhersteller. Platzhalter in `[…]` vor dem Versand ausfüllen. Diese RFQ ist zugleich das Eingabe-Template für die RFQ-Automation aus [`04`](04-rfq-fabrik-automation.md). Stand: 2026-06-27.

## RFQ-Stammdaten (für Asana / Automation)

| Feld | Wert |
| --- | --- |
| RFQ-ID | `RFQ-2026-0001` |
| Produkt-Arbeitstitel | Goldene-Milch-Churna 150 g |
| Format | Loses Pulver / Churna (Vollfrucht/Gewürz, **kein Extrakt**) |
| Ziel-MOQ (Erstcharge) | 1.000–3.000 Dosen à 150 g (bitte Staffel ab Kleinstcharge angeben) |
| Zielpreis/Einheit | ≤ 4,00 € / 150-g-Dose (Zielmarge ~75 %) |
| Ziel-Liefertermin | `[Datum]` (ca. 8–12 Wochen nach Freigabe) |
| Versendet an | Drexel Private Label · Naturtheke · VehGro |
| Antwort erbeten bis | `[Datum, +14 Tage]` |

---

## E-Mail-Text (kopierfertig)

**Betreff:** `[RFQ-2026-0001] Anfrage Lohnherstellung Bio-Churna (Pulvermischung) – Viktilabs`

> Sehr geehrte Damen und Herren,
>
> wir, **Viktilabs** (Supplement-Eigenmarke, DE), planen die Einführung einer aromatisierten Bio-Pulvermischung („Goldene-Milch-Churna") und bitten um ein Angebot zur Lohnherstellung/Lohnabfüllung im Private Label.
>
> **Produkt:** lose Pulvermischung auf Basis von Triphala-, Amla-, Kurkuma-, Ingwer-, Ceylon-Zimt- und Kardamom-Pulver (Vollfrucht/Gewürz, **keine Extrakte**), Bio, vegan, ohne Zusatz-/Füllstoffe. Endgebinde **150-g-Dose** (Glas oder Mono-Material-Doypack). Rezeptur-Feinabstimmung gern gemeinsam.
>
> Die vollständige Spezifikation inkl. Rezeptur-Richtwerten und Qualitätsanforderungen ist angehängt. Bitte beantworten Sie die untenstehenden Punkte.
>
> Mit freundlichen Grüßen
> `[Name]`, Viktilabs · `[Kontakt]`

---

## Spezifikations- & Angebotsblatt (Anhang zur RFQ)

### A) Rezeptur (Richtwerte, finalisierbar)
Triphala (Amalaki/Bibhitaki/Haritaki 1:1:1) ~35 % · Amla ~14 % · Kurkuma-**Pulver** ≤ 15 % · Ingwer ~10 % · Ceylon-Zimt (*Cinnamomum verum*, **nicht** Cassia) ~10 % · Kardamom ~5 % · optional Kokosblütenzucker ~10 % · schwarzer Pfeffer: Prise (Piperin ≤ 2 mg/Tagesportion). Alles **Bio (EU-Öko)**.

### B) Bitte je Punkt beantworten
1. **Machbarkeit & Rezeptur:** Können Sie diese Mischung herstellen? Eigene R&D/Rezepturoptimierung möglich? Vorschläge zu Geschmack/Löslichkeit?
2. **MOQ & Staffelpreise:** Mindestmenge + Preis/150-g-Dose bei 1.000 / 3.000 / 5.000 / 10.000 Dosen.
3. **Einmalkosten:** Setup/Rezepturentwicklung/Tooling.
4. **Lieferzeit** ab Freigabe (Wochen).
5. **Zertifizierungen:** GMP / ISO 22000 / IFS / HACCP / **Öko-Kontrollstelle (DE-ÖKO-Nr.)** – bitte Nachweise.
6. **Rohstoffherkunft & Rückverfolgbarkeit:** Herkunftsländer, eigene Lieferkette? Charge/Erntejahr dokumentiert?
7. **Verpackung:** Optionen 150-g-Glas vs. Doypack, Befüllung, Trockenmittel/Barriere, Etikettierung im Haus?
8. **Stabilität/MHD:** abgeleitetes MHD, Stabilitätsdaten verfügbar?
9. **Zahlungsziel & Angebotsgültigkeit.**

### C) Qualitäts-/Grenzwert-Anforderungen (K.-o.-Kriterium – CoA je Charge erforderlich)
Bitte bestätigen Sie die Einhaltung **und** liefern Sie ein chargenspezifisches CoA eines **akkreditierten Labors (ISO 17025)**:

| Parameter | Anforderung |
| --- | --- |
| Blei (Pb) | ≤ 1,0 mg/kg |
| Cadmium (Cd) | ≤ 1,0 mg/kg |
| Quecksilber (Hg) | ≤ 0,1 mg/kg |
| Arsen (anorg.) | ≤ 1,0 mg/kg |
| Pestizide | konform EU-MRL (VO 396/2005), Multimethod |
| Ethylenoxid (EtO) | nicht nachweisbar (≤ 0,1 mg/kg) |
| Aflatoxine | B1 ≤ 2 / Summe ≤ 4 µg/kg; Ochratoxin A ≤ 15 µg/kg |
| PAK (PAH4) | konform |
| Mikrobiologie | *Salmonella* / *E. coli* in 25 g nicht nachweisbar; TAMC, Hefen/Schimmel im Spez.-Rahmen |
| Botanische Identität | bestätigt, keine Streckung/Füllstoffe |
| Ausschluss | keine „Rasa shastra"/Bhasma-Rohstoffe |

> Hinweis: Wir prüfen Angebote u. a. nach Preis (35 %), Schadstoff-/CoA-Konformität (20 %), Zertifikaten (15 %), Lieferzeit (12 %), MOQ-Passung (10 %) und Rezeptur-Treue (8 %). Angebote ohne Schwermetall-CoA werden nicht berücksichtigt.

---

## Nach Eingang der Angebote
Die Antworten laufen über die **RFQ-Automation** ([`04`](04-rfq-fabrik-automation.md)): Claude extrahiert die Felder in das einheitliche JSON, prüft Schwermetalle hart gegen VO (EU) 2023/915, fehlende Pflichtangaben lösen eine automatische Rückfrage aus, und Workflow C erzeugt die gewichtete Vergleichstabelle als Entscheidungsvorlage. Die finale Lieferantenwahl trifft ein Mensch (Gate G4).
