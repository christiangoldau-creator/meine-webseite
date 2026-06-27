# 03 – Sourcing-Pipeline: „Von Null bis in den Shop"

> Vollständiger Stage-Gate-Prozess für die Supplement-Produktentwicklung – von der Kongress-Idee bis zum verkaufsfertigen Produkt im Viktilabs-Shop. Mit Entscheidungstoren (GO/HOLD/KILL), parallelen Tracks, Rollen, Dauer und Kosten. Stand: 2026-06-27.

## Meine Empfehlung: Wie die optimale Pipeline aussieht

Bevor die Detailstufen kommen, mein eigener Blick auf das Zielbild – weil die Pipeline mehr leisten muss als „ein Produkt bauen". Sie muss **kontinuierlich aus 90 Kongressen Produktchancen ernten, sie diszipliniert filtern und die Gewinner schnell in den Shop bringen** – und das mit dem vorhandenen Team und Stack.

**Drei Designprinzipien:**

1. **Trichter, nicht Fließband.** Am Anfang stehen viele billige Ideen, am Ende wenige teure Produktionsentscheidungen. Die teuren Schritte (Rezeptur-R&D, Erst-Inventar 10–40 k€) dürfen erst nach den billigen Filtern (Regulatorik-Vorprüfung 0,8–2,5 k€, Business Case) kommen. **Das wichtigste Tor ist G3 (Regulatorik) – es liegt bewusst früh**, weil bei Ayurveda-Botanicals die meisten Show-Stopper rechtlicher Natur sind (Novel Food, Ashwagandha-Verbotsrisiko, nicht-auslobbare Claims). Jeder Euro, der hier ein Konzept killt, spart fünfstellige Beträge später.

2. **Zwei Geschwindigkeiten.** Nicht jedes Produkt braucht 30 Wochen. Ich empfehle **zwei Bahnen**:
   - **Fast-Track (White-Label/Reformat, 8–12 Wochen):** bestehende Hero-Wirkstoffe in neuem Format/neuer Aufmachung (z. B. Goldene-Milch-Churna, neue Bundles). Niedriges Risiko, schneller Umsatz.
   - **Custom-Track (Neuentwicklung, 20–32 Wochen):** echte neue Botanical-Komplexe mit eigener Rezeptur, Stabilitätsdaten, Novel-Food-Klärung.

3. **Auf dem bestehenden Stack aufsetzen, nichts Neues erfinden.** Die Firma hat bereits die Architektur **Asana (Single Source of Truth) · Google Drive (Storage) · n8n (Orchestrator) · Claude API (Engine)** für die Content-Pipeline. Die Sourcing-Pipeline ist dieselbe Architektur mit anderem Inhalt: Asana-Projekt „Produkt-Pipeline" mit Custom-Fields = Gates, Drive-Ordner je Produkt, n8n-Workflows für die automatisierbaren Teile (Repeated-Claims-Mining aus Kongressen, RFQ-Automation → siehe [`04`](04-rfq-fabrik-automation.md), Compliance-Vorprüfung, Shopify-Push).

### Das Zielbild als Fluss

```
  ┌─ KONTINUIERLICHE IDEEN-QUELLE ──────────────────────────────┐
  │  90 Kongress-Transkripte ─▶ n8n + Claude "Repeated-Claims    │
  │  Miner" ─▶ Opportunity-Backlog in Asana (auto-priorisiert)   │
  └──────────────────────────────┬──────────────────────────────┘
                                  ▼
  G1 Idee  ▶  G2 Business Case  ▶  G3 REGULATORIK (Frühfilter!)
                                  │
        ┌─────────────── nach G3: zwei Bahnen ───────────────┐
        ▼                                                    ▼
   FAST-TRACK (8–12 Wo)                          CUSTOM-TRACK (20–32 Wo)
   White-Label/Reformat                          Neue Rezeptur + Stabilität
        └───────────────────────┬────────────────────────────┘
                                 ▼
   G4 Sourcing/RFQ ▶ G5 Muster/Stabilität ▶ G6 Etikett/Compliance
   ▶ G7 BVL-Anzeige ▶ G8 Produktionsfreigabe ▶ G9 Launch (Kongress→Mail→Shop)
   ▶ G10 Post-Launch-Review (T+90)

   Parallele Tracks: A Regulatory/QA · B Brand/Content · C Demand/CRM · D Stabilität
```

**Wichtigste Engpässe, die man aktiv managen muss:** (1) Stabilitätsdaten + Produktions-Slot (kritischer Pfad im Custom-Track), (2) Novel-Food-Klärung für standardisierte Extrakte (Monate Vorlauf), (3) der Health-Editor/Regulatory-Engpass (wie schon in der Content-Pipeline – feste Wochenstunden vereinbaren).

---

## Der Stage-Gate-Prozess im Detail

Klassisches **Stage-Gate®-Modell (Cooper)**: abgegrenzte Arbeitsstufen, getrennt durch Tore mit harten **GO/HOLD/KILL**-Kriterien. Querschnitt (Regulatorik, QA, Content) läuft als **paralleler Track**. **10 Gates / 14 Stufen.**

> **Kalibrierungs-Faustregeln (recherchiert):**
> - White-Label (nur eigenes Label): 4–8 Wo · Private Label (leichte Anpassung): 8–16 Wo · Custom (neue Multi-Ingredient-Rezeptur): 6–12 Monate
> - Custom-R&D/Formulierung: 2.000–10.000+ €/SKU · Labortests: 1.000–3.000 €/Produkt · versteckte Compliance-Kosten: +20–40 % auf Stückpreis
> - **MOQ nach Format:** Kapseln/Pulver am niedrigsten (DE realistisch 1.000–5.000) · Liquid/Tropfen 1.000–5.000 · **Softgels 10.000–30.000+ (Nischen-Killer)** · Tee/Pulver 500–3.000

### Übersicht: Stufen, Gates, Owner

| # | Stufe | Gate | Owner | Dauer |
| --- | --- | --- | --- | --- |
| 1 | Ideen-/Opportunity-Findung | **G1 Idea Screen** | Head of Product | 1–2 Wo |
| 2 | Markt-/Wettbewerbs-/Evidenz-Validierung | **G2 Business Case** | Product + Data | 2–3 Wo |
| 3 | **Regulatorik-Vorprüfung** | **G3 Regulatory Clearance** | Regulatory/Legal | 1–2 Wo (parallel zu 2) |
| 4 | Rezeptur & Rohstoffe | — | Product + R&D (Hersteller) | 2–4 Wo |
| 5 | Lohnhersteller-Auswahl & RFQ | **G4 Sourcing & Cost** | Procurement | 2–4 Wo |
| 6 | Bemusterung & Stabilität | **G5 Sample/Stability** | QA | 3–12 Wo |
| 7 | Naming & Branding | — | Brand/Marketing | 2–3 Wo (parallel) |
| 8 | Verpackung / Darreichungsform | — | Product + Packaging | 2–4 Wo (parallel) |
| 9 | Etikett & Compliance | **G6 Label Compliance** | Regulatory | 2–3 Wo |
| 10 | BVL-Anzeige (§ 5 NemV) | **G7 Notification Done** | Regulatory | < 1 Tag |
| 11 | Produktionsfreigabe | **G8 Production Release** | QA + Ops | 4–10 Wo (Lieferzeit) |
| 12 | Shopify-Listing / Content / SEO | — | E-Commerce | 2–4 Wo (parallel ab G6) |
| 13 | Launch über Kongress / E-Mail | **G9 Go-to-Market** | Growth/CRM | Launch-Woche |
| 14 | Tracking & Iteration | **G10 Post-Launch Review** | Product + Data | fortlaufend (T+90) |

**Parallele Tracks:** A Regulatory/QA (ab Stufe 3) · B Brand/Content (ab G2) · C Demand/CRM (ab G2, Kongress-Slot reservieren) · D Stabilität (ab Stufe 6, läuft bis nach Launch für volles MHD).

---

### Die Gates im Detail (GO/HOLD/KILL)

**G1 Idea Screen** — *GO:* Audience-Fit + bestehender Kanal (Kongress→Mail→Shop) + Marge ≥ 65 % DB1. *HOLD:* kein Kongress-Slot in 6 Mt. *KILL:* kein Kanal-Fit / Me-too ohne Margenvorteil / MOQ-Killer-Format (Softgel 30.000+).
Input: Shopify-Lücken, umsatzstarke Kongressthemen, ActiveCampaign-Daten. Kosten ~0 €.

**G2 Business Case** — *GO:* Break-even ≤ 50 % der Erst-Charge; Ziel-DB1 ≥ 70 %; belastbare Evidenz. *HOLD:* Evidenz dünn → Claim-Strategie klären. *KILL:* Marktpreis drückt Marge < 60 %. Kosten 0,5–2 k€ (Tools).

**G3 Regulatory Clearance** ⭐ *(wichtigstes Frühgate)* — *GO:* alle Stoffe verkehrsfähig, kein Novel-Food-Konflikt, ≥ 1 tragfähiger Claim **oder** klares Positionierungs-Konzept ohne Heilversprechen. *HOLD:* Stoff auf On-Hold/in Bewertung → umbauen. *KILL:* Novel Food ohne Zulassung / national verboten.
Output: Ampel je Inhaltsstoff, Höchstmengen, vorläufige (nur zugelassene) Claim-Liste. Kosten 0,8–2,5 k€ (Sachverständiger/Kanzlei).
> Verbindliche Befunde: **Ashwagandha** unter EU-Art.-8-Verfahren (DK-Verbot, FR-Liste) → Bestandsrisiko, Plan B vorsehen. **Botanical-Claims faktisch eingefroren** (EuGH 30.04.2025, BGH 05.06.2025) → keine wirkungsbezogene Werbung. Triphala/Brahmi/Shatavari grundsätzlich verkehrsfähig, aber **standardisierte Extrakte** stoffspezifisch auf Novel Food prüfen.

**G4 Sourcing & Cost** — *GO:* zertifizierter EU-Partner (GMP/IFS), MOQ ≤ geplantes Erst-Inventar, Ziel-DB ≥ 70 %, Etikett-Compliance-Check zugesagt. *HOLD:* nur 1 Angebot / MOQ zu hoch → Format wechseln. *KILL:* keine Zertifizierung / Stückkosten sprengen Marge.
> RFQ an ≥ 3 Hersteller → Scorecard. Hersteller-Pool & Auswahlkriterien in [`06-hersteller-eu.md`](06-hersteller-eu.md). Die Angebots-*Verarbeitung* automatisiert [`04-rfq-fabrik-automation.md`](04-rfq-fabrik-automation.md).

**G5 Sample/Stability** — *GO:* Muster spec-konform, beschleunigte Stabilität ok, Schwermetalle unter Grenzwert. *HOLD:* grenzwertig → Rezeptur/Verpackung anpassen. *KILL:* Wirkstoffabbau/mikrobielle Last nicht beherrschbar.
Labore (ISO 17025): Eurofins, BAV-Institut (Tentamus), SGS Fresenius, Intertek, AGROLAB. Tests 1–3 k€/Produkt; beschleunigte Stabilität 6–12 Wo (Echtzeit läuft weiter).

**G6 Label Compliance** — *GO:* Etikett + Claims von Regulatory/Kanzlei freigegeben. *HOLD:* strittiger Claim → streichen. *KILL:* nur mit Heilversprechen verkaufbar.
Pflichtangaben (NemV + LMIV 1169/2011): Verkehrsbezeichnung, Wirkstoffe + Mengen/Tagesportion, empf. Tagesdosis + „nicht überschreiten", „ersetzt keine ausgewogene Ernährung", „außerhalb der Reichweite von Kindern", verantwortl. Unternehmer, Allergene, Nährwert, Los/MHD. Kosten 0,5–2 k€.

**G7 Notification Done** — *GO:* BVL-Übermittlungsbestätigung liegt vor. Anzeige § 5 NemV über BVL-Onlineportal (**ab 01.07.2026 nur digital im Bundesportal**), kostenfrei. *Wichtig:* Anzeige ≠ Verkehrsfähigkeitsbescheinigung (optional über Sachverständigen, empfohlen bei Ayurveda-Botanicals).

**G8 Production Release** — *GO:* Chargen-CoA spec-konform, Etikett korrekt, MHD gedruckt, BVL-Anzeige erfolgt. *HOLD:* Out-of-Spec → Nachprüfung. *KILL:* Charge nicht konform → Reproduktion.
Lieferzeit 4–10 Wo. Hauptkostenblock = Erst-Inventar (z. B. 5.000 × ~5–9 € ≈ 25–45 k€).

**G9 Go-to-Market** — *GO:* Bestand ≥ Launch-Forecast, PDP & E-Mails compliance-geprüft, Tracking gesetzt. *HOLD:* Bestand knapp → Soft-Launch/Waitlist.
Launch über Kongress-Erwähnung (vertraglich ≥ 4 Mikronährstoff-Slots/Kongress) → ActiveCampaign-Sequenz → Shop, Bundle analog „Supplementboxen Veda MC Wechseljahre".

**G10 Post-Launch Review (T+90)** — *GO (Scale):* Sell-through-Ziel + DB ≥ Plan → Nachproduktion (degressive Stückkosten ~8,6 → ~4,2 €/Einheit). *HOLD (Optimize):* PDP/Preis/Bundle iterieren. *KILL (Discontinue):* Abverkauf < Schwelle → Rest abverkaufen, SKU streichen.

---

## Timeline & Kosten

**Kritischer Pfad (Custom-Ayurveda-Komplex):** G1–G3 (Wo 1–4) → Rezeptur/Sourcing (Wo 4–8) → Bemusterung + parallel Branding/Packaging/Etikett (Wo 8–16, Stabilität bis ~20) → BVL (~16) → Produktion (16–26) → Listing (ab 14) → Launch (~26–28) → Review (~40).
→ **Custom ~20–32 Wochen · White-Label-Reformat ~8–12 Wochen.**

| Kostenblock je SKU (Erst-Charge 3.000–5.000 St.) | Range (€) |
| --- | --- |
| Regulatorik-Vorprüfung + Etikett-/Claim-Review | 1.300 – 4.500 |
| Rezeptur-/R&D-Fee (Custom) | 1.800 – 9.000 |
| Labor-Tests + Stabilität | 1.800 – 5.500 |
| Verpackung Tooling/Druck + Design/Foto/Copy | 1.000 – 6.000 |
| Marken-/Domain-/optional Verkehrsfähigkeitsbescheinigung | 300 – 3.000 |
| **Erst-Inventar (Stückkosten × MOQ)** | 10.000 – 40.000 |
| **Summe pro SKU** | **~15.000 – 60.000** |

White-Label ohne R&D/Tooling am unteren Ende; Custom-Liquid/Komplex am oberen Ende.

---

## Drei Pipeline-Leitplanken für Veda360 (aus der Recherche)

1. **Format = Margen- & Geschwindigkeitshebel:** Kapsel + Pulver/Churna + Tee (niedrige MOQ, kurze Lead Times), **Softgels meiden**. Schließt zugleich die Format-Lücke.
2. **Ashwagandha-Risiko managen:** keine neue strategische SKU allein auf Ashwagandha; diversifizieren (Triphala, Brahmi, Shatavari/Mönchspfeffer), jeweils in G3 stoffrechtlich absichern.
3. **Claim-Disziplin als Marken-Asset:** Positionierung über Tradition/Qualität (Standardisierung, schwermetallgeprüft, Glas) statt Wirkung – passt zum Marken-Korridor und senkt Abmahnrisiko.

---

## Wie sich das in den Stack einklinkt (Automatisierungsgrad je Stufe)

| Stufe | Automatisierbar via n8n/Claude? | Mensch entscheidet |
| --- | --- | --- |
| 1 Ideen | **Hoch** – „Repeated-Claims-Miner" (Kongress-Transkripte → Claude → Asana-Backlog mit Score) | Priorisierung am G1 |
| 2 Business Case | Mittel – Wettbewerbspreis-/SEO-Scraping, Claude-Entwurf | Freigabe G2 |
| 3 Regulatorik | Mittel – Claude-Vorprüfung gegen Novel-Food-Katalog/On-Hold-Liste als **Entwurf** | Sachverständiger zeichnet G3 |
| 5 RFQ | **Hoch** – siehe [`04`](04-rfq-fabrik-automation.md): RFQ-Versand, Angebots-Extraktion, Vergleich, Nachfass | Lieferantenwahl G4 |
| 9 Etikett/Content | Mittel – Claude generiert PDP/E-Mail **HCVO-vorgefiltert** | Regulatory-Freigabe G6, Launch G9 |
| 14 Tracking | **Hoch** – Shopify/ActiveCampaign-KPIs → Asana-Report | Scale/Kill G10 |

Die regulatorischen Pflichtpunkte sind als Checkliste in [`05-regulatorik-und-compliance.md`](05-regulatorik-und-compliance.md) konsolidiert; die Hersteller-Auswahl in [`06-hersteller-eu.md`](06-hersteller-eu.md).
