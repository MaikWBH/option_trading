# Anki-Deck: Optionshandel Grundlagen

Fertige Anki-Karten zum Optionshandel – auf Deutsch, in einfacher Sprache, mit Beispielen und Diagrammen. Erstellt auf Basis von [../data/Optionshandel_Interactive_Brokers.md](../data/Optionshandel_Interactive_Brokers.md).

## Inhalt

| Datei | Kartentyp | Anzahl |
|---|---|---|
| `optionen_basic.tsv` | Basic (Frage → Antwort) | 68 |
| `optionen_cloze.tsv` | Cloze (Lückentext) | 12 |
| `optionen_diagramme.tsv` | Basic mit Bild (Mermaid-Diagramme) | 10 |
| `media/` | 10 Diagramm-Bilder (PNG) | — |

**Gesamt: 90 Karten**, verteilt auf 7 Unterdecks unter `Optionshandel Grundlagen`:
Grundlagen · Käufer & Verkäufer · Preis & Griechen · Strategien · IBKR-Umsetzung · Verfall & Andienung · Risikomanagement.

---

## Import in Anki – Schritt für Schritt

### 1. Bilder bereitstellen (wichtig, zuerst!)

Damit die Diagramm-Karten die Bilder anzeigen, müssen die 10 PNGs in Ankis Medienordner `collection.media`:

- **Windows:** `%APPDATA%\Anki2\<Profilname>\collection.media\`
- **macOS:** `~/Library/Application Support/Anki2/<Profilname>/collection.media/`
- **Linux:** `~/.local/share/Anki2/<Profilname>/collection.media/`

Kopiere den **kompletten Inhalt** des Ordners `media/` (alle `*.png`) dorthin.

> Tipp: Den Profilnamen siehst du in Anki unter *Datei → Profil wechseln*. Standard ist meist „Benutzer 1“.

### 2. TSV-Dateien importieren

Für **jede** der drei `.tsv`-Dateien:

1. In Anki: **Datei → Importieren…**
2. Die `.tsv`-Datei auswählen.
3. Anki erkennt die Kopfzeilen automatisch (Trennzeichen = Tab, HTML aktiviert, Notiztyp, Zieldeck).
   - Falls gefragt: **Notiztyp** = `Basic` (bzw. `Cloze` für die Cloze-Datei), **Feldtrennung** = Tab.
   - „HTML in Feldern zulassen“ muss **aktiviert** sein.
4. Auf **Importieren** klicken.

Reihenfolge egal – am besten alle drei nacheinander importieren.

### 3. Fertig

Die Karten liegen jetzt unter dem Deck **Optionshandel Grundlagen** mit seinen 7 Unterdecks. Du kannst sofort lernen.

---

## Karten anpassen oder erweitern

Die Karteninhalte stehen im gut lesbaren Generator-Skript [generate_cards.py](generate_cards.py).
Ändere dort Text/Karten und erzeuge die TSV-Dateien neu:

```bash
python3 generate_cards.py
```

Die Diagramm-Quellen (Mermaid) liegen in `../diagrams_src/*.mmd`. Wenn du ein Diagramm änderst, musst du das zugehörige PNG neu rendern (siehe `../diagrams_src/`).

---

## Lernempfehlung (aus dem Lernkonzept)

- **Spaced Repetition:** 5–10 Min täglich statt einmal 3 Stunden.
- **Interleaving:** Strategien mischen (CSP → Covered Call → Wheel), statt ein Thema am Stück zu pauken.
- **Active Recall:** erst selbst antworten, dann die Rückseite aufdecken.
- **Feynman:** Karten, bei denen du ins Stocken gerätst, laut in eigenen Worten erklären.
