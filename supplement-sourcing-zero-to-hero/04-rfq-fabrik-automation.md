# 04 – Automatisierte Verarbeitung von Fabrik-Angeboten (RFQ-Management)

> Wie eingehende Lohnhersteller-Angebote automatisch erfasst, strukturiert, verglichen und mit Rückfragen versehen werden – auf dem vorhandenen Stack. Stand: 2026-06-27.

**Stack:** Gmail → n8n → Claude API → Asana + Google Drive (+ Slack).
**Rollen:** Asana = Single Source of Truth · Google Drive = Storage · n8n = Orchestrator · Claude API = Extraktions-/Veredelungs-Engine.

Dieses Dokument beantwortet deine konkrete Frage: *„Angebote von Fabriken müssen automatisiert verarbeitet werden, wenn sie reinkommen. Es müssen Nachfragen gestellt werden, produktbare Daten eingeflickt werden."* Die Lösung sind vier n8n-Workflows (Versand, Erfassung, Vergleich, Rückfrage) um ein einheitliches Daten-Schema.

> **⚠️ Ayurveda-spezifisches K.-o.-Kriterium (verbindlich):** Bei den Ziel-Wirkstoffen (Triphala, Brahmi, Shatavari, Tulsi, Amla, Boswellia, Moringa …) ist die Schadstoff-/Schwermetall-Prüfung **kein optionaler Punkt, sondern Auto-Disqualifikation**. Studien fanden in ~60 % ayurvedischer Proben toxische Schwermetalle (Arsen-Überschreitungen bis zum 49.000-fachen, dokumentierte Bleivergiftung Köln 2022). EU-Höchstgehalte nach VO (EU) 2023/915 für NEM: Blei ≤ 1,0 · Cadmium ≤ 1,0 · Quecksilber ≤ 0,1 mg/kg. Die Automatisierung prüft CoA-Werte **hart** gegen diese Grenzwerte.

---

## 1. Einheitliches Daten-Schema (RFQ-/Angebots-JSON)

Kanonisches Format, das n8n nach Asana (Custom Fields + Attachment), Drive (Roh + JSON) und Slack schreibt. Felder mappen 1:1 auf Asana-Custom-Fields.

```json
{
  "rfq": {
    "rfq_id": "RFQ-2026-0007",
    "produkt_arbeitstitel": "Triphala Churna 500g",
    "wirkstoff": "Triphala (Amalaki/Bibhitaki/Haritaki 1:1:1)",
    "ziel_format": "Pulver/Churna",
    "ziel_dosis_pro_einheit": "5 g/Tagesportion",
    "standardisierung": "min. 40% Tannine, definiertes Fruchtsäure-Profil",
    "ziel_moq": 2500,
    "zielpreis_pro_einheit_eur": 4.50,
    "zieltermin_lieferung": "2026-09-15",
    "geforderte_zertifikate": ["GMP", "ISO 22000/HACCP", "Bio (EG-Öko/DE-ÖKO)"],
    "geforderte_coa": ["Schwermetalle (Pb/Cd/Hg/As)", "Mikrobiologie", "Pestizide", "Identität/Wirkstoffgehalt"],
    "versendet_an": ["hersteller_a@...", "hersteller_b@..."]
  },
  "angebot": {
    "angebots_id": "OFF-2026-0007-B",
    "rfq_id": "RFQ-2026-0007",
    "hersteller_name": "Beispiel Pharma GmbH",
    "eingangsdatum": "2026-07-02",
    "drive_ordner_url": "https://drive.google.com/...",
    "preis": {
      "preis_pro_einheit_eur": 4.85,
      "preisbasis": "pro 500g Dose",
      "staffelpreise": [
        {"menge": 2500, "preis_eur": 5.20},
        {"menge": 5000, "preis_eur": 4.85},
        {"menge": 10000, "preis_eur": 4.40}
      ],
      "einmalkosten_setup_eur": 850,
      "zahlungsziel": "30 Tage netto",
      "preis_gueltig_bis": "2026-08-31"
    },
    "moq": 2500,
    "lieferzeit_wochen": 8,
    "format": "Pulver/Churna",
    "rezeptur": {
      "wirkstoff_bestaetigt": true,
      "standardisierung_bestaetigt": "40% Tannine bestätigt",
      "fuellstoffe_zusatzstoffe": ["keine"],
      "herkunft_rohstoff": "Indien, eigene Lieferkette"
    },
    "zertifikate": { "GMP": true, "ISO_HACCP": true, "Bio": false, "weitere": ["IFS Food"] },
    "coa": {
      "vorhanden": true,
      "schwermetalle": { "blei_mg_kg": 0.4, "cadmium_mg_kg": 0.3, "quecksilber_mg_kg": 0.02, "arsen_mg_kg": 0.1, "konform_eu_2023_915": true },
      "mikrobiologie_bestanden": true,
      "pestizide_bestanden": true
    },
    "offene_punkte": ["Bio-Zertifikat fehlt", "Staffelpreis >10k nicht genannt"],
    "vollstaendigkeit_prozent": 85,
    "score_gesamt": 78.5,
    "status": "Angebot vollständig",
    "extraktions_konfidenz": 0.92,
    "claude_zusammenfassung": "Wettbewerbsfähiger Preis, GMP+IFS vorhanden, Schwermetalle konform. Bio fehlt — Nachfrage nötig."
  }
}
```

**Pflicht-vs-Optional-Logik:** Fehlt eines von `{preis_pro_einheit_eur, moq, lieferzeit_wochen, coa.schwermetalle, zertifikate.GMP}` → `status = "Daten unvollständig"` → triggert automatische Rückfrage (Workflow D). `vollstaendigkeit_prozent` = Anteil befüllter Pflichtfelder.

---

## 2. Die vier n8n-Workflows

### Workflow A — RFQ-Versand (standardisiert, multi-Hersteller)
```
[Asana Trigger: Task in Sektion "RFQ versenden bereit"]
   ▼ [Function: RFQ-JSON aus Asana Custom Fields bauen]
   ▼ [Claude API: formales, HCVO-konformes RFQ-Schreiben (DE) generieren]
   ▼ [Drive: RFQ-PDF/Spezifikationsblatt ablegen → /RFQs/RFQ-2026-0007/]
   ▼ [Loop über Hersteller] ─► [Gmail Send] personalisierte RFQ-Mail + PDF
         Betreff: "[RFQ-2026-0007] Anfrage Triphala Churna – Viktilabs"
   ▼ [Asana: Status "RFQ versendet" + Subtask je Hersteller "Angebot ausstehend"]
```
**Schlüssel:** Die `[RFQ-ID]` im Betreff ist der **Korrelationsschlüssel**, über den Workflow B eingehende Antworten dem richtigen Asana-Task zuordnet (Regex auf Subject/References-Header).

### Workflow B — Angebots-Erfassung (eingehend) — *das Herzstück*
```
[Gmail Trigger: Label "RFQ-Inbox" ODER Betreff enthält "RFQ-"]
   ▼ [Switch: Anhang?] ─ ja → [Drive speichern] + [Extract from File: PDF/Excel/Word → Text]
   ▼ [Merge: Mail-Body + Anhangstext]
   ▼ [Claude API: Extraktions-Prompt → striktes JSON]   (Sonnet Default; Opus bei komplexem CoA)
   ▼ [Function: Schema validieren, Preis/Datum normalisieren (EUR/ISO),
                Schwermetalle gegen VO 2023/915 prüfen]
   ▼ [Switch: Schwermetalle konform?]
        ├─ nein → [Asana: "Disqualifiziert (Schadstoff)"] + [Slack 🚨]
        └─ ja ▼ [Switch: vollständig < 100 %?] ─ ja → Workflow D
   ▼ [Asana: Task per RFQ-ID finden/aktualisieren, Custom Fields füllen,
              JSON als Attachment, Drive-Link, claude_zusammenfassung als Kommentar]
   ▼ [Slack: "Neues Angebot von <Hersteller>: 4,85€/Einheit, Score vorläufig"]
```
Dies ist das „produktbare Daten einflicken": Claude liest die unstrukturierte Hersteller-Mail + CoA-PDF und schreibt **strukturierte, vergleichbare Felder** direkt in Asana.

### Workflow C — Angebots-Vergleich & Scoring
```
[Trigger: alle Angebote einer RFQ = "Angebot vollständig" ODER manuell/Cron-Deadline]
   ▼ [Asana: alle Angebote zu RFQ-ID sammeln]
   ▼ [Function: gewichtetes Scoring (Abschnitt 3), auf vergleichbare Zielmenge normalisiert]
   ▼ [Claude API: Vergleichstabelle (Markdown) + Empfehlung + Risiken]
   ▼ [Drive: Vergleichstabelle ablegen]
   ▼ [Asana: Task "ENTSCHEIDUNG: Hersteller wählen" → Einkauf, Status "Wartet auf Freigabe"]
   ▼ [Slack: Vergleich posten + @Verantwortliche]   ← HUMAN-IN-THE-LOOP
```

### Workflow D — Rückfragen-Generierung
```
[Trigger: Status "Daten unvollständig"]
   ▼ [Claude API: Nachfass-Mail entwerfen — nur die offenen Punkte, höflich, DE]
   ▼ [Gmail: create_draft]   ← NICHT auto-send (Freigabe durch Mensch)
   ▼ [Asana: Status "Rückfrage offen", Draft-Link, Fälligkeit +3 Tage]
   ▼ [Slack: "Rückfrage-Entwurf bereit zur Freigabe"]
```

> Bewährte Referenz-Templates auf demselben Stack existieren bereits: n8n „Extract & log Gmail invoices with Claude Sonnet", „Email invoice archiving & extraction (Gmail/Drive/AI)", „Email classification with Gmail & Claude" – exakt das Muster Gmail-Trigger → Anhang-Extraktion → Claude-JSON → Normalisierung → Drive/Asana + Slack.

---

## 3. Scoring-Modell (gewichtete Matrix)

| Kriterium | Gewicht | Bewertung (0–100) |
| --- | :--: | --- |
| **Preis/Einheit** (normalisiert) | 35 % | `100 × (min_preis / preis_angebot)` |
| **Schadstoff/CoA-Konformität** | 20 % | konform = 100; näher am Grenzwert → niedriger; CoA fehlt = 0 (+ Disqualifikation) |
| **Zertifikate** (GMP/ISO/Bio) | 15 % | anteilig je gefordertem Zertifikat; GMP fehlt = max. 40 |
| **Lieferzeit** | 12 % | `100 × (min_lieferzeit / lieferzeit_angebot)` |
| **MOQ-Passung** | 10 % | MOQ ≤ Ziel = 100; sonst linear abwertend |
| **Rezeptur/Standardisierung** | 8 % | exakt bestätigt = 100 |

`score_gesamt = Σ(score × gewicht)`, Skala 0–100.
**Wichtig:** nicht naiv Stückpreise vergleichen, wenn MOQ/Staffeln/Zahlungsziel abweichen → auf *vergleichbarer Zielmenge* rechnen (Staffelpreis interpolieren) und Setup-Einmalkosten berücksichtigen. „Quoted Lead Time ≠ Reliability" → Asana-History-Feld „Liefertreue Vergangenheit" fließt in Folge-RFQs ein.

---

## 4. Claude-Extraktions-Prompt (Skelett)

```
SYSTEM:
Du bist Extraktions-Engine für Lohnhersteller-Angebote (Nahrungsergänzungsmittel, DE).
Gib AUSSCHLIESSLICH valides JSON nach dem Schema zurück. Keine Prosa. Erfinde nichts:
Fehlt ein Wert → null + Eintrag in "offene_punkte". Preise in EUR (Fremdwährung NICHT
umrechnen, kennzeichnen), Daten als ISO-8601, Schwermetalle numerisch in mg/kg.

USER:
== RFQ-SPEZIFIKATION (Soll) ==      {rfq_json}
== EINGEGANGENE HERSTELLER-MAIL ==  {mail_body}
== ANHÄNGE (CoA / Angebot, Text) == {attachment_text}

== AUFGABE ==
1) Extrahiere alle Felder gemäß "angebot"-Schema.
2) Gleiche Ist gegen Soll ab (rezeptur.*_bestaetigt, MOQ ≤ ziel_moq, Preis vs zielpreis).
3) Prüfe coa.schwermetalle gegen EU 2023/915 (Pb ≤1,0 / Cd ≤1,0 / Hg ≤0,1 mg/kg)
   → konform_eu_2023_915 (true/false/null).
4) Liste fehlende Pflichtwerte in "offene_punkte", berechne "vollstaendigkeit_prozent".
5) "claude_zusammenfassung": max. 3 Sätze, sachlich, KEINE Heilversprechen.
6) "extraktions_konfidenz": 0–1.

Antworte NUR mit dem JSON-Objekt.
```
Implementierung: striktes JSON über Structured-Output/`tool_use` erzwingen; RFQ-Spezifikation per Prompt-Caching; Sonnet als Default, Opus nur bei `extraktions_konfidenz < 0,8` als Re-Run (Kostenkontrolle).

---

## 5. Asana-Struktur

**Portfolio:** „Viktilabs Sourcing" · **Projekt:** „RFQ – Lohnhersteller-Angebote" (Board). Ein Task pro RFQ (Produkt), je Angebot ein verlinkter Task/Subtask (Feld „RFQ-ID").

**Status-Lifecycle (Board-Spalten):**
`1 Spezifikation in Arbeit → 2 RFQ versenden bereit (▶A) → 3 RFQ versendet → 4 Angebot eingegangen (▶B) → 5 Daten unvollständig/Rückfrage offen (▶D) → 6 Angebot vollständig → 7 Im Vergleich (▶C) → 8 Wartet auf Freigabe (HITL) → 9 Hersteller gewählt → 10 Disqualifiziert → 11 Archiviert`

**Custom Fields (Auszug):** RFQ-ID (text) · Hersteller (text) · Format (enum) · Preis/Einheit EUR (number) · MOQ (number) · Lieferzeit Wo (number) · GMP/Bio (enum) · CoA Schwermetalle (enum: konform/grenzwertig/nicht konform/fehlt) · **Blei mg/kg (number, hartes K.-o.-Feld)** · Vollständigkeit % (number) · Score (number) · Konfidenz Extraktion (number, <0,8 → manuelle Sichtung) · Drive-Ordner (URL).

**Human-in-the-loop-Gates & Eskalation:**
- **Gate 1 – Rückfragen:** Claude schreibt nur Gmail-*Draft*, kein Auto-Versand.
- **Gate 2 – Schadstoff-Disqualifikation:** Automatik markiert + Slack-Alert; finale Verwerfung bestätigt der Einkauf (kein stilles Löschen).
- **Gate 3 – Lieferanten-Entscheidung:** Workflow C erstellt nur eine Entscheidungs-Task mit Empfehlung; **die Wahl trifft ein Mensch.**
- **Eskalation (n8n-Cron, täglich):** (a) „RFQ versendet" ohne Antwort > Frist → Erinnerungs-Draft; (b) „Rückfrage offen" > 3 Tage → Eskalation; (c) „Wartet auf Freigabe" > 5 Tage → Slack-Reminder.
- **Konfidenz-Gate:** `extraktions_konfidenz < 0,8` → Flag „Manuelle Prüfung".

---

## Aufwand & nächste Schritte

- **Bau-Aufwand** (analog zur bestehenden Content-Pipeline): Workflow B ist der komplexeste (~10–14 h), A/C/D je ~4–8 h. Realistisch 1 Person, 2–3 Wochen netto inkl. Prompt-Iteration.
- **Voraussetzungen:** Gmail-Label/Filter „RFQ-Inbox", Asana-Projekt + Custom Fields, Claude-API-Credential, Drive-Ordnerstruktur `/RFQs/`.
- **Error-Handling** wie im Haus-Standard: 3 Retries mit Backoff, bei Final-Failure Slack-Alert + Asana-Comment, Status bleibt „stuck-sichtbar".

**Quellen:** EU VO 2023/915 (Schwermetall-Höchstgehalte, Eurofins/BMUKN) · Verbraucherzentrale & LAVES (Schwermetalle in ayurvedischen NEM) · AuraVMS/LightSource/Tranquil (RFQ-Scoring-Best-Practice) · cmdirectory (Nutraceutical-RFQ-Template) · n8n-Workflow-Bibliothek (Gmail+Claude+Drive+Slack) · Asana Developer Docs (Custom Fields).
