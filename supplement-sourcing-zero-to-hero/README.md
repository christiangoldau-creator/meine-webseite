# Supplement Sourcing – From Zero to Hero

Strukturierte Sourcing- und Produktinnovations-Pipeline für **Viktilabs**-Supplements, die aus den **Medumio/Veda360-Kongressen** heraus entwickelt werden – von der Kongress-Erkenntnis bis zum verkaufsfertigen Produkt im Shop.

**Durchgespielt am Beispiel des Ayurveda-/Veda360-Kongresses.**

## Worum es geht

Die Kongresse (~90) besitzen eine warme, kaufstarke Audience – aber für viele Themen fehlt das passende Supplement-Sortiment. Dieses Projekt baut die Pipeline, die (1) aus Kongressinhalten + Markt + Amazon/Büchern + Web wiederkehrende Produktchancen erkennt, (2) daraus konkrete Produktkonzepte ableitet und bewertet, und (3) sie systematisch und teil-automatisiert „von Null bis in den Shop" bringt – inkl. Regulatorik, EU-Lohnfertigung und automatisierter Angebotsverarbeitung.

## Kernergebnisse (Ayurveda-Beispiel)

- **Sortimentslücke:** Viktilabs hat die Hero-Wirkstoffe Ashwagandha & Curcumin – aber nur als Kapseln. Es fehlen Botanicals (Triphala, Brahmi, Shatavari, Tulsi …) und Formate (Pulver/Churna, Tee, Öl).
- **Größte Markenchance:** „Frauengesundheit/Wechseljahre × Ayurveda × Evidenz" – von niemandem besetzt; **Shatavari** ist schwach gebrandet.
- **⚠️ Kritisches Risiko:** **Ashwagandha** (#1-Hero, ~19.500 Stück Lager) steht unter EU-Verbotsrisiko (Art.-8-Verfahren, DK-Verbot, BfR-Warnung). → diversifizieren, nicht hochskalieren.
- **Vertriebs-Burggraben:** Der Funnel `Kongress → E-Mail → Shop` ist einzigartig und sogar vertraglich verankert (≥4 Mikronährstoff-Interviews mit Viktilabs-Nennung pro Kongress).
- **6 Produktkonzepte** wurden generiert und **adversarial geprüft** (2× KILL, 4× CAUTION). Robusteste Plays: Goldene-Milch-Churna, Shatavari, Tulsi-Tee (Bundle), Brahmi.

## Dokumente

| Datei | Inhalt |
| --- | --- |
| [`00-situationsanalyse.md`](00-situationsanalyse.md) | Ausgangslage: Markenstruktur, Viktilabs-Katalog-Lücke, bestehende Pipeline-Architektur |
| [`01-analyse-ayurveda-kongress.md`](01-analyse-ayurveda-kongress.md) | Konsolidierte Produktinnovations-Analyse: Markt, Wettbewerb, Evidenz, Amazon/Bücher, Kongressinhalte, Opportunity-Matrix |
| [`02-produktideen.md`](02-produktideen.md) | 6 Produktkonzepte mit Scoring + ehrlicher adversarialer Bewertung (GO/CAUTION/KILL), Format-Vergleich, Roadmap |
| [`03-sourcing-pipeline.md`](03-sourcing-pipeline.md) | Stage-Gate-Pipeline „von Null bis in den Shop": 10 Gates, parallele Tracks, Rollen, Timeline, Kosten + Architektur-Empfehlung |
| [`04-rfq-fabrik-automation.md`](04-rfq-fabrik-automation.md) | Automatisierte Verarbeitung von Fabrik-Angeboten (Gmail→n8n→Claude→Asana): Schema, Workflows, Scoring, Rückfragen |
| [`05-regulatorik-und-compliance.md`](05-regulatorik-und-compliance.md) | Regulatorik-Ampel je Botanical, Novel Food, Schwermetalle, HCVO/HWG, NemV – Compliance-Checkliste |
| [`06-hersteller-eu.md`](06-hersteller-eu.md) | EU-Lohnhersteller-Shortlist je Format + Format-/Margen-Ökonomie (Kapsel vs. Pulver vs. Tee vs. Öl vs. Tinktur) |

## Die Pipeline in einem Satz

```
90 Kongresse → Repeated-Claims-Miner (Claude) → Opportunity-Backlog (Asana)
   → G1 Idee → G2 Business Case → G3 REGULATORIK (Frühfilter)
   → [Fast-Track 8–12 Wo | Custom-Track 20–32 Wo]
   → RFQ/Hersteller → Muster/Stabilität → Etikett/Compliance → BVL-Anzeige
   → Produktion → Launch (Kongress→Mail→Shop) → Post-Launch-Review
```

Architektur durchgängig auf dem vorhandenen Stack: **Asana** (Single Source of Truth) · **Google Drive** (Storage) · **n8n** (Orchestrator) · **Claude API** (Engine).

## Empfohlene erste Schritte

1. **Pilot-Produkt:** aromatisiertes **Goldene-Milch-Churna** (sauberste Rechtslage, niedrigstes MOQ, größte Differenzierung) – Fast-Track.
2. **Strategie-SKU:** **Shatavari** nach Novel-Food-Klärung – größte Markenlücke, umsatzstärkstes Veda-Thema.
3. **Infrastruktur:** Asana-Projekt „Produkt-Pipeline" + „RFQ-Angebote" anlegen, RFQ-Automation (Doc 04) bauen, RFQs für Top-3-Kapseln + 1 Churna an EU-Hersteller (Doc 06) senden.
4. **Risiko-Hausaufgabe:** Ashwagandha-Bestandsstrategie + Pflicht-Warnhinweise (Doc 05).

---

> Erstellt mit einer 18-Agenten-Recherche-Pipeline (Markt, Wettbewerb, Evidenz, Amazon/Bücher, Regulatorik, Hersteller, Ökonomie, interne Kongressinhalte) inkl. adversarialer Verifikation. Alle Web-Befunde sind in den Dokumenten mit Quellen verlinkt. Marktzahlen kommerzieller Research-Häuser variieren methodisch – als Richtwerte zu lesen. **Kein Ersatz für lebensmittelrechtliche Beratung vor Produktentscheidungen.**
