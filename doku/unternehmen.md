# VeloWerk Zürich AG – Unternehmensbeschreibung und Prozessgrundlage

> Fiktives Lehrbeispiel. Diese Datei ist die Referenz für Prozessbeschreibung und BPMN-Modell.
> Quelle: `KK6-4_VeloWerkZuerich_Unternehmensbeschreibung.pdf`
> Abschnitte mit „offen“ sind im Quelldokument nicht festgelegt und müssen von der Gruppe ergänzt werden.

## Gruppe

- **Gruppennummer:** KK6-4
- **Mitglieder:** Andi Kadolli, Adi Lama, Valdrin Pachuku, Skender Zenullahu
- **Präsentation Unternehmensbeschreibung:** 1. Oktober 2026

## Steckbrief

| Feld | Angabe |
|---|---|
| Name | VeloWerk Zürich AG |
| Kurzname für Dateinamen | VeloWerkZuerich |
| Branche | E-Bike-Verkauf, Werkstattservice und Vermietung |
| Rechtsform | AG |
| Sitz / Standort | Raum Zürich (lokaler Anbieter) |
| Real oder fiktiv | Fiktiv |
| Mitarbeitende | offen |

## Kurzbeschreibung

VeloWerk Zürich verbindet Verkauf, Werkstatt und Vermietung von E-Bikes. Beratung und Reklamationsbearbeitung sichern passende E-Bike-Mobilität über die gesamte Nutzungsdauer.

## Leistungswege und Angebot

Lokaler E-Bike-Anbieter im Raum Zürich mit drei Leistungswegen:

- **Verkauf:** E-Bikes verkaufen und übergeben
- **Werkstattservice:** Reparaturen und Wartungen
- **Vermietung:** E-Bikes vermieten und zurücknehmen

Die **Garantie- und Reklamationsbearbeitung** greift bei Bedarf ergänzend ein.

## Positionierung

VeloWerk begleitet Auswahl, Nutzung und Werterhalt. Persönliche Beratung und Werkstattservice verbinden einmalige Leistungen mit einer längerfristigen Kundenbeziehung.

## Kundschaft

- Privatkundschaft
- Berufspendlerinnen und Berufspendler
- Unternehmen und Organisationen
- Touristinnen und Touristen

## Geschäftsmodell

- Marge aus dem E-Bike-Verkauf
- Entgelte für Reparatur und Wartung
- Mietgebühren für E-Bikes

## Unternehmensziel

Zuverlässige und unkomplizierte E-Bike-Mobilität durch persönliche Beratung sowie einen transparenten und verlässlichen Werkstattservice.

## Strategischer Fokus

| Nr. | Fokus | Inhalt |
|---|---|---|
| 01 | Kundenbeziehung | Beratung und Service begleiten die gesamte Nutzungsdauer |
| 02 | Werkstattqualität | Reparaturen planbar und verlässlich abwickeln |
| 03 | Transparente Kommunikation | Termine, Kosten und Status nachvollziehbar machen |
| 04 | Nachhaltige Nutzung | Nutzungsdauer der E-Bikes durch Wartung verlängern |

## Prozesslogik

- **Managementprozesse** geben Richtung und Qualitätsrahmen vor.
- **Kernprozesse** erzeugen den Kundennutzen.
- **Supportprozesse** sichern Personal, Material, Daten und Infrastruktur.

## Prozesslandkarte

> Stand Landkarte: 08.10.2026. Nur Prozesse, die in der K4-Dokumentation genannt sind; übrige ergänzen.

### Managementprozesse

- M2 Finanzsteuerung
- M3 Qualität und Nachhaltigkeit steuern
- offen: weitere M-Prozesse

### Kernprozesse

- K1 Anliegen klären und Kundschaft beraten
- K2 Warenversorgung und Warenverfügbarkeit sicherstellen
- K3 offen
- **K4 Reparatur- und Serviceaufträge abwickeln** (gewählter Kernprozess)
  - K4.1 Auftrag und Leistungsumfang klären
  - K4.2 Wartung / Reparatur planen und durchführen
  - K4.3 Ergebnis prüfen und E-Bike zurückgeben
- K5 E-Bike-Vermietungen und Rücknahmen abwickeln
- K6 Garantie- und Reklamationsfälle bearbeiten

### Supportprozesse

- S4 Buchhaltung und Zahlungsverkehr abwickeln
- offen: weitere S-Prozesse (laut Prozesslogik: Personal, Material, Daten, Infrastruktur)

## Organisation

### Rollen in K4

> Laut AN1 fachliche Rollen und Modellierungsannahmen; eine Person kann mehrere Rollen übernehmen.

| Rolle | Verantwortung in K4 |
|---|---|
| Serviceannahme | Anliegen und Übergabe erfassen, Kosten und Terminrahmen abstimmen, Kundenentscheide dokumentieren, Rückgabe koordinieren, Leistungsdaten übermitteln |
| Werkstatt | Diagnose und technischen Umfang klären, Teilebedarf abstimmen, freigegebenen Umfang bearbeiten, prüfen und ggf. nacharbeiten |

### Prozessbeteiligte ausserhalb von K4

> Im Modell abgegrenzt, interne Abläufe nicht modelliert; Kommunikation über Nachrichtenflüsse.

| Beteiligte | Beziehung zu K4 |
|---|---|
| Kundschaft | Stellt Werkstattanfrage, entscheidet über Vorschläge, Lieferoptionen und Zusatzarbeiten, holt E-Bike ab |
| K2 Warenversorgung | Erhält Teilebedarf, meldet Status und Bereitstellung (M04, M05, M08), erhält Restteilemeldung bei Abbruch (M15) |
| S4 Buchhaltung | Erhält Leistungsdaten (M12, M14), übernimmt Rechnung und Zahlung |

## Systeme und Hilfsmittel

Bewusst nicht festgelegt: Die Dokumentation behauptet weder ein vorhandenes IT-System noch einen beobachteten Medienbruch; eine durchgängige Auftragsreferenz ist nur Gestaltungsempfehlung.

## Gewählter Kernprozess

- **Name:** K4 Reparatur- und Serviceaufträge abwickeln
- **Kurzname für Dateinamen:** ReparaturService
- **Fachlicher Stand:** K4-A-3.0, Abgabestand 03.11.2026 (= Fassung v1 für Aufgabe B)
- **Start:** E01 Werkstattanfrage der Kundschaft nach Anliegenklärung in K1
- **Ende:** E11 Auftrag vollständig erfüllt und geschlossen / E13 Auftrag ohne vollständige Leistung abgeschlossen
- **Abgrenzung:** einzelner externer Kundenauftrag; Terminbuchung vor der Anfrage, interne K5-Aufträge und spätere Reklamationen (K6) nicht detailliert
- **Begründung der Wahl:** unmittelbarer Kundennutzen, mehrere Rollen, relevante Entscheidungen (technische Machbarkeit, Freigaben, Teileversorgung, Zusatzbefunde, Nacharbeit)

## Annahmen

Modellierungsannahmen AN1–AN7 sind in der Prozessdokumentation K4 festgehalten (Rollen, Freigaben, Fristen, Teile, Zusatz und Rückgabe, Nacharbeit, Ergebnisübergänge). Änderungen an Annahmen dort pflegen.
