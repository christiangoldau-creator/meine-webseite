---
name: sourcing-pipeline
description: >-
  Spielt die Supplement-Sourcing-Pipeline „von der Kongress-Idee bis zum
  verkaufsfertigen Produkt im Shop" für einen Medumio/Veda360-Kongress durch.
  Nutze diese Skill, wenn der Nutzer aus einem Kongress/Thema neue Viktilabs-
  Supplements ableiten, eine Produktinnovations-Analyse, Opportunity-Matrix,
  Produktkonzepte, Produzierbarkeit (Fabriken/Rohstoffe/Grenzwerte), eine
  Hersteller-Anfrage (RFQ) oder eine vollständige Pipeline-Simulation/
  Visualisierung will. Auslöser u. a.: „Sourcing-Pipeline für <Kongress>",
  „welche Supplemente sollen wir produzieren", „Produktideen aus dem Kongress",
  „Hersteller-Anfrage erstellen", „Pipeline durchspielen/simulieren".
---

# Sourcing-Pipeline: Kongress → Produkt → Shop

Du führst die Produkt-Sourcing-Pipeline für die Firmengruppe **Medumio**
(Kongresse) / **Veda360** (ganzheitlich-ayurvedische Kongressmarke) /
**Viktilabs** (Supplement-Eigenmarke, Shopify Plus, DE/EUR) durch.

**Eingabe:** ein Kongress oder Thema (z. B. „Wechseljahre", „Autoimmun",
„Ayurveda/Veda360", „Skelett/Gelenke"). Optional ein Ziel-Hero-Produkt.

**Ziel:** belastbare, regulatorisch saubere, margenstarke Produktentscheidungen
entlang des einzigartigen Vertriebswegs `Kongress → ActiveCampaign → Shop` —
plus präsentierbare Deliverables für Geschäftsführung und Abteilung.

**Referenz-Implementierung:** der vollständige Ayurveda-Durchlauf liegt in
`supplement-sourcing-zero-to-hero/` (Dokumente `00`–`09` + `cockpit.html` +
`simulation.html`). Nutze ihn als Vorlage für Struktur, Tiefe und Tonalität.

---

## Phasen (jede Phase = ein Deliverable + ein Gate)

### Phase 0 — Kontext laden
- **Unternehmenswissen + Kongress-Pipeline** (Google Drive): `search_files` /
  `read_file_content` (z. B. `pipeline-architektur-skelett.md`, Mastertabellen,
  Supplementboxen, Mailserien).
- **Bestehender Katalog** (Shopify): `search_products` / `search_collections` —
  gezielt nach den relevanten Wirkstoffen/Formaten suchen (nicht alles dumpen;
  große Outputs werden in Dateien gespeichert → mit `jq`/Subagent verarbeiten).
- **Markenstruktur & Vertriebsweg** festhalten (welcher Kongress, welche Audience).
- Deliverable: `00-situationsanalyse.md` (Markenstruktur, Katalog-Lücke).

### Phase 1 — Repeated-Claims-Mining (interne Kongressinhalte)
- Durchsuche die Kongress-Transkripte/Mastertabellen des Zielkongresses in Drive.
- Extrahiere **wiederholt** auftretende Experten-Empfehlungen (Wirkstoff ×
  Häufigkeit), Indikations-Prioritäten, genannte Formate, bestehende
  Produktplatzierungen/Bundles. Belege mit Datei-Titel als Quelle.

### Phase 2 — Recherche (Web + Markt)
Pro Dimension belastbare, **mit Quell-URLs belegte** Befunde:
Markt (DACH/EU, CAGR, Audience-Fit) · Wettbewerb (Marken, Preise, Lücken) ·
Evidenz-Ranking der Botanicals (Evidenz × Audience-Fit) · Amazon-/Buch-Signale
(Nachfrage + Differenzierung) · **Regulatorik** (Novel Food, NemV/AM-Abgrenzung,
Schwermetalle VO 2023/915, HCVO/HWG) · **EU-Lohnhersteller** je Format ·
Format-/Margen-Ökonomie.
- Lade dafür `WebSearch`/`WebFetch` via ToolSearch.
- Bei „gründlich/umfassend/ultracode" oder explizitem Wunsch: **Workflow-Tool**
  für parallele Fan-out-Recherche + adversariale Verifikation nutzen (siehe
  Referenz-Run). Sonst sequenziell mit Subagenten.
- Deliverable: `01-analyse-<kongress>.md` (konsolidierte Analyse + Opportunity-Matrix).

### Phase 3 — Opportunity-Matrix
Bewerte {Botanical/Wirkstoff} × {Format} × {Indikation} gewichtet:
Nachfrage/Fit 25 % · Vertriebsweg 20 % · Regulatorik 20 % · Marge 15 % ·
Wettbewerbslücke 12 % · Evidenz 8 %. Ranke die Top-10. Hebe hervor, was
bestehende Hero-SKUs **ergänzt statt kannibalisiert** (neue Botanicals/Formate).

### Phase 4 — Konzepte + adversariale Prüfung
- Entwickle 5–6 konkrete Konzepte (Mix der Formate, Kombi-/Bundle-Logik),
  je mit Wirkstoffen/Dosis, Positionierung, COGS/VK/Marge, Wettbewerb,
  Regulatorik-Risiko, Vertriebsweg, Kongress-Anker.
- **Prüfe jedes Konzept adversarial** (Regulatory + Commercial, skeptisch):
  Novel Food, Verbots-/AM-Risiko, Schwermetalle, Claim-Falle, Marktsättigung,
  Kannibalisierung → Verdikt **GO / CAUTION / KILL** mit Begründung.
- Deliverable: `02-produktideen.md`.

### Phase 5 — Hero-Produkt & Produzierbarkeit
- Hero-Produkt festlegen (Empfehlung begründen; bei echtem Entscheidungsbedarf
  `AskUserQuestion`, sonst empfohlene Wahl treffen und weiterarbeiten).
- Gesperrte Spezifikation + Rohstoff-BOM + **Grenzwert-/CoA-Anforderungen**
  (Pb/Cd/Hg/As, Pestizide, EtO, Mykotoxine, Mikrobiologie) + passende Fabriken.
- Deliverables: `03-sourcing-pipeline.md`, `05-regulatorik-und-compliance.md`,
  `06-hersteller-eu.md`, `07-produzierbarkeit-<produkt>.md`.

### Phase 6 — RFQ + optionale Simulation
- Versandfertiges Hersteller-Anschreiben + Spezifikations-/Grenzwertblatt
  (`08-rfq-anfrage-<produkt>.md`), zugleich Eingabe-Template für die
  RFQ-Automation (`04-rfq-fabrik-automation.md`: Gmail→n8n→Claude→Asana).
- Auf Wunsch: **Komplettsimulation** aller Schritte mit konstruierten Beispielen
  (Fabrik-Antworten, Vergleich, Bemusterung, Etikett, Launch) →
  `09-simulation-<produkt>.md`. **Simulierte Werte immer klar als solche markieren.**

### Phase 7 — Visualisierung
- Präsentationsreifes, selbst-enthaltenes Artifact (HTML) für Geschäftsführung/
  Abteilung: Pipeline-Cockpit (Status) und/oder visuelle Begehung der Simulation.
  Lade vorab die Skill `artifact-design`. Halte die Projekt-Designidentität bei
  (warmes Grün/Kurkuma, Serif-Display, Mono für Daten) für Konsistenz.

---

## Verbindliche Leitplanken (gelten in jeder Phase)

1. **Regulatorik ist das wichtigste Frühgate.** Standardisierte Extrakte vorab
   auf Novel Food prüfen. **Ashwagandha** steht unter EU-Verbotsrisiko
   (Art.-8-Verfahren, DK-Verbot, BfR 039/2024) → nicht als neue Säule aufbauen.
2. **Keine Heilversprechen.** Für Botanicals gibt es faktisch keine erlaubten
   Health Claims (EuGH C-386/23) → Positionierung über Tradition/Qualität;
   Claim-Träger sind nur Vitamine/Mineralstoffe mit zugelassenen Claims.
3. **Schwermetall-CoA je Charge** ist K.-o.-Kriterium (Ayurveda-Rohware ist
   dokumentiert hoch belastet; VO (EU) 2023/915).
4. **Ehrlichkeit:** Recherche mit Quellen belegen; simulierte/konstruierte Daten
   immer eindeutig kennzeichnen; Marktzahlen als Richtwerte ausweisen.
5. **Auf dem vorhandenen Stack aufsetzen:** Asana = Single Source of Truth,
   Google Drive = Storage, n8n = Orchestrator, Claude API = Engine.
6. **Format-Logik:** Kapsel = Margen-/Skalen-Rückgrat; Pulver/Churna =
   Differenzierung bei niedrigem MOQ; Tee = Bundle/Einstieg; Softgels meiden
   (MOQ-Killer); Öl/Tinktur nur selektiv.

## Output & Abschluss
- Alle Deliverables als nummerierte Markdown-Dokumente in einem Projektordner
  ablegen (Schema wie `supplement-sourcing-zero-to-hero/`), README als Index.
- Änderungen committen und auf den Arbeits-Branch pushen; bei neuem Branch
  Draft-PR anlegen.
- Am Ende: knappe Zusammenfassung der Entscheidungen + Artifact-Links + nächste
  Schritte. Keine internen Modell-/Tool-Details in Repo-Artefakten.
