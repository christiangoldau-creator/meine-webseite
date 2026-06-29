# Produkt-Detailseite (PDP) im Viktilabs-Shop-Stil

Aufbau nach echter Viktilabs-Produktseite. Tonalität **„Du"**, warm-empowernd. Erst die paste-fertige
Copy als Repo-Doc schreiben (`13-…`, `14-…` als Vorlage), dann optional als **Artifact** rendern.

## Sektions-Reihenfolge (verbindlich)

1. **HERO / Buy-Box** — Titel (Produktname), Untertitel, Preis (+ ggf. Streichpreis/Staffel), Mengen-Varianten, „Auf Lager – in 2–3 Tagen", Badges: ⭐ 4,8 bei über 1 Mio. Kund:innen · Versand ab 49 € · 90-Tage-Geld-zurück · Klimafreundlicher Versand · Laborgeprüft & in DE entwickelt.
2. **Gut zu wissen** — 5 USP-Bullets (kurz, konkret, kein Heilversprechen).
3. **Inhaltsstoffe & Nährwerte** — Tabelle pro Tagesportion (+ NRV wo vorhanden), volle Zutatenliste, „Bio/vegan/glutenfrei".
4. **Verzehr & Hinweise** — 4 Karten: Einnahme · Dosierung · Unverträglichkeiten · Empfehlungen. + Pflichtsatz „kein Ersatz für ausgewogene Ernährung; außerhalb der Reichweite von Kindern; Tagesdosis nicht überschreiten".
5. **Wirkung & Studien** — Disclaimer (s. Claim-Regel) + Verweis auf Kongress/Forschung.
6. **Laboranalysen & Zertifizierungen** — Regelmäßige Analysen · HACCP · Transparenz (Laborberichte) · Bio (DE-ÖKO-Nr.).
7. **Besonders gut in Kombination mit** — Cross-Sell/Bundle.
8. **Unsere Mission: Gesundheit neu denken** — gegründet 2020 (Leon Benedens · Paul Seelhorst · Christian Goldau), eigenfinanziert.
9. **Nur das Beste für dich** — Qualitäts-Grid (ohne Füllstoffe/Magnesiumstearat/Titandioxid/künstl. Süßstoffe; gentechnikfrei; auf Schwermetalle & Mikrobiologie getestet …).
10. **Deine Gesundheit. Deine Entscheidung.** — Vergleichstabelle Viktilabs vs. Andere.
11. **FAQ** — 6–8 Fragen (Einnahme, Form, vegan, Kombination, Lagerung, Reichweite …).

## Claim-Regel (Compliance) — wichtig

- Vermarktung über **Aufklärung** (Kongress/Mail), **nicht** über Produkt-Claims.
- Auf Produkt/Seite nur **zugelassene** gesundheitsbezogene Angaben — praktisch v. a. **Magnesium** (Nerven/Muskeln/Müdigkeit, VO 1924/2006). Diesen Claim ruhig nutzen, das ist der legale Träger.
- **Pflanzliche Bestandteile (Shatavari, Brahmi, Kurkuma …):** keine Wirkangaben. Stattdessen Viktilabs-Standardsatz: „Aufgrund gesetzlicher Vorgaben dürfen wir dir keine detaillierten Angaben zur Wirkung machen — informier dich selbst" + Verweis auf den Kongress + unabhängige Forschung.
- **Niemals** Heilversprechen / krankheitsbezogene Aussagen (HWG/HCVO). Vor Live-Gang HWG/HCVO-Check + § 5 NemV-Anzeige.

## Wiederkehrende Markenphrasen
„Gesundheit neu denken" · „Deine Gesundheit. Deine Entscheidung." · „individuelle Balance aus Vitalität und Wohlbefinden" · „Nahrungsergänzung, der du wirklich vertrauen kannst" · „Laborgeprüft und in Deutschland entwickelt" · „maximale Transparenz".

## Als Artifact rendern
- HTML mit eigenem `<style>` (kein Webfont-CDN — System-Sans-Stack), warmweißer Grund, Near-Black-Typo, **Goldakzent** für Linien/Preis, je Produkt passende Akzent-Farbwelt (z. B. Plum für Abend, Gold für Morgen).
- Produktbild als `data:`-URI: vorher auf ~760 px verkleinern (JPEG q84) → in `<img src="__HERO__">` mit `scripts/inject_image.py` einsetzen (NIE PowerShell).
- Layout: zweispaltiger Hero (Bild | Buy-Box), darunter gestapelte Sektionen; responsive (eine Spalte mobil); Tabellen in `overflow-x:auto`; FAQ als `<details>`.
- Favicon passend (z. B. ☀️ Morgen, 🌙 Abend). Footer-Hinweis: „Mockup-Bild KI-generiert, Etikett-Typografie für den Druck nachzusetzen."
