# 07 – Produzierbarkeit: Hero-Produkt „Goldene-Milch-Churna"

> Produzierbarkeits-Stufe der Pipeline (Stage 4–6, Gates G3→G5) für das gewählte Pilot-Hero-Produkt. Enthält: gesperrte Produktdefinition, Rohstoffspezifikation (BOM), Grenzwerte/CoA-Anforderungen, passende Fabriken und offene Klärungspunkte. Stand: 2026-06-27.

## 1. Hero-Produkt-Definition (gesperrte Spezifikation)

| Merkmal | Festlegung |
| --- | --- |
| **Arbeitstitel** | Goldene-Milch-Churna (Veda-Linie) |
| **Format** | Loses Pulver / Churna (kein Extrakt, keine Kapsel) |
| **Packungsgröße** | 150 g Dose (Glas oder Mono-Material-Doypack), ~30 Portionen |
| **Tagesportion** | ca. 5 g (1 gestr. TL) in warme (Pflanzen-)Milch |
| **Positionierung** | Authentisches Ayurveda-Ritual, Bio, Premium, schadstoffgeprüft. Kein Wirkungs-Claim (HCVO) — Story über Tradition + Qualität |
| **Kongress-Anker** | Veda360 Darm / Pflanzenmedizin (sekundär: Wechseljahre als „Abendritual") |
| **Ziel-VK** | 16,90 € / 150 g · Ziel-COGS 2,50–4,00 € · Ziel-Marge ~75–78 % |

### Warum dieses Produkt als Pilot
Sauberste Rechtslage im gesamten Konzept-Feld (Vollfrucht/Gewürz statt standardisierter Extrakt → **geringes Novel-Food-Risiko**), niedrigstes MOQ (ab ~50-kg-Charge, keine Kapsellinie nötig), schließt die größte Format-Lücke (Churna) und löst das aus Rezensionen bekannte Triphala-Geschmacksproblem über die Aromatisierung.

> **⚠️ Kritische Design-Leitplanke (aus der adversarialen Prüfung):** Der **Curcumin-ADI** (EFSA: 3 mg/kg KG ≈ 210 mg/Tag) darf nicht tangiert werden. Deshalb: **Curcuma nur als Pulver** (kein Extrakt!), Anteil ≤ 15–20 % des Blends. Rechnung: 5 g Churna × 15 % = 750 mg Kurkumapulver × ~3 % Curcumin ≈ **~22 mg Curcumin/Tag** → weit unter ADI. **Piperin ≤ 2 mg/Tag** (BfR) → schwarzer Pfeffer nur als Prise.

## 2. Rezeptur & Bill of Materials (BOM)

Ziel-Blend (Richtwerte, durch Hersteller-R&D zu finalisieren):

| Komponente | Botanisch / Teil | Anteil | Funktion | Qualität |
| --- | --- | :--: | --- | --- |
| Triphala-Pulver | Amalaki (*Phyllanthus emblica*, Frucht) + Bibhitaki (*Terminalia bellirica*) + Haritaki (*Terminalia chebula*), 1:1:1 | ~35 % | Kern-Botanical (Darm/Rasayana) | Bio, Vollfrucht-Pulver |
| Kurkuma-Pulver | *Curcuma longa*, Wurzelstock | ≤ 15 % | Goldfarbe, Geschmack (ADI-limitiert!) | Bio |
| Ingwer-Pulver | *Zingiber officinale*, Wurzelstock | ~10 % | Wärme/Schärfe, Geschmack | Bio |
| Ceylon-Zimt | *Cinnamomum verum* (**nicht** Cassia – Cumarin!) | ~10 % | Geschmack | Bio, Ceylon (Cumarin-arm) |
| Kardamom | *Elettaria cardamomum* | ~5 % | Aroma | Bio |
| Amla-Pulver (zusätzl.) | *Phyllanthus emblica* | ~14 % | Antioxidans/Vitamin-C-Story | Bio |
| Kokosblütenzucker o. Ä. (optional) | — | ~10 % | Geschmacksrundung (oder weglassen für „zuckerfrei") | Bio |
| Schwarzer Pfeffer | *Piper nigrum* | Prise | Bioverfügbarkeit (Piperin ≤ 2 mg/Tag) | Bio |

**Vegan, glutenfrei, laktosefrei, ohne Zusatzstoffe/Füllstoffe** (Hygienefaktor laut Amazon-Rezensionssignalen). **Ceylon-Zimt statt Cassia** zwingend (Cumarin-Grenzwert).

## 3. Grenzwerte & CoA-Anforderungen (verbindlich je Charge)

Diese Werte sind die **Mindestanforderung an den Lieferanten** (im RFQ als K.-o.-Kriterium). Konservativ unter den gesetzlichen Höchstwerten angesetzt; finale matrixspezifische Werte mit Labor/Sachverständigem bestätigen.

| Parameter | Anforderung (Spezifikation) | Rechtsbezug |
| --- | --- | --- |
| **Blei (Pb)** | ≤ 1,0 mg/kg | VO (EU) 2023/915 (NEM ≤ 3,0; konservativ) |
| **Cadmium (Cd)** | ≤ 1,0 mg/kg | VO (EU) 2023/915 |
| **Quecksilber (Hg)** | ≤ 0,1 mg/kg | VO (EU) 2023/915 |
| **Arsen (anorg.)** | ≤ 1,0 mg/kg | VO (EU) 2023/915 / Reinheitskriterien |
| **Pestizide** | konform MRL VO (EG) 396/2005 (Multimethod) | EU-MRL |
| **Ethylenoxid (EtO)** | nicht nachweisbar (≤ 0,1 mg/kg, Summe) | EU-Pestizid-VO; RASFF-Dauerthema bei Asien-Gewürzen |
| **Mykotoxine** | Aflatoxin B1 ≤ 2 µg/kg, Summe B1/B2/G1/G2 ≤ 4 µg/kg; Ochratoxin A ≤ 15 µg/kg (Gewürze) | VO (EU) 2023/915 |
| **PAK (PAH4)** | konform (getrocknete/erhitzte Ware) | VO (EU) 2023/915 |
| **Cumarin** | über Ceylon-Zimt minimieren | LFGB / BfR |
| **Mikrobiologie** | TAMC, Hefen/Schimmel im Spez.-Rahmen; *E. coli* / *Salmonella* in 25 g: nicht nachweisbar | DGE/Apothekenstandard |
| **Identität/Reinheit** | botanische Identität bestätigt, keine Streckung/Füllstoffe | — |
| **Rückverfolgbarkeit** | Herkunftsland + Charge + Erntejahr; Bio über Öko-Kontrollstelle (DE-ÖKO-xxx) | EU-Öko-VO |

**Ausschluss:** „Rasa shastra"/Bhasma-Rohstoffe (gezielter Metallzusatz) strikt verboten. Akkreditiertes Drittlabor (ISO 17025), nicht nur Lieferanten-Selbstauskunft.

## 4. Passende Fabriken (Churna-Format)

Aus der Hersteller-Shortlist ([`06`](06-hersteller-eu.md)) für **Pulver/Churna** relevant:

| Hersteller | Land | MOQ | Rolle |
| --- | --- | --- | --- |
| **Drexel Private Label** | DE | projektabh. | Erstwahl: Bio-Pulver + Extrakte, >30 J., saubere Doku |
| **Naturtheke** | DE | **ab 50** | Markttest-/Kleinst-Charge vor Skalierung |
| **VehGro** | NL | teils kein MOQ | Bio-Rohstoffkatalog + Lohnfüllung kombinierbar |
| **Plantafood / TISSO** | DE | projektabh. | Full-Service-Alternative inkl. Bio, falls Kombi mit späteren Kapseln |
| *Rohware-Vorlieferant* | DE | industriell | MartinBauer für rückstandsgeprüfte Botanical-Rohware höchster Doku |

**Empfehlung:** RFQ an **Drexel + Naturtheke + VehGro** (3 Angebote, Pflicht für G4). Naturtheke ermöglicht eine echte Kleinst-Testcharge für den Sandbox-Durchlauf.

## 5. Verpackung & Stabilität

- **Primär:** 150-g-Braunglas (UV-Schutz, Premium) **oder** recyclebarer Mono-Material-Doypack (versandgünstig). Pulver feuchteempfindlich → Trockenmittel/Aluminium-Barriere prüfen.
- **Stabilität (G5):** Echtzeit + beschleunigt, Ziel-MHD ableiten; Wirkstoff-/Farbstabilität (Curcumin lichtempfindlich) und Feuchteaufnahme prüfen.

## 6. Offene Klärungspunkte (Gate-Checkliste)

- [ ] **G3:** Novel-Food-Status der Triphala-Einzelkomponenten (Terminalia chebula/bellirica) als Vollfrucht-Pulver final bestätigen (Vollfrucht eher unkritisch, aber dokumentieren)
- [ ] **G3:** finale Rezeptur gegen Curcumin-ADI rechnerisch belegen (Curcuma-% × Pulver-Curcumingehalt)
- [ ] **G4:** ≥ 3 Hersteller-Angebote, Schwermetall-CoA als K.-o.-Kriterium
- [ ] **G5:** Bemusterung sensorisch (Geschmack löst das Triphala-Bitterproblem?) + Stabilität
- [ ] **G6:** Etikett ohne Wirkungs-Claim; Allergene; Nettofüllmenge; Dosierhinweis
- [ ] **G7:** § 5 NemV-Anzeige BVL (bzw. Einstufung Lebensmittel/Gewürzmischung vs. NEM klären)

> **Hinweis zur Einstufung:** Ein reines aromatisiertes Churna kann je nach Auslobung als **NEM** *oder* als **Lebensmittel/Gewürzzubereitung** vermarktet werden. Lebensmittel-Einstufung = noch geringere Regulatorik (keine NemV-Anzeige), aber dann keinerlei nährstoffbezogene Aussagen. Vor G6 mit Sachverständigem festlegen.

Die konkrete, versandfertige Anfrage an die Hersteller steht in [`08-rfq-anfrage-goldene-milch-churna.md`](08-rfq-anfrage-goldene-milch-churna.md).
