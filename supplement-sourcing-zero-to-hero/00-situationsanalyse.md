# 00 – Situationsanalyse (Ausgangslage)

> Interner Kontext, auf gesicherten Daten aus Shopify (Viktilabs), Google Drive und der bestehenden Kongress-Pipeline. Stand: 2026-06-27.

## 1. Markenarchitektur

| Marke | Rolle | Audience |
| --- | --- | --- |
| **Medumio** | Gesundheitsakademie, ~90 Online-Kongresse (Autoimmun, Endometriose, Skelett/Gelenke, Wechseljahre, ADHS, Vitalpilze …) | Gesundheitsaffin, 45–65, kritisch ggü. reiner Schulmedizin |
| **Veda360** | Ganzheitlich/ayurvedisch positionierte Kongress-Marke (Wechseljahre, Stress/Nervensystem, Frauengesundheit, Pflanzenmedizin, Myzel) | Überwiegend Frauen 45–65, kaufstark bei Digitalprodukten |
| **Curivo** | Dritte Kongress-/Mail-Marke (ActiveCampaign-Portal) | — |
| **Viktilabs** | Supplement-Eigenmarke (Shopify Plus, `viktilabs.de`, DE, EUR) | Kund:innen aus dem Kongress-Funnel + DTC |

**Wertschöpfungslogik / stärkster Vertriebsweg:**
`Kongress (Medumio/Veda360) → E-Mail-Funnel (ActiveCampaign) → Viktilabs-Shop`

Das ist der entscheidende strukturelle Vorteil: Wir besitzen die **Audience** *vor* dem Produkt. Ein neues Supplement muss nicht „kalt" in den Markt – es kann an einen bereits laufenden, themenscharfen Kongress angedockt werden. Genau das ist die Kernidee dieses Projekts: **Produkte aus dem Kongressthema heraus entwickeln**, statt umgekehrt.

## 2. Das Problem (vom Auftrag)

Der **Ayurveda-/Veda360-Kongress** erzielt hohe Digitalprodukt-Umsätze, aber es gibt **kein passendes Supplement-Sortiment**, das die Audience nach dem Kongress monetarisiert. Es fehlt sowohl an Botanicals als auch an passenden Darreichungsformen.

## 3. Viktilabs-Katalog: Bestand & Lücke (Ayurveda)

### Bestand (ayurveda-relevant, bestätigt aus Shopify)

| Produkt | Wirkstoff | Format | VK | Status | Lager |
| --- | --- | --- | --- | --- | --- |
| Bio Ashwagandha (KSM-66®) | 5 % Withanolide | Kapseln | 24,90 € | ACTIVE | ~19.500 (sehr hoch) |
| Curcuma-Komplex | 95 % Curcuminoide + Piperin | Kapseln | 18,90 € | ACTIVE | ~7.800 (hoch) |
| Schlummerzeit-Paket | Ashwagandha + Magnesium + L-Tryptophan + Melatonin | Bundle | 63,18 € | ACTIVE | — |
| Frauenwohl-Paket | Mönchspfeffer + Eisen + Omega-3 + Ashwagandha | Bundle | 74,34 € | ACTIVE | — |

**Sortimentsstruktur gesamt (~96 Produkte):** stark in **Kapseln (62)** und **flüssig/Tropfen (25)**, wenige **liposomal (3)**. Indikations-Collections existieren bereits für Stress, Schlaf, Hormone, Frauengesundheit/Fruchtbarkeit, Darm, Entzündung, Gelenke, Leber, Schilddrüse, Vitalpilze u. a. – die thematische Infrastruktur im Shop ist also vorhanden.

### Lücke (das eigentliche Sourcing-Feld)

1. **Botanical-Lücke:** Außer Ashwagandha & Curcumin fehlen die klassischen Ayurveda-Botanicals praktisch vollständig – u. a. **Triphala, Brahmi/Bacopa, Shatavari, Tulsi (Holy Basil), Amla/Amalaki, Boswellia, Moringa, Guggul, Gotu Kola, Trikatu**.
2. **Format-Lücke:** Im Ayurveda-Bereich gibt es **keine Pulver/Churna, keine Tees, keine Öle, keine Tinkturen** – obwohl genau diese Formate die ayurvedische Anwendungswelt (Abhyanga-Öl, Churna, Kräutertee) authentisch abbilden und Differenzierung + Wiederkauf ermöglichen.
3. **Linien-Lücke:** Es gibt keine als **Ayurveda-Linie** gebündelte, dosha-/themenbasierte Produktwelt, an die der Kongress andocken kann.

> **Wichtig fürs Sourcing:** Ashwagandha & Curcumin haben hohe Lagerbestände. Neue Konzepte sollten diese **ergänzen** (neue Botanicals und/oder neue Formate), nicht kannibalisieren.

## 4. Vorhandene Pipeline-Architektur (Referenz)

Es existiert bereits eine **halbautomatische Content-Pipeline** (Dokument *pipeline-architektur-skelett.md*) mit klaren Architektur-Konventionen, die wir für die Sourcing-Pipeline wiederverwenden sollten:

- **Asana** = Single Source of Truth für Status & Aufgaben (Custom Fields, Status-Lifecycle, Sections)
- **Google Drive** = Storage für Recherche-Material & Deliverables (feste Ordnerstruktur pro Vorgang)
- **n8n** = Orchestrator zwischen den Systemen (getrennte, versionierte Workflows)
- **Claude API** = Extraktions- & Veredelungs-Engine (Prompts als versionierte `.txt` in Git)
- Bewährtes **Error-Handling-Pattern**: 3 Retries mit Backoff, bei Final-Failure Slack-Alert + Asana-Comment, Status bleibt „stuck-sichtbar".

Der existierende **Kongress-Extraktions-Workflow** (n8n zieht Transkripte aus Drive → Claude extrahiert Kernaussagen) ist die direkte Vorlage für den **„Repeated-Claims-Miner"**, mit dem wir aus den ~90 Kongressen wiederkehrende Experten-Aussagen über Supplemente gewinnen.

## 5. Konsequenz für dieses Projekt

Die Sourcing-Pipeline ist im Kern eine **Erweiterung der bestehenden Architektur** um eine Produkt-statt-Artikel-Logik:

```
Kongress-Transkripte ──▶ Repeated-Claims-Miner (Claude) ──▶ Opportunity-Matrix
                                                                   │
                                                                   ▼
            ┌──────── Stage-Gate-Produktpipeline (Asana = SSOT) ────────┐
            │  Idee → Validierung → Regulatorik → Rezeptur → RFQ/        │
            │  Hersteller → Bemusterung → Branding/Verpackung → Etikett/ │
            │  Compliance → BVL-Notifizierung → Shopify-Launch → Tracking│
            └────────────────────────────────────────────────────────────┘
                                                                   ▲
            RFQ-/Angebots-Automation (Gmail → n8n → Claude → Asana) ┘
```

Die Detailausarbeitung (Markt, Evidenz, Konzepte, Stage-Gates, RFQ-Automation, Regulatorik, Hersteller) folgt in den Dokumenten `01`–`06`.
