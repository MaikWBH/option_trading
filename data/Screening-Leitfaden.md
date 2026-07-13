# Wöchentlicher Screening-Leitfaden: Cash-Secured Puts & Covered Calls bei IBKR
 
> Entstanden in zwei Durchgängen: Recherche (Agent 1) → Prüfung gegen deine Grundlagen-Zusammenfassung + Diskussion (Agent 2) → finale, geprüfte Fassung.
> **Kein Anlageberatung.** Dient dem Aufbau eines wiederholbaren Paper-Trading-Prozesses.
 
---
 
## 0. Das Ziel dieses Leitfadens
 
Ein **fester wöchentlicher Ablauf**, mit dem du in 20–30 Minuten von "ich habe keine Idee" zu "hier sind 2–3 passende Cash-Secured-Put- oder Covered-Call-Kandidaten" kommst – reproduzierbar, ohne jedes Mal neu nachzudenken.
 
Der Prozess hat drei Schichten:
1. **Watchlist** – WELCHE Aktien überhaupt in Frage kommen (macht man selten neu).
2. **Wochen-Screening** – WELCHE davon diese Woche gute Konditionen bieten (macht man wöchentlich).
3. **Strike-Auswahl** – WELCHER konkrete Strike/Verfall (macht man pro Trade).
 
---
 
## 1. Starter-Watchlist (ausgewogen, zum Üben im Paper Trading)
 
Kriterium für die Auswahl: **hohe Liquidität** (enge Geld-Brief-Spanne, hohes Open Interest), **großkapitalisiert**, **über verschiedene Branchen gestreut** – damit du früh lernst, wie sich Prämien je nach Sektor/Volatilität unterscheiden. Das ist eine neutrale Lern-Auswahl, keine Kaufempfehlung.
 
| Sektor | Ticker | Warum als Einstieg geeignet |
|---|---|---|
| Tech (Mega-Cap) | AAPL, MSFT | Sehr liquide Optionsketten, enge Spreads, moderate Volatilität |
| Zahlungsverkehr | V oder MA | Stabil, breit gehandelt |
| Basiskonsum | KO, PG | Niedrige Volatilität, gut zum Üben mit kleinen Prämien |
| Gesundheit | JNJ | Defensiv, ruhig |
| Finanzen | JPM | Liquide, reagiert auf Zinsnews |
| Energie | XOM oder CVX | Andere Volatilitäts-/Zyklus-Dynamik als Tech |
| Breiter Markt (ETF) | SPY oder QQQ | Kein Einzelaktienrisiko, sehr enge Spreads, ideal zum reinen Prämien-Üben |
 
**Praxistipp:** Starte im Paper Trading bewusst mit 3–4 dieser Namen plus einem ETF, statt gleich 15 Werte zu verfolgen. Weniger Positionen = mehr Verständnis pro Trade.
 
*Später erweitern:* Sobald du den Ablauf verinnerlicht hast, kannst du Werte ergänzen, die du ohnehin aus anderen Gründen im Blick hast (z. B. aus deinem bestehenden Tech-ETF-Umfeld) – aber weiterhin nur Aktien, die du laut Cash-Secured-Put-Logik auch wirklich besitzen möchtest.
 
---
 
## 2. Deine Werkzeuge in IBKR TWS
 
TWS bringt für diesen Prozess alles kostenlos mit, was du brauchst – du musst nur wissen, welches Tool wofür:
 
| TWS-Tool | Wofür in deinem Workflow |
|---|---|
| **Market Scanner** | Grobes Screening nach Kriterien wie Volumen, IV, Kursbewegung über den gesamten Markt |
| **Option Chain / OptionTrader** | Konkrete Strikes, Prämien, Delta, Bid/Ask je Verfall ansehen und Order aufgeben |
| **Probability Lab** | Zeigt dir, mit welcher Wahrscheinlichkeit ein Strike am Verfallstag im/aus dem Geld landet – gut zur Delta-Kontrolle |
| **Option Strategy Lab** | Du gibst eine Markterwartung ein (z. B. "Kurs bleibt seitwärts/steigt leicht"), TWS schlägt passende Strategien inkl. Cash-Secured Put/Covered Call vor und lässt nach Prämie, Delta, Strike, Verfall filtern |
| **Volatility Lab** | Vergleicht aktuelle mit historischer Volatilität – hilfreich, um "teure" (hohe IV) Optionen zu erkennen |
| **Option Activity Analysis** | Zeigt, wo Open Interest/Volumen wirklich liegt – Liquiditätscheck vor dem Trade |
 
**Tool-Ausblick (kostenpflichtig, falls du später mehr willst):**
- **Barchart Premier** (~10 $/Monat aufwärts) und **MarketChameleon** bieten eigene IV-Rank-/IV-Percentile-Screener über tausende Aktien hinweg, die TWS in dieser Form nicht hat – nützlich, um aus dem gesamten Markt statt nur deiner Watchlist zu screenen.
- **PowerOptions** ist ein spezialisierter Prämienverkäufer-Screener (IV Rank, IV Percentile, IV/HV-Spread über mehrere tausend Aktien).
- Für den Einstieg reicht aber **TWS allein** völlig aus – die kostenpflichtigen Tools lohnen sich erst, wenn du über deine feste Watchlist hinaus systematisch neue Kandidaten im Gesamtmarkt suchen willst.
 
---
 
## 3. Der wöchentliche Ablauf (ca. 20–30 Min, z. B. Montagfrüh oder Sonntagabend)
 
### Schritt 1 – Vorfilter auf deiner Watchlist
Gehe deine Watchlist durch und schließe diese Woche alle Werte aus, bei denen:
- **Earnings (Quartalszahlen) in die gewählte Laufzeit fallen** (unberechenbare Kurssprünge – als Einsteiger meiden).
- Größere angekündigte Unternehmensereignisse anstehen (Übernahme, Produktlaunch mit hoher Erwartung etc.).
 
### Schritt 2 – Volatilität prüfen (Volatility Lab oder Option Chain)
Schau dir die **implizite Volatilität** der übrig gebliebenen Werte an. Bevorzuge Werte, deren IV **aktuell eher erhöht** ist im Vergleich zu ihrem eigenen historischen Niveau – dort bekommst du für dasselbe Risiko mehr Prämie. Ist die IV bei allen Werten sehr niedrig, ist das kein Beinbruch, nur: die Prämien werden mager ausfallen.
 
### Schritt 3 – Optionskette öffnen (OptionTrader)
Für jeden verbliebenen Kandidaten:
1. Verfall wählen: **30–45 Tage** Restlaufzeit.
2. Strike wählen über **Delta**, nicht über den Kurs:
   - Cash-Secured Put: Delta ca. **–0,20 bis –0,30**
   - Covered Call: Delta ca. **0,20 bis 0,30**
   (Delta ≈ grobe Wahrscheinlichkeit, dass die Option am Ende im Geld landet – niedriger Delta = konservativer.)
3. Liquidität checken: **enger Bid-Ask-Spread** und **spürbares Open Interest/Volumen** an diesem Strike. Sehr breite Spreads = schlechte Fülloption, meiden.
 
### Schritt 4 – Gegenprobe im Probability Lab / Option Strategy Lab
Trage deine Erwartung ein (z. B. "Kurs bleibt über X $" für einen Put) und lass dir die Wahrscheinlichkeit sowie Alternativstrikes anzeigen. Nutze das als zweite Meinung, nicht als alleinige Entscheidungsgrundlage.
 
### Schritt 5 – Auswahl treffen und Limit-Order vorbereiten
- Wähle die 1–2 Kandidaten mit dem besten Verhältnis aus Prämie, Delta und Liquidität.
- Preis der Order: **immer als Limit**, ausgehend vom **Mid-Preis** zwischen Bid und Ask.
- Positionsgröße: pro Trade nur ein kleiner Teil des (Paper-)Depots – auch im Paper Trading, damit sich die Größenordnung später real richtig anfühlt.
 
### Schritt 6 – Dokumentieren
Halte kurz fest: Ticker, Strike, Verfall, Delta, kassierte Prämie, Grund für die Wahl. Das ist die Basis, um nach ein paar Wochen zu sehen, welche Muster bei dir funktionieren.
 
---
 
## 4. Checkliste zum Abhaken (jede Woche)
 
- [ ] Watchlist auf anstehende Earnings/Events geprüft und Kandidaten mit Ereignis in der Laufzeit ausgeschlossen
- [ ] IV der verbliebenen Kandidaten verglichen, eher erhöhte IV bevorzugt
- [ ] Verfall 30–45 Tage gewählt
- [ ] Strike über Delta (~0,20–0,30) gewählt, nicht über Bauchgefühl
- [ ] Bid-Ask-Spread eng, Open Interest ausreichend
- [ ] Nur Aktien im Auswahlprozess, die ich im Falle einer Andienung auch wirklich halten möchte
- [ ] Positionsgröße bewusst klein gehalten
- [ ] Limit-Order nahe Mid-Preis, keine Market-Order
- [ ] Trade dokumentiert
 
---
 
## 5. Häufige Anfängerfehler (aus der Prüfungsrunde ergänzt)
 
1. **Delta ignorieren und nur auf die Prämienhöhe schauen.** Eine hohe Prämie bei hohem Delta bedeutet auch eine hohe Wahrscheinlichkeit der Andienung – das ist kein Geschenk, sondern der Preis für mehr Risiko.
2. **Earnings-Termine übersehen.** Der häufigste Anfängerfehler: Eine Option läuft über den Quartalszahlen-Termin, die IV kollabiert danach ("IV Crush") oder der Kurs springt – beides kann den Trade in eine ungeplante Richtung drehen.
3. **Zu viele unterschiedliche Werte gleichzeitig verfolgen.** Am Anfang lieber wenige Werte richtig gut kennenlernen als 20 Werte oberflächlich screenen.
4. **Prämie ohne Liquiditätscheck kassieren.** Ein "guter" Delta-Strike mit breitem Spread lässt sich später schlecht oder nur zu ungünstigen Kursen glattstellen/rollen.
5. **Aktien im Screening haben, die man eigentlich gar nicht besitzen möchte.** Nur weil die IV hoch ist, heißt das nicht, dass die Aktie in dein Depot gehört – die Grundregel "nur Aktien, die du wirklich willst" gilt für die *gesamte* Watchlist, nicht nur für den einzelnen Trade.
 
---
 
## 6. Kurzformel zum Merken
 
> **Watchlist fest → Earnings raus → IV vergleichen → 30–45 DTE → Delta 0,20–0,30 → Liquidität prüfen → Limit-Order zum Mid → klein positionieren → dokumentieren.**
 
---
 
## Quellen (Stand: Juli 2026)
- IBKR Traders' Academy: OptionTrader, Option Strategy Lab, Probability Lab, TWS Option Tools (interactivebrokers.com/campus)
- Barchart.com: IV Rank & IV Percentile Erklärung, Options Screener
- MarketChameleon: Implied Volatility Rankings Report
- PowerOptions: IV Rank Screener
- Deine hochgeladene Zusammenfassung "Optionshandel bei Interactive Brokers" (Grundlage für Begriffe, Strategie-Logik und Risikoregeln)