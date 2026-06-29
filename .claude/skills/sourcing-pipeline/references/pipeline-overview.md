# Pipeline-Übersicht & Doc-Mapping

Wissensbasis-Repo: `C:\Users\state\meine-webseite\supplement-sourcing-zero-to-hero\`
(Branch `claude/supplement-sourcing-github-unk0l9`). Vor inhaltlicher Arbeit das passende Doc lesen.

| Stufe | Inhalt | Repo-Doc |
| --- | --- | --- |
| Kontext | Ausgangslage, Markenstruktur, Viktilabs-Katalog-Lücke | `00-situationsanalyse.md` |
| 1 Transkripte | Vimeo-API-Transkripte ziehen | `10-vimeo-transcript-integration.md` + `tools/vimeo_transcripts.py` |
| 2 Claims-Mining | konsolidierte Produktinnovations-Analyse; frequenzgerankter Backlog | `01-analyse-ayurveda-kongress.md`, `11-claims-mining-und-empfehlung.md` |
| 3 Produktideen | Konzepte + adversariale Bewertung (GO/CAUTION/KILL) | `02-produktideen.md` |
| Pipeline-Architektur | Stage-Gate „von Null bis in den Shop", 10 Gates | `03-sourcing-pipeline.md` |
| 5 RFQ-Automation | Gmail→n8n→Claude→Asana, Scoring | `04-rfq-fabrik-automation.md` |
| 4 Regulatorik (G3) | Ampel je Botanical, Novel Food, HWG/HCVO, NemV | `05-regulatorik-und-compliance.md` |
| 5 Hersteller | EU-Lohnhersteller (Master + Longlist) | `06-hersteller-eu.md`, `06b-hersteller-longlist-eu.md`, `gemini-brief-lohnhersteller.md` |
| 6 Produzierbarkeit | Spezifikation, BOM, CoA — je Produkt | `07-…churna.md`, `12-…golden-age-abendritual.md` |
| 5 RFQ-Versand | versandfertige Hersteller-Anfrage | `08-rfq-anfrage-…churna.md` |
| Simulation | Komplettdurchlauf aller Schritte (Beispiel) | `09-simulation-…churna.md` |
| 7 Produktseiten | PDP-Copy je Produkt | `13-…`, `14-…` |
| Cockpit | visuelle Status-/Konzept-Übersicht | `cockpit.html`, `simulation.html` |
| 7 Design-Assets | Mockups, PDP-HTML | `design/` |

## Arbeitsprinzipien
- **Neue Outputs** als nächstes nummeriertes Doc im Repo ablegen (gleicher Stil, Datums-Stand, Quellen verlinken).
- **Adversariale Verifikation**: Konzepte/Behauptungen kritisch gegenprüfen (eigener Skeptiker-Blick) — lieber früh killen als nach der Erstcharge.
- **Regulatorik ist Frühfilter (G3)**, nicht nachgelagert: Novel Food, AM-Dosis, Verbots-/Warnstoffe, Schadstoffe gelten **claim-unabhängig**.
- **Funnel-Burggraben**: Kongress → E-Mail → Shop; Vermarktung über Aufklärung, nicht über Produkt-Claims.
- **Bekannte Leitplanken**: Ashwagandha = regulatorisch ROT (nicht skalieren); Shatavari-Vollwurzel statt Extrakt + Art.-4-NF-Konsultation; Curcumin-ADI (~210 mg/Tag) + Piperin ≤ 2 mg; Brahmi ≤ 250 mg + Schilddrüsen-Warnhinweis.
