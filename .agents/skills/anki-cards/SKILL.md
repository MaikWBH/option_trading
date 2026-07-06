---
name: anki-cards
description: Generate well-structured Anki flashcards from any topic or document, with Mermaid diagrams for visual concepts. Use this skill whenever the user wants to create flashcards, learning cards, Anki decks, study cards, spaced repetition content, or wants to memorize concepts like option Greeks, trading strategies, payoff diagrams, or any other subject matter. Trigger on phrases like "erstelle Anki Karten", "create flashcards", "make study cards", "build a deck for", "help me memorize", or whenever the user shares a document and asks to learn from it. Always use this skill when visual/diagram-based cards would help understanding.
---

# Anki Card Creator

Du erstellst hochwertige Anki-Karten, die auf wissenschaftlichen Lernmethoden basieren: Feynman-Technik, Active Recall, Spaced Repetition und Chunking. Die Karten sollen Verständnis fördern, nicht blindes Auswendiglernen.

## Schritt 1: Kontext klären

Bevor du Karten erstellst, kläre kurz:
- **Thema & Tiefe**: Was soll gelernt werden? Einsteiger oder Fortgeschrittene?
- **Vorwissen**: Was weiß der Nutzer bereits?
- **Sprache**: Deutsch, Englisch oder gemischt?
- **Kartentyp-Präferenz**: Nur Basic, oder auch Cloze-Deletion und Diagramm-Karten?

Wenn der Nutzer ein Dokument mitschickt, extrahiere daraus die wichtigsten lernbaren Konzepte und schlage vor, welche davon als Karten sinnvoll sind. Frage aber nur dann nach, wenn Kontext wirklich fehlt — im Zweifel fang einfach an.

---

## Schritt 2: Karten entwerfen

### Grundprinzipien guter Anki-Karten

**Atomarität**: Eine Karte = eine Idee. Statt „Erkläre alle Greeks" → fünf separate Karten für Delta, Gamma, Theta, Vega, Rho.

**Verstehen statt auswendig lernen**: Fragen sollten Konzeptverständnis prüfen, nicht nur Definitionen abrufen. 

Schlechte Karte:
> F: Was ist Delta?  
> A: Die Sensitivität des Optionspreises gegenüber dem Kursänderung des Basiswerts.

Bessere Karte:
> F: Eine Aktie steigt um $1. Die Call-Option hat Delta = 0.6. Wie ändert sich der Optionspreis näherungsweise?  
> A: Der Optionspreis steigt um ca. $0.60. Delta misst diese Änderungsrate — deshalb ist es nützlich als "Aktienäquivalent" der Option zu denken.

**Kontextueller Anker**: Wo sinnvoll, gib der Frage einen kurzen Rahmen (z.B. eine Handelssituation), damit der Lernende die Information einordnen kann.

**Memory Hook**: Ergänze die Rückseite mit einer Eselsbrücke, Analogie oder einem Beispiel, wo es das Lernen erleichtert.

---

### Kartentypen

#### Basic (Standard)
Vorderseite: Frage oder Konzept  
Rückseite: Antwort + optionale Eselsbrücke/Beispiel

```
Vorderseite:
Was bedeutet es wenn eine Call-Option "In-the-Money" (ITM) ist?

Rückseite:
Der aktuelle Aktienkurs liegt **über** dem Strike-Preis der Option.

Beispiel: Aktie bei $65, Strike bei $60 → Option ist $5 ITM (hat $5 inneren Wert).

Eselsbrücke: "Im Geld" = du könntest die Option jetzt profitabel ausüben.
```

#### Cloze Deletion
Für Definitionen und Formeln, bei denen das Ergänzen eines Begriffs das Lernen verankert.

```
Der {{c1::Zeitwert}} (Extrinsic Value) einer Option nimmt mit {{c2::näherndem Verfallsdatum}} 
ab — dieser Effekt wird als {{c3::Theta-Zerfall}} bezeichnet.
```

#### Diagramm-Karten (Mermaid)
Für visuelle Konzepte: Payoff-Profile, Entscheidungsbäume, Beziehungsdiagramme.

Mermaid-Code auf der Rückseite einbetten (siehe Abschnitt "Mermaid-Diagramme in Anki" unten).

---

## Schritt 3: Ausgabeformat

Gib die Karten in **zwei Formaten** aus:

### Format 1: Lesbares Markdown (zur Vorschau & Diskussion)

Zeige die Karten übersichtlich mit Vorderseite / Rückseite / Diagramm, damit der Nutzer sie sofort bewerten kann.

### Format 2: Anki-Import-Datei (TSV)

```
#separator:tab
#html:true
#notetype:Basic
Vorderseite (HTML)	Rückseite (HTML)
```

Für Cloze-Karten:
```
#separator:tab  
#html:true
#notetype:Cloze
Text mit {{c1::...}} Lücken	Optionales Zusatzmaterial
```

HTML-Formatierung nutzen für:
- `<b>Fettschrift</b>` für Schlüsselbegriffe
- `<br>` für Zeilenumbrüche
- `<ul><li>...</li></ul>` für Listen

---

## Mermaid-Diagramme in Anki

Anki unterstützt HTML in Karten. Mermaid-Diagramme kannst du auf zwei Wegen einbetten:

### Weg A: Mermaid.js via CDN (empfohlen für Anki Desktop/Web)

Füge in die Kartenvorlage (Card Template) einmalig ein:
```html
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true});</script>
```

Dann in der Karte:
```html
<div class="mermaid">
flowchart LR
    A[Delta] -->|steigt wenn| B[Option tiefer ITM]
    A -->|sinkt wenn| C[Option tiefer OTM]
</div>
```

### Weg B: Statisches SVG (funktioniert überall, kein Internet nötig)

Generiere SVG aus Mermaid mit dem CLI-Tool `mmdc`:
```bash
mmdc -i diagram.mmd -o diagram.svg
```

Dann SVG-Inhalt direkt in die Karte einbetten (als `<img src="...">` oder inline `<svg>...`).

### Erzeuge Mermaid-Karten so

Im Markdown-Format zeige das Diagramm gerendert. Im TSV-Format schreibe den HTML-Block mit `<div class="mermaid">...</div>`.

---

## Welche Diagramme wann?

| Konzept | Diagramm-Typ | Mermaid-Typ |
|---|---|---|
| Greeks-Beziehungen | Abhängigkeitsgraph | `flowchart` |
| Strategie-Auswahl | Entscheidungsbaum | `flowchart TD` |
| Payoff-Profile | Liniendiagramm | `xychart-beta` |
| Zeitverlauf / Prozesse | Sequenz | `sequenceDiagram` |
| Vergleiche (Covered Call vs. Naked Call) | Tabelle + flowchart | `flowchart LR` |

---

## Schritt 4: Deck-Struktur vorschlagen

Strukturiere Karten in logische Decks (Hierarchie mit `::` in Anki):

```
Optionen::Grundlagen::Call & Put
Optionen::Grundlagen::Strike & Prämie
Optionen::Griechen::Delta
Optionen::Griechen::Theta
Optionen::Strategien::Covered Call
Optionen::Strategien::Cash-Secured Put
Optionen::Strategien::Iron Condor
Optionen::Risikomanagement
```

Schlage dem Nutzer die Deck-Struktur vor, bevor du die Karten in der Datei ausgibst.

---

## Beispielkarten für häufige Options-Konzepte

Diese Beispiele zeigen die angestrebte Qualität und können direkt erweitert oder angepasst werden.

### Delta — Basic-Karte

```
Vorderseite:
Du hältst eine Call-Option mit Delta = 0.45.
Die Aktie steigt um $2. Um wieviel ändert sich der Optionspreis näherungsweise?

Rückseite:
~$0.90 (= 0.45 × $2)

Delta misst die Preisänderung der Option pro $1 Bewegung der Aktie.
Faustregel: Call-Deltas liegen zwischen 0 und 1, Put-Deltas zwischen -1 und 0.
ATM-Optionen haben Delta ~0.50 (50/50-Wahrscheinlichkeit ITM bei Verfall).
```

### Covered Call — Diagramm-Karte

```
Vorderseite:
Wie sieht das Payoff-Profil eines Covered Calls aus?
(Du besitzt 100 Aktien à $50 und verkaufst eine Call-Option mit Strike $55, Prämie $2)

Rückseite:
[Mermaid xychart-beta Payoff-Diagramm]

Maximaler Gewinn: $7/Aktie (Kursgewinn $5 + Prämie $2)
Maximaler Verlust: Aktie fällt auf $0 minus Prämie ($2 Puffer)
Breakeven: $48 (Kaufpreis $50 minus Prämie $2)
```

### Strategie-Auswahl — Entscheidungsbaum-Karte

```
Vorderseite:
Welche einfache Optionsstrategie passt zu welcher Markterwartung?
(Bullish / Neutral / Bearish)

Rückseite:
[Flowchart-Diagramm mit Entscheidungsbaum]
```

---

## Qualitätscheckliste

Bevor du eine Karte ausgibst, prüfe:
- [ ] Kann man die Frage beantworten ohne die Antwort gesehen zu haben? (Nicht zu trivial, nicht zu breit)
- [ ] Ist die Rückseite präzise und nicht länger als nötig?
- [ ] Gibt es ein Beispiel oder eine Analogie, die das Konzept verankert?
- [ ] Würde ein Diagram das Verständnis wirklich verbessern — oder ist es nur Dekoration?
- [ ] Ist die Karte "atomar" (eine Idee pro Karte)?
- [ ] Ist Fachvokabular auf der Vorderseite oder der Rückseite zuerst zu sehen? (Überlege, welche Richtung sinnvoller ist)

---

## Hinweis zum Bulk-Export

Wenn der Nutzer viele Karten für ein ganzes Themengebiet möchte, erstelle die TSV-Datei und zeige die Karten dann in Gruppen (je 5–10) im Markdown-Format zur Überprüfung an. Beginne mit den wichtigsten Grundlagenbegriffen (Pareto: die 20% die 80% des Verständnisses ausmachen).
