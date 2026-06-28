# Onboarding: Supplement Sourcing – Zero to Hero

> Unternehmens-Leitfaden zur wiederverwendbaren **Sourcing-Pipeline**, mit der wir aus unseren Kongressen (Medumio/Veda360) neue **Viktilabs**-Supplemente entwickeln – von der Kongress-Idee bis zum verkaufsfertigen Produkt im Shop. Durchgespielt am **Ayurveda-Beispiel**.

## Was das ist (in einem Satz)
Eine teilautomatisierte **Stage-Gate-Pipeline + Claude-Code-Skill**, die Kongressinhalte, Markt-, Evidenz-, Amazon-, Regulatorik- und Hersteller-Recherche bündelt, daraus geprüfte Produktkonzepte ableitet und sie systematisch bis ins Regal bringt – auf unserem Stack **Asana · Google Drive · n8n · Claude**.

## Schnellstart (für Kolleg:innen)
1. **Claude Code installieren** (Windows, PowerShell): `irm https://claude.ai/install.ps1 | iex` → neues Terminal → `claude --version`.
2. **Repo holen:**
   ```bash
   git clone https://github.com/christiangoldau-creator/meine-webseite.git
   cd meine-webseite
   git checkout claude/supplement-sourcing-github-unk0l9
   claude
   ```
3. In Claude Code die Skill nutzen: **`/sourcing-pipeline <Kongress>`** (z. B. „Wechseljahre", „Ayurveda/Veda360", „Skelett").

## Die Skill: `/sourcing-pipeline`
Liegt in `.claude/skills/sourcing-pipeline/SKILL.md`. Sie spielt für einen Kongress 8 Phasen durch:
0. Kontext laden (Unternehmenswissen Drive + Viktilabs-Katalog Shopify)
1. **Repeated-Claims-Mining** – wiederkehrende Experten-Aussagen aus Mastertabellen **+ Vimeo-Volltext-Transkripten**
2. Recherche (Markt, Wettbewerb, Evidenz, Amazon/Bücher, Regulatorik, Hersteller, Ökonomie)
3. Opportunity-Matrix (gewichtetes Ranking)
4. 5–6 Produktkonzepte **+ adversariale Prüfung** (GO/CAUTION/KILL)
5. Hero-Produkt & Produzierbarkeit (Fabriken, Rohstoffe, Grenzwerte)
6. RFQ + optionale Komplettsimulation
7. Visualisierung (Cockpit/Begehung als Artifact)

## Dokumenten-Landkarte (`supplement-sourcing-zero-to-hero/`)
| Datei | Inhalt |
| --- | --- |
| `README.md` | Projekt-Index |
| `00-situationsanalyse.md` | Markenstruktur, Katalog-Lücke, Pipeline-Architektur |
| `01-analyse-ayurveda-kongress.md` | Konsolidierte Produktinnovations-Analyse + Opportunity-Matrix |
| `02-produktideen.md` | 6 Konzepte mit Scoring + GO/CAUTION/KILL-Prüfung |
| `03-sourcing-pipeline.md` | Stage-Gate „Null bis Shop" (10 Gates, Tracks, Timeline, Kosten) |
| `04-rfq-fabrik-automation.md` | Automatisierte Angebots-Verarbeitung (Gmail→n8n→Claude→Asana) |
| `05-regulatorik-und-compliance.md` | Ampel je Botanical, Novel Food, Schwermetalle, HCVO/HWG, NemV |
| `06-hersteller-eu.md` | Kuratierte EU-Hersteller-Master-Liste + bestehender Stamm + Ökonomie |
| `06b-hersteller-longlist-eu.md` | Vollständige EU-Longlist (100+ Hersteller, ~18 Länder) |
| `07-produzierbarkeit-goldene-milch-churna.md` | Hero-Produkt: Spezifikation, BOM, Grenzwerte, Fabriken |
| `08-rfq-anfrage-goldene-milch-churna.md` | Versandfertige Hersteller-Anfrage (RFQ) |
| `09-simulation-goldene-milch-churna.md` | Komplettsimulation aller Schritte (mit Beispiel-Artefakten) |
| `10-vimeo-transcript-integration.md` | Vimeo-API-Transkripte für Schritt 1 + `tools/vimeo_transcripts.py` |
| `gemini-brief-lohnhersteller.md` | Gemini-Deep-Research-Brief (Hersteller-Suche) |
| `cockpit.html` / `simulation.html` | Visuelle Cockpit-/Begehungs-Artifacts |

## Setup-Bausteine
- **Vimeo-Transkripte (Schritt 1):** Personal Access Token (Scopes `private`, `video_files`) als Umgebungsvariable `VIMEO_ACCESS_TOKEN` – **nie in Chat/Repo**. Skript: `tools/vimeo_transcripts.py`. Details: `10-…md`.
- **RFQ-Automation:** Asana-Projekt „RFQ – Lohnhersteller-Angebote" + n8n-Workflows (Schema/Workflows in `04-…md`).
- **Hersteller-Bestand:** in Google Drive („Adressen Lohnhersteller", 12 Partner) – neue Optionen in `06`/`06b`.

## Verbindliche Leitplanken (für alle Produkte)
1. **Regulatorik ist das erste Gate.** Standardisierte Extrakte vorab auf Novel Food prüfen. **Ashwagandha** unter EU-Verbotsrisiko → nicht hochskalieren.
2. **Keine Heilversprechen.** Für Botanicals faktisch keine erlaubten Health Claims → Positionierung über Tradition/Qualität; Claim-Träger nur Vitamine/Mineralstoffe.
3. **Schwermetall-CoA je Charge = K.-o.-Kriterium** (Ayurveda-Rohware-Risiko, VO (EU) 2023/915).
4. **Ehrlichkeit:** Quellen belegen; simulierte/konstruierte Daten klar kennzeichnen.

## Wichtigste Erkenntnisse (Ayurveda-Beispiel)
- Sortimentslücke: Hero-Wirkstoffe nur als Kapseln; fehlende Botanicals (Triphala, Brahmi, Shatavari …) und Formate (Pulver/Churna, Tee, Öl).
- Größte Chance: „Frauengesundheit/Wechseljahre × Ayurveda × Evidenz" (Shatavari).
- Pilot-Hero: **Goldene-Milch-Churna** (sauberste Rechtslage, niedrigstes MOQ).
- Vertriebs-Burggraben: `Kongress → E-Mail → Shop` (vertraglich verankerte Produktplatzierung).

## Arbeitsteilung lokal vs. Cloud
- **Lokaler Claude Code** (auf dem PC): alles mit Zugriff auf Dateien/Token/Vimeo (Transkripte ziehen).
- **Claude im Web/Cloud:** Strategie, Doku, Analysen am Repo. Beide arbeiten am **selben GitHub-Branch** – gepushte Ergebnisse sind überall sichtbar.

---
*Fragen / Weiterentwicklung der Pipeline-Stufen: einfach `/sourcing-pipeline` starten oder die Dokumente im Projektordner ergänzen und committen.*
