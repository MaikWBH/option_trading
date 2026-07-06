# Anki-Karten: Covered Call Strategie

**Deck:** `Optionen::Strategien::Covered Call`  
**Karten gesamt:** 8 (7 Basic, 1 Cloze — davon 1 mit Payoff-Diagramm)

---

## Karte 1 — Basic: Komponenten

**Vorderseite:**
> Was sind die zwei Komponenten eines Covered Calls?

**Rückseite:**

1. **Long Stock** — Du besitzt bereits 100 Aktien des Underlyings.
2. **Short Call** — Du verkaufst eine Call-Option auf dieselbe Aktie (gleicher Basiswert, gleicher Verfall).

Die Option ist "covered" (gedeckt), weil du die Aktien bereits hältst — im Ausübungsfall kannst du sie direkt liefern, ohne sie neu kaufen zu müssen.

---

## Karte 2 — Basic: Wann einsetzen?

**Vorderseite:**
> Welche Markterwartung rechtfertigt den Einsatz eines Covered Calls?

**Rückseite:**

**Neutral bis leicht bullisch.**

Geeignet wenn:
- Du die Aktie bereits besitzt und sie **halten** willst
- Du einen stabilen oder **moderat steigenden** Kurs erwartest
- Du **kein** starkes Kursanstiegspotenzial siehst (oder bewusst darauf verzichtest)
- Du laufende Einnahmen aus der Prämie generieren willst

**Nicht geeignet wenn:** Du einen starken Kursanstieg erwartest — deine Gewinne sind durch den Strike gedeckelt.

---

## Karte 3 — Diagramm: Payoff-Profil

**Vorderseite:**
> Wie sieht das Payoff-Profil eines Covered Calls bei Verfall aus?  
> (Aktie gekauft bei $50 | Short Call Strike $55 | Prämie erhalten: $2)

**Rückseite:**

```mermaid
xychart-beta
    title "Covered Call Payoff bei Verfall"
    x-axis [40, 42, 44, 46, 48, 50, 52, 54, 55, 57, 60]
    y-axis "Gewinn/Verlust ($/Aktie)" -10 10
    line [-8, -6, -4, -2, 0, 2, 4, 6, 7, 7, 7]
```

| Kennzahl | Wert | Formel |
|---|---|---|
| **Breakeven** | $48 | Kaufpreis − Prämie |
| **Max. Gewinn** | $7 | (Strike − Kaufpreis) + Prämie |
| **Max. Verlust** | $48/Aktie | Kaufpreis − Prämie (bei S → 0) |

**Interpretation:** Die Kurve steigt linear bis zum Strike ($55), danach ist der Gewinn gedeckelt. Links vom Breakeven ($48) macht die Position Verlust.

> **Anki-Hinweis:** Mermaid-Rendering erfordert einmalige Einrichtung im Kartentemplate:  
> `Extras → Kartentypen → Vorlage bearbeiten` → Script-Tag einfügen (siehe Import-Hinweise unten).

---

## Karte 4 — Basic: Maximaler Gewinn

**Vorderseite:**
> Covered Call: Aktie bei $50 gekauft, Call Strike $55 verkauft, Prämie $2 erhalten.  
> Was ist der **maximale Gewinn** pro Aktie, und wann tritt er ein?

**Rückseite:**

**$7 pro Aktie**, wenn der Aktienkurs bei Verfall **≥ Strike ($55)** liegt.

**Formel: Max. Gewinn = (Strike − Kaufpreis) + Prämie**  
= (55 − 50) + 2 = **$7**

- Kursgewinn bis zum Strike: $5
- Prämieneinnahme: $2
- Gewinne über $55 hinaus gehen an den Call-Käufer (du hast sie "verkauft")

---

## Karte 5 — Basic: Maximaler Verlust

**Vorderseite:**
> Covered Call: Aktie bei $50 gekauft, Prämie $2 erhalten.  
> Was ist der **maximale Verlust** pro Aktie?

**Rückseite:**

**$48 pro Aktie** — im theoretischen Fall, dass die Aktie auf $0 fällt.

**Formel: Max. Verlust = Kaufpreis − Prämie**  
= 50 − 2 = **$48**

Die Prämie ($2) puffert den Verlust leicht ab, eliminiert das Downside-Risiko aber **nicht**. Der Covered Call bietet keinen substanziellen Schutz gegen starke Kursrückgänge — dafür bräuchtest du einen Protective Put.

---

## Karte 6 — Cloze: Breakeven-Formel

**Text:**

Beim Covered Call liegt der Breakeven-Punkt bei {{c1::Kaufpreis − Prämie}}.

Beispiel: Aktie gekauft bei **$50**, Call-Prämie erhalten **$2** → Breakeven = {{c2::$48}}.

Interpretation: Unterhalb von $48 macht die Gesamtposition Verlust — trotz der erhaltenen Prämie.

---

## Karte 7 — Basic: Opportunity Cost (starker Kursanstieg)

**Vorderseite:**
> Du hast einen Covered Call: Aktie Einstieg $50, Call Strike $55, Prämie $2 erhalten.  
> Die Aktie steigt auf $70. Was passiert, und was kostet dich das?

**Rückseite:**

Die Call-Option wird ausgeübt. Du **musst** deine Aktien zum Strike $55 liefern.

- **Dein Gewinn:** $7 (= $5 Kursgewinn + $2 Prämie)
- **Entgangener Gewinn:** $15 (= $70 − $55 — dieser Betrag geht an den Call-Käufer)

**Opportunity Cost** ist das Hauptrisiko des Covered Calls: Du verkaufst das Upside-Potenzial gegen eine begrenzte Prämie. Das ist der bewusste "Preis" der Strategie — akzeptabel, wenn du ohnehin keinen starken Anstieg erwartet hast.

---

## Karte 8 — Basic: Alle Kennzahlen auf einen Blick

**Vorderseite:**
> Nenne die drei wichtigsten Kennzahlen des Covered Calls als Formeln.  
> (Kaufpreis = K, Strike = S, Prämie = P)

**Rückseite:**

| Kennzahl | Formel | Beispiel (K=$50, S=$55, P=$2) |
|---|---|---|
| **Max. Gewinn** | (S − K) + P | **$7** |
| **Max. Verlust** | K − P | **$48** |
| **Breakeven** | K − P | **$48** |

Beachte: Max. Verlust und Breakeven haben dieselbe Formel — beide = Kaufpreis minus Prämie.  
Der Gewinn ist nach oben durch den Strike **gedeckelt**, der Verlust nach unten durch den Aktienkurs (max. auf $0) **unbegrenzt** (bis K−P).

---

## Import-Hinweise für Anki

### Kartentypen

- **Karten 1–5, 7–8:** Basic-Karten → mit dem `#notetype:Basic`-Block aus `cards.tsv` importieren
- **Karte 6:** Cloze-Karte → mit dem `#notetype:Cloze`-Block importieren (separater Import-Vorgang)

### Mermaid-Diagramm einrichten (einmalig)

Für Karte 3 (Payoff-Diagramm) muss **einmalig** folgendes in die Kartenvorlage eingefügt werden:

1. Anki öffnen → **Extras → Kartentypen verwalten**
2. Den "Basic"-Typ auswählen → **Vorlage bearbeiten**
3. Am Ende des **Rückseiten-Templates** einfügen:

```html
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true});</script>
```
