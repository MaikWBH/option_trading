#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator für das Anki-Deck "Optionshandel Grundlagen".
Erzeugt drei TSV-Importdateien:
  - optionen_basic.tsv       (Notetype: Basic)
  - optionen_cloze.tsv       (Notetype: Cloze)
  - optionen_diagramme.tsv   (Notetype: Basic, mit Bildern)

Quelle der Inhalte: data/Optionshandel_Interactive_Brokers.md
Zielgruppe: kompletter Anfänger, einfache deutsche Sprache, mit Beispielen.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

DECK = "Optionshandel Grundlagen"

# ---------------------------------------------------------------------------
# BASIC-KARTEN:  (Unterdeck, Vorderseite, Rückseite, Tags)
# ---------------------------------------------------------------------------
basic = [
    # --- 1. Grundlagen ------------------------------------------------------
    ("Grundlagen",
     "Was ist eine <b>Option</b>?",
     "Ein <b>Vertrag</b> über den zukünftigen Kauf oder Verkauf eines <b>Basiswerts</b> (engl. <i>underlying</i>) – z.&nbsp;B. einer Aktie (engl. <i>stock</i>) – zu einem vorher festgelegten Preis.<br><br>Der Käufer (engl. <i>buyer</i>) erhält ein <b>Recht</b> (engl. <i>right</i>) – keine Pflicht (engl. <i>obligation</i>).",
     "grundlagen"),

    ("Grundlagen",
     "Was ist ein <b>Call</b> (dt. Kaufoption)?",
     "Das <b>Recht, die Aktie zu kaufen</b> (engl. <i>to buy</i>) – zu einem festen Preis.<br><br>🧠 Merkbild: <b>Call = Reservierung.</b> Du sicherst dir heute den Kaufpreis für später.<br>Der Käufer erwartet <b>steigende</b> Kurse (engl. <i>bullish</i>).",
     "grundlagen call"),

    ("Grundlagen",
     "Was ist ein <b>Put</b> (dt. Verkaufsoption)?",
     "Das <b>Recht, die Aktie zu verkaufen</b> (engl. <i>to sell</i>) – zu einem festen Preis.<br><br>🧠 Merkbild: <b>Put = Versicherung.</b> Du sicherst dich gegen fallende Kurse ab.<br>Der Käufer erwartet <b>fallende</b> Kurse (engl. <i>bearish</i>).",
     "grundlagen put"),

    ("Grundlagen",
     "Merkbild: Warum ist ein <b>Call</b> wie eine <b>Reservierung</b>?",
     "Du sicherst dir <b>heute</b> das Recht, etwas <b>später</b> zu einem festen Preis zu kaufen – egal, wie teuer es dann wirklich ist.",
     "grundlagen call eselsbruecke"),

    ("Grundlagen",
     "Merkbild: Warum ist ein <b>Put</b> wie eine <b>Versicherung</b>?",
     "Du sicherst dir das Recht, später zu einem festen Preis zu <b>verkaufen</b> – wie eine Versicherung gegen fallende Kurse.",
     "grundlagen put eselsbruecke"),

    ("Grundlagen",
     "Was ist der <b>Basiswert</b> (engl. <i>Underlying</i>)?",
     "Die Aktie (engl. <i>stock</i>) oder der Wert, auf den sich die Option bezieht (z.&nbsp;B. Apple).",
     "grundlagen begriffe"),

    ("Grundlagen",
     "Was ist der <b>Strike</b> (dt. Ausübungs- oder Basispreis)?",
     "Der vereinbarte Preis, zu dem die Aktie gekauft oder verkauft werden darf.<br><br>Vollständig engl.: <i>strike price</i>.",
     "grundlagen begriffe strike"),

    ("Grundlagen",
     "Was ist die <b>Prämie</b> (engl. <i>Premium</i>) einer Option?",
     "Der <b>Preis der Option</b> selbst.<br><br>Der <b>Käufer zahlt</b> sie, der <b>Verkäufer erhält</b> sie.",
     "grundlagen begriffe praemie"),

    ("Grundlagen",
     "Wie viele Aktien umfasst <b>1 Optionskontrakt</b> (engl. <i>option contract</i>)?",
     "<b>100 Aktien.</b> Der Multiplikator ist also immer 100.<br><br>💡 Eine Prämie von „1,50&nbsp;$“ bedeutet in Wirklichkeit 1,50&nbsp;$ × 100 = <b>150&nbsp;$</b> pro Kontrakt.",
     "grundlagen begriffe kontrakt"),

    ("Grundlagen",
     "Was bedeutet <b>Ausübung</b> (engl. <i>Exercise</i>)?",
     "Der <b>Käufer</b> nutzt sein Recht und kauft bzw. verkauft die Aktien zum Strike.",
     "grundlagen begriffe"),

    ("Grundlagen",
     "Was bedeutet <b>Andienung</b> (engl. <i>Assignment</i>)?",
     "Dem <b>Verkäufer</b> wird die Pflicht zugeteilt: Er muss die Aktien liefern (Call) oder abnehmen (Put).",
     "grundlagen begriffe andienung"),

    ("Grundlagen",
     "Warum sind <b>Optionen</b> <u>nicht</u> dasselbe wie <b>Optionsscheine</b> (engl. <i>warrants</i>)?",
     "<b>Optionen</b> werden direkt an einer <b>Terminbörse</b> (engl. <i>options exchange</i>) gehandelt – kein Emittenten-Ausfallrisiko.<br><br><b>Optionsscheine/Zertifikate</b> kaufst du von einer <b>Bank</b>. Geht die Bank pleite, ist dein Geld in Gefahr.",
     "grundlagen abgrenzung"),

    ("Grundlagen",
     "Wann ist ein <b>Call</b> „im Geld“ (<b>ITM</b>, engl. <i>in the money</i>)?",
     "Wenn der <b>Kurs über dem Strike</b> liegt.<br><br>Beispiel: Aktie 65&nbsp;$, Strike 60&nbsp;$ → der Call ist 5&nbsp;$ im Geld.",
     "grundlagen moneyness itm"),

    ("Grundlagen",
     "Wann ist ein <b>Put</b> „im Geld“ (<b>ITM</b>, engl. <i>in the money</i>)?",
     "Wenn der <b>Kurs unter dem Strike</b> liegt.<br><br>Beispiel: Aktie 45&nbsp;$, Strike 50&nbsp;$ → der Put ist 5&nbsp;$ im Geld.",
     "grundlagen moneyness itm"),

    ("Grundlagen",
     "Was bedeuten <b>ITM</b>, <b>ATM</b> und <b>OTM</b>?",
     "<b>ITM</b> = Im Geld (engl. <i>In The Money</i>)<br><b>ATM</b> = Am Geld (engl. <i>At The Money</i>, Kurs ≈ Strike)<br><b>OTM</b> = Aus dem Geld (engl. <i>Out of The Money</i>)<br><br>Faustregel: <b>ITM</b> ist teuer (hat echten Wert), <b>OTM</b> ist billig (nur Hoffnung).",
     "grundlagen moneyness"),

    # --- 2. Käufer / Verkäufer & Grundpositionen ---------------------------
    ("Käufer & Verkäufer",
     "Unterschied <b>Käufer (Long)</b> und <b>Verkäufer (Short)</b>?",
     "<b>Käufer / Long</b> (engl. <i>buyer</i>): zahlt Prämie, hat ein <b>Recht</b> (engl. <i>right</i>), Risiko begrenzt (max. die Prämie).<br><br><b>Verkäufer / Short</b> (engl. <i>seller</i>): erhält Prämie, hat eine <b>Pflicht</b> (engl. <i>obligation</i>), muss Geld oder Aktien bereithalten.",
     "positionen long short"),

    ("Käufer & Verkäufer",
     "Was ist ein <b>Stillhalter</b> (engl. <i>Writer</i> / Option Seller)?",
     "Der <b>Verkäufer</b> einer Option. Er <i>hält still</i> und wartet ab – hält Aktien (Call) oder Geld (Put) bereit, falls der Käufer sein Recht nutzt. Dafür kassiert er die <b>Prämie</b>.",
     "positionen stillhalter"),

    ("Käufer & Verkäufer",
     "Merksatz: Der Stillhalter ist wie eine …?",
     "… <b>Versicherung, die Prämien kassiert.</b><br><br>Meistens tritt der „Schadensfall“ nicht ein, und die Prämie ist verdient. Darauf baut die konservative Strategie auf.",
     "positionen stillhalter eselsbruecke"),

    ("Käufer & Verkäufer",
     "Was erwartet ein <b>Long Call</b>?",
     "Setzt auf <b>steigende</b> Kurse (engl. <i>bullish</i>) – Recht zu kaufen.",
     "positionen"),

    ("Käufer & Verkäufer",
     "Was erwartet ein <b>Long Put</b>?",
     "Setzt auf <b>fallende</b> Kurse (engl. <i>bearish</i>) – Recht zu verkaufen.",
     "positionen"),

    ("Käufer & Verkäufer",
     "Was wünscht sich ein <b>Short Call</b> (Verkäufer eines Calls)?",
     "Dass der Kurs <b>NICHT stark steigt</b> – dann verfällt der Call wertlos (engl. <i>expires worthless</i>) und die Prämie bleibt ihm.",
     "positionen"),

    ("Käufer & Verkäufer",
     "Was wünscht sich ein <b>Short Put</b> (Verkäufer eines Puts)?",
     "Dass der Kurs <b>NICHT stark fällt</b> – dann verfällt der Put wertlos (engl. <i>expires worthless</i>) und die Prämie bleibt ihm.",
     "positionen"),

    # --- 3. Preisbildung & Griechen ----------------------------------------
    ("Preis & Griechen",
     "Aus welchen zwei Bausteinen besteht die <b>Prämie</b> (engl. <i>Premium</i>)?",
     "<b>Prämie = Innerer Wert + Zeitwert</b><br><br>• Innerer Wert (engl. <i>intrinsic value</i>) = schon „echtes Geld“ wert (nur bei ITM).<br>• Zeitwert (engl. <i>time value</i>) = Aufschlag für Restlaufzeit &amp; Unsicherheit; schmilzt bis zum Verfall auf null.",
     "preis praemie"),

    ("Preis & Griechen",
     "Was ist der <b>innere Wert</b> (engl. <i>Intrinsic Value</i>) einer Option?",
     "Der Teil der Prämie, der schon „echtes Geld“ wert ist – <b>nur bei ITM-Optionen</b> vorhanden.",
     "preis innerer-wert"),

    ("Preis & Griechen",
     "Was ist der <b>Zeitwert</b> (engl. <i>Time Value</i> / Extrinsic Value) einer Option?",
     "Der Aufschlag für die <b>verbleibende Zeit und Unsicherheit</b>. Er schmilzt bis zum Verfall auf <b>null</b>.",
     "preis zeitwert"),

    ("Preis & Griechen",
     "Was misst <b>Delta</b> (einer der „Griechen“, engl. <i>the Greeks</i>)?",
     "Wie stark sich die Prämie ändert, wenn die Aktie sich um <b>1&nbsp;$</b> bewegt.<br><br>Beispiel: Delta 0,40 → Aktie +1&nbsp;$ → Option ca. <b>+0,40&nbsp;$</b>.<br>🧠 Merkhilfe: „<b>Richtung</b>“.",
     "preis griechen delta"),

    ("Preis & Griechen",
     "Delta grob als <b>Wahrscheinlichkeit</b> gelesen – was heißt das?",
     "Delta ist ungefähr die <b>Wahrscheinlichkeit</b>, dass die Option im Geld endet.<br><br>Beispiel: Delta 0,30 → grob 30&nbsp;% Chance, dass sie ITM ausläuft.",
     "preis griechen delta"),

    ("Preis & Griechen",
     "Was misst <b>Theta</b>?",
     "Wie viel Wert die Option <b>pro Tag</b> durch Zeitablauf verliert – der <b>Zeitwertverfall</b> (engl. <i>time decay</i>).<br><br>🧠 Merkhilfe: „<b>T</b>ime“.",
     "preis griechen theta"),

    ("Preis & Griechen",
     "Was misst <b>Vega</b>?",
     "Wie stark die Prämie auf Änderungen der <b>Volatilität</b> (engl. <i>volatility</i>) reagiert.<br><br>🧠 Merkhilfe: „<b>V</b>olatilität“.",
     "preis griechen vega"),

    ("Preis & Griechen",
     "Was misst <b>Gamma</b>?",
     "Wie schnell sich das <b>Delta selbst</b> ändert.<br><br>🧠 Merkhilfe: „<b>Beschleunigung</b>“.",
     "preis griechen gamma"),

    ("Preis & Griechen",
     "Warum ist <b>Theta der beste Freund des Stillhalters</b>?",
     "Jeden Tag verliert die Option Zeitwert. Für den <b>Käufer</b> schlecht (Option „schmilzt“), für den <b>Verkäufer</b> gut: Er hat die Prämie kassiert und profitiert vom Wertverlust.",
     "preis griechen theta stillhalter"),

    ("Preis & Griechen",
     "Wann beschleunigt sich der <b>Zeitwertverfall</b> (engl. <i>Time Decay</i>) stark?",
     "In den letzten <b>ca. 30 Tagen</b> vor Verfall.<br><br>Deshalb verkaufen Stillhalter oft Optionen mit <b>30–45 Tagen</b> Restlaufzeit (engl. <i>days to expiration, DTE</i>).",
     "preis griechen theta"),

    ("Preis & Griechen",
     "Was ist <b>implizite Volatilität (IV)</b> (engl. <i>Implied Volatility</i>)?",
     "Die vom <b>Markt erwartete zukünftige Schwankungsbreite</b> des Kurses.",
     "preis volatilitaet iv"),

    ("Preis & Griechen",
     "Wie wirkt <b>hohe IV</b> auf die Prämie?",
     "<b>Hohe IV → hohe Prämien.</b> Für Verkäufer gut (mehr Prämie).<br><b>Niedrige IV → magere Prämien.</b>",
     "preis volatilitaet iv"),

    ("Preis & Griechen",
     "Profi-Regel: Wann eröffnet man <b>Stillhaltergeschäfte</b> am besten?",
     "Bei <b>hoher</b> impliziter Volatilität (z.&nbsp;B. nach einem Kursrutsch, wenn die Angst hoch ist). Man verkauft „teure“ Optionen und profitiert, wenn sich der Markt beruhigt.",
     "preis volatilitaet iv strategie"),

    # --- 4. Einsteiger-Strategien ------------------------------------------
    ("Strategien",
     "Was ist die Grundidee eines <b>Cash-Secured Put (CSP)</b> (dt. bar gedeckter Put)?",
     "Du verkaufst einen Put auf eine Aktie, die du <b>ohnehin gerne besitzen würdest</b> – nur etwas billiger. Du kassierst sofort die Prämie und hältst das Kaufgeld bereit (<i>cash secured</i>).",
     "strategien csp"),

    ("Strategien",
     "CSP-Beispiel: Aktie 52&nbsp;$, du verkaufst einen Put Strike 50&nbsp;$ für 1,50&nbsp;$ Prämie. Die zwei möglichen Ausgänge?",
     "1) Kurs bleibt <b>über 50&nbsp;$</b> → Put verfällt wertlos, du behältst <b>150&nbsp;$</b> Prämie.<br>2) Kurs fällt <b>unter 50&nbsp;$</b> → du kaufst 100 Aktien zu 50&nbsp;$, effektiver Einstand <b>48,50&nbsp;$</b>.<br><br>Beide Ausgänge sind okay.",
     "strategien csp beispiel"),

    ("Strategien",
     "CSP: Wie berechnet sich der <b>maximale Gewinn</b> (engl. <i>max profit</i>)?",
     "= die <b>Prämie</b>.<br><br>Beispiel: 1,50&nbsp;$ × 100 = <b>150&nbsp;$</b>.",
     "strategien csp kennzahlen"),

    ("Strategien",
     "CSP: Wie berechnet sich der <b>Breakeven</b> (dt. Gewinnschwelle)?",
     "<b>Breakeven = Strike − Prämie</b><br><br>Beispiel: 50&nbsp;$ − 1,50&nbsp;$ = <b>48,50&nbsp;$</b>.",
     "strategien csp kennzahlen"),

    ("Strategien",
     "CSP: Wie groß ist der <b>maximale Verlust</b> (engl. <i>max loss</i>)?",
     "(Strike − Prämie) × 100, falls der Kurs auf 0 fällt.<br><br>Beispiel: (50 − 1,50) × 100 = <b>4.850&nbsp;$</b>.<br>⚠️ Das Risiko ist groß – die Aktie könnte theoretisch auf 0 fallen.",
     "strategien csp kennzahlen risiko"),

    ("Strategien",
     "Goldene Regel für den <b>Cash-Secured Put</b>?",
     "Verkaufe Puts <b>nur auf Aktien, die du wirklich besitzen willst</b> – und nur so viele, wie du dir tatsächlich leisten kannst zu kaufen.",
     "strategien csp regel"),

    ("Strategien",
     "Was ist die Grundidee eines <b>Covered Calls</b> (dt. gedeckter Call)?",
     "Du besitzt bereits <b>100 Aktien</b> und verkaufst darauf einen Call. Du kassierst Prämie und bist bereit, die Aktien zu einem höheren Preis (Strike) zu verkaufen. Der Call ist durch deine Aktien <b>gedeckt</b> (engl. <i>covered</i>).",
     "strategien covered-call"),

    ("Strategien",
     "Covered-Call-Beispiel: 100 Aktien zu 50&nbsp;$ gekauft, Call Strike 55&nbsp;$ für 1,50&nbsp;$ verkauft. Die zwei Ausgänge?",
     "1) Kurs <b>unter 55&nbsp;$</b> → Call verfällt wertlos, du behältst Aktien + <b>150&nbsp;$</b> Prämie.<br>2) Kurs <b>über 55&nbsp;$</b> → Aktien werden zu 55&nbsp;$ verkauft; Gewinn = 5&nbsp;$ Kurs + 1,50&nbsp;$ Prämie.",
     "strategien covered-call beispiel"),

    ("Strategien",
     "Covered Call: <b>maximaler Gewinn</b> (engl. <i>max profit</i>)?",
     "(Strike − Kaufpreis + Prämie) × 100.<br><br>Beispiel: (55 − 50 + 1,50) × 100 = <b>650&nbsp;$</b>.",
     "strategien covered-call kennzahlen"),

    ("Strategien",
     "Was ist der <b>Hauptnachteil</b> eines Covered Calls?",
     "Der Gewinn ist nach oben <b>gedeckelt</b> (engl. <i>capped</i>). Steigt die Aktie stark (z.&nbsp;B. auf 70&nbsp;$), musst du trotzdem zum Strike (55&nbsp;$) verkaufen und verpasst den Rest.",
     "strategien covered-call risiko"),

    ("Strategien",
     "Für welche Aktien eignet sich ein <b>Covered Call</b> besonders?",
     "Für <b>ruhige, seitwärts laufende</b> Aktien. Für „Raketen“ (starke Aufwärtstrends) weniger, weil man das Aufwärtspotenzial abschneidet.",
     "strategien covered-call"),

    ("Strategien",
     "Was ist <b>„The Wheel“</b> (dt. „das Rad“)?",
     "Ein Kreislauf aus beiden Strategien: <b>1)</b> Cash-Secured Put verkaufen, bis Aktien angedient werden → <b>2)</b> auf diese Aktien Covered Calls verkaufen, bis sie verkauft werden → dann wieder bei 1. In jeder Runde kassierst du Prämien.",
     "strategien wheel"),

    ("Strategien",
     "Was ist mit der <b>„zweiten Dividende“</b> gemeint?",
     "Die regelmäßig kassierten <b>Prämien</b> aus dem Verkauf von Optionen (Stillhalten) – ein Zusatzeinkommen zusätzlich zur normalen Dividende (engl. <i>dividend</i>).",
     "strategien wheel eselsbruecke"),

    # --- 5. IBKR-Umsetzung -------------------------------------------------
    ("IBKR-Umsetzung",
     "Warum ist <b>Interactive Brokers (IBKR)</b> bei Optionshändlern beliebt?",
     "• Günstige Gebühren (engl. <i>fees / commissions</i>)<br>• Weltweiter Zugang (v.&nbsp;a. liquide US-Optionsmärkte)<br>• Professionelle Software<br>• Hohe Sicherheit durch strenge Regulierung",
     "ibkr"),

    ("IBKR-Umsetzung",
     "Unterschied <b>Cash-Konto</b> (engl. <i>cash account</i>) und <b>Margin-Konto</b> (engl. <i>margin account</i>)?",
     "<b>Cash-Konto:</b> nur eigenes Geld, konservativ, weniger Strategien.<br><b>Margin-Konto:</b> Handel auf Kreditbasis, nötig für die meisten Optionsstrategien – aber mehr Risiko (Margin Call möglich).",
     "ibkr konto"),

    ("IBKR-Umsetzung",
     "Welche drei IBKR-Werkzeuge (Software) gibt es?",
     "<b>Trader Workstation (TWS)</b> – Profi-Desktop.<br><b>Client Portal</b> – Weboberfläche, gut für Einsteiger.<br><b>IBKR Mobile</b> – App fürs Smartphone.",
     "ibkr software"),

    ("IBKR-Umsetzung",
     "Warum immer mit <b>Limit-Orders</b> handeln (nie „Market“)?",
     "Optionen haben oft eine <b>breite Geld-Brief-Spanne</b> (engl. <i>bid-ask spread</i>). Bei einer Marktorder bekommst du den ungünstigsten Preis. Mit einer <b>Limit-Order</b> setzt du einen fairen Preis nahe dem Mittelkurs (engl. <i>mid</i>).",
     "ibkr order limit"),

    ("IBKR-Umsetzung",
     "Was bedeuten <b>Bid</b>, <b>Ask</b> und <b>Mid</b>?",
     "<b>Bid</b> (dt. Geldkurs) = Preis, zu dem du sofort verkaufen kannst.<br><b>Ask</b> (dt. Briefkurs) = Preis, zu dem du sofort kaufen kannst.<br><b>Mid</b> = Mitte dazwischen – hier solltest du dein Limit ansetzen.",
     "ibkr order"),

    ("IBKR-Umsetzung",
     "Grobe Gebühr für eine US-Aktienoption bei IBKR?",
     "Oft rund <b>0,65&nbsp;USD pro Kontrakt</b> (Gebühr = engl. <i>commission</i>; plus kleine Mindestgebühr pro Order). Prüfe die aktuellen Konditionen immer selbst.",
     "ibkr gebuehren"),

    ("IBKR-Umsetzung",
     "Warum brauchst du bei IBKR ein <b>Marktdaten-Abo</b> (engl. <i>market data subscription</i>)?",
     "Für <b>Echtzeit-Optionspreise</b> (z.&nbsp;B. OPRA-Daten für US-Optionen). Ohne Abo siehst du oft nur verzögerte Kurse.",
     "ibkr marktdaten"),

    # --- 6. Verfallstag & Andienung ----------------------------------------
    ("Verfall & Andienung",
     "Was bedeutet „<b>amerikanischer Typ</b>“ (engl. <i>American style</i>) bei US-Aktienoptionen?",
     "Der Käufer darf <b>jederzeit</b> bis zum Verfall (engl. <i>expiration</i>) ausüben – nicht nur am letzten Tag.",
     "verfall typ"),

    ("Verfall & Andienung",
     "Was passiert, wenn die Option <b>wertlos (OTM)</b> ausläuft (engl. <i>expires worthless</i>)?",
     "Du musst <b>nichts tun</b> – die kassierte Prämie ist dein Gewinn.",
     "verfall otm"),

    ("Verfall & Andienung",
     "Was passiert, wenn die Option <b>im Geld (ITM)</b> ausläuft?",
     "Du wirst <b>angedient</b> (engl. <i>assigned</i>): Du musst die Aktien liefern (Call) bzw. abnehmen (Put).",
     "verfall itm andienung"),

    ("Verfall & Andienung",
     "Was bedeutet eine Position <b>„rollen“</b> (engl. <i>Rolling</i>)?",
     "Du <b>kaufst die laufende Option zurück</b> und verkaufst gleichzeitig eine <b>neue mit späterem Verfall</b> (und ggf. anderem Strike) – um Andienung zu vermeiden oder weiter Prämien zu kassieren.",
     "verfall rollen"),

    ("Verfall & Andienung",
     "Wann droht eine <b>vorzeitige Andienung</b> (engl. <i>early assignment</i>) in der Praxis meist?",
     "Meist nur <b>kurz vor Verfall</b> oder rund um <b>Dividendentermine</b> (engl. <i>ex-dividend date</i>).",
     "verfall andienung"),

    # --- 7. Risikomanagement & Anfängerfehler ------------------------------
    ("Risikomanagement",
     "Woher kommt laut den Quellen der Erfolg im Optionshandel?",
     "<b>Nicht</b> von der cleversten Strategie, sondern von <b>Disziplin und Risikomanagement</b> (engl. <i>risk management</i>).",
     "risiko grundsatz"),

    ("Risikomanagement",
     "Regel: Wie groß sollten <b>Positionen</b> sein (Positionsgröße)?",
     "<b>Klein.</b> Pro Trade nur einen kleinen Bruchteil des Kapitals einsetzen – so verkraftest du auch einen Rückschlag.<br><br>Fachbegriff: <b>Positionsgröße</b> (engl. <i>position sizing</i>).",
     "risiko position"),

    ("Risikomanagement",
     "Regel: Auf welche Aktien solltest du <b>Puts verkaufen</b>?",
     "Nur auf <b>Aktien, die du wirklich besitzen willst</b>. Ein Cash-Secured Put ist ein Kaufauftrag mit Bonus.",
     "risiko qualitaet"),

    ("Risikomanagement",
     "Regel: Wann nehmen viele Stillhalter <b>Gewinne mit</b>?",
     "Sobald z.&nbsp;B. <b>50&nbsp;% des möglichen Gewinns</b> erreicht sind – sie kaufen die Option zurück (engl. <i>buy to close</i>). Das senkt das Risiko in der Schlussphase.",
     "risiko exit"),

    ("Risikomanagement",
     "Warum sollten Anfänger keine <b>nackten (ungedeckten) Calls</b> (engl. <i>naked calls</i>) verkaufen?",
     "Weil das Verlustrisiko theoretisch <b>unbegrenzt</b> ist – der Kurs kann beliebig weit steigen.",
     "risiko naked"),

    ("Risikomanagement",
     "Was solltest du vor dem Einsatz von echtem Geld tun?",
     "Zuerst <b>Paper Trading</b> (dt. Demokonto / Übungskonto) nutzen und alle Abläufe üben. Fehler kosten dort nichts.",
     "risiko papertrading"),

    ("Risikomanagement",
     "Häufiger Anfängerfehler rund um den <b>Faktor 100</b> (Multiplikator, engl. <i>multiplier</i>)?",
     "Ihn zu vergessen! Immer <b>× 100</b> rechnen: „1,50&nbsp;$ Prämie“ = 150&nbsp;$, „50&nbsp;$ Strike“ = 5.000&nbsp;$ pro Kontrakt.",
     "risiko fehler faktor100"),

    ("Risikomanagement",
     "Besserer Ansatz als Optionen zu <b>kaufen</b> und auf schnelle Gewinne zu hoffen?",
     "Als Einsteiger lieber <b>verkaufen</b> (Stillhalter) und <b>Theta</b> (Zeitwertverfall, engl. <i>time decay</i>) für sich arbeiten lassen.",
     "risiko fehler"),
]

# ---------------------------------------------------------------------------
# CLOZE-KARTEN:  (Unterdeck, Text mit {{c1::...}}, Extra/Hinweis, Tags)
# ---------------------------------------------------------------------------
cloze = [
    ("Grundlagen",
     "Ein <b>Call</b> (dt. Kaufoption) gibt das Recht, die Aktie zu {{c1::kaufen}}; ein <b>Put</b> (dt. Verkaufsoption) gibt das Recht, die Aktie zu {{c2::verkaufen}}.",
     "", "cloze grundlagen"),

    ("Grundlagen",
     "1 Optionskontrakt (engl. <i>contract</i>) = {{c1::100}} Aktien. Eine Prämie (engl. <i>premium</i>) von 1,50&nbsp;$ entspricht also {{c2::150&nbsp;$}} pro Kontrakt.",
     "", "cloze grundlagen kontrakt"),

    ("Grundlagen",
     "Der Käufer (engl. <i>buyer</i>) einer Option hat ein {{c1::Recht}}, der Verkäufer/Stillhalter (engl. <i>seller/writer</i>) hat eine {{c2::Pflicht}}.",
     "engl.: right vs. obligation.", "cloze positionen"),

    ("Preis & Griechen",
     "Prämie = {{c1::Innerer Wert}} + {{c2::Zeitwert}}.",
     "engl.: intrinsic value + time value. Der Zeitwert schmilzt bis zum Verfall auf null.", "cloze preis"),

    ("Preis & Griechen",
     "{{c1::Delta}} misst die Preisänderung pro 1&nbsp;$ Kursbewegung. {{c2::Theta}} misst den täglichen Zeitwertverlust (engl. <i>time decay</i>). {{c3::Vega}} misst die Reaktion auf Volatilität (engl. <i>volatility</i>).",
     "", "cloze griechen"),

    ("Preis & Griechen",
     "Hohe implizite Volatilität (IV, engl. <i>implied volatility</i>) führt zu {{c1::hohen}} Prämien – für den Verkäufer {{c2::gut}}.",
     "", "cloze volatilitaet"),

    ("Strategien",
     "Beim <b>Cash-Secured Put</b> gilt: Breakeven (dt. Gewinnschwelle) = {{c1::Strike − Prämie}}, maximaler Gewinn (engl. <i>max profit</i>) = {{c2::die Prämie}}.",
     "Beispiel: Strike 50 $, Prämie 1,50 $ → Breakeven 48,50 $.", "cloze strategien csp"),

    ("Strategien",
     "Beim <b>Covered Call</b> (dt. gedeckter Call) ist der Gewinn nach oben {{c1::gedeckelt}}, weil du die Aktien zum {{c2::Strike}} verkaufen musst.",
     "engl.: der Gewinn ist „capped“.", "cloze strategien covered-call"),

    ("Strategien",
     "Der Kreislauf aus Cash-Secured Put und Covered Call heißt {{c1::The Wheel}}; die kassierten Prämien (engl. <i>premiums</i>) nennt man die {{c2::zweite Dividende}}.",
     "", "cloze strategien wheel"),

    ("IBKR-Umsetzung",
     "Bei Optionen immer {{c1::Limit}}-Orders nutzen, nie {{c2::Market}}-Orders – wegen der breiten Geld-Brief-Spanne (engl. <i>bid-ask spread</i>).",
     "", "cloze ibkr order"),

    ("Verfall & Andienung",
     "Läuft die Option <b>OTM</b> aus, {{c1::verfällt sie wertlos}} und die Prämie ist Gewinn. Läuft sie <b>ITM</b> aus, wirst du {{c2::angedient}}.",
     "engl.: OTM → expires worthless; ITM → you get assigned.", "cloze verfall"),

    ("Risikomanagement",
     "Verkaufe Puts nur auf Aktien, die du {{c1::wirklich besitzen willst}}, und halte die Positionsgröße (engl. <i>position size</i>) {{c2::klein}}.",
     "", "cloze risiko"),
]

# ---------------------------------------------------------------------------
# DIAGRAMM-KARTEN:  (Unterdeck, Vorderseite, Bilddatei, Erklärung/Zusatz, Tags)
# ---------------------------------------------------------------------------
diagram = [
    ("Grundlagen",
     "Welche Option kaufst du, je nach Markterwartung (steigend/fallend)?",
     "01_call_put_entscheidung.png",
     "Steigende Kurse erwartet (engl. <i>bullish</i>) → <b>Call</b> (Recht zu kaufen).<br>Fallende Kurse erwartet (engl. <i>bearish</i>) → <b>Put</b> (Recht zu verkaufen).",
     "diagramm grundlagen call put"),

    ("Käufer & Verkäufer",
     "Wie sehen die <b>vier Grundpositionen</b> eines Optionsgeschäfts aus?",
     "02_vier_grundpositionen.png",
     "Käufer (Long): <b>Long Call</b> / <b>Long Put</b>.<br>Verkäufer (Short): <b>Short Call</b> / <b>Short Put</b>.<br>Käufer hat das Recht (engl. <i>right</i>), Verkäufer die Pflicht (engl. <i>obligation</i>).",
     "diagramm positionen"),

    ("Preis & Griechen",
     "Woraus setzt sich der <b>Optionspreis</b> zusammen?",
     "03_preis_bausteine.png",
     "Prämie = <b>Innerer Wert</b> (engl. <i>intrinsic value</i>; Abstand Kurs–Strike, nur ITM) + <b>Zeitwert</b> (engl. <i>time value</i>; Restlaufzeit → Theta, IV → Vega, Zins → Rho).",
     "diagramm preis"),

    ("Strategien",
     "Wie läuft ein <b>Cash-Secured Put</b> ab (beide Ausgänge)?",
     "04_cash_secured_put.png",
     "Kurs über Strike → Put verfällt wertlos, Prämie bleibt.<br>Kurs unter Strike → Andienung (engl. <i>assignment</i>), du kaufst die Aktien zum Wunschpreis (Einstand sinkt um die Prämie).",
     "diagramm strategien csp"),

    ("Strategien",
     "Wie läuft ein <b>Covered Call</b> ab (beide Ausgänge)?",
     "05_covered_call.png",
     "Kurs unter Strike → Call verfällt wertlos, du behältst Aktien + Prämie.<br>Kurs über Strike → Aktien werden zum Strike verkauft, Gewinn nach oben gedeckelt (engl. <i>capped</i>).",
     "diagramm strategien covered-call"),

    ("Strategien",
     "Wie funktioniert der Kreislauf <b>„The Wheel“</b>?",
     "06_the_wheel.png",
     "1) Cash-Secured Put verkaufen → bei Andienung Aktien im Depot.<br>2) Covered Call verkaufen → bei Andienung Aktien verkauft → zurück zu 1.<br>In jeder Runde Prämien kassieren.",
     "diagramm strategien wheel"),

    ("IBKR-Umsetzung",
     "Welchen <b>Kontotyp</b> (engl. <i>account type</i>) wählst du bei IBKR – und warum?",
     "07_kontotyp.png",
     "<b>Cash-Konto:</b> nur eigenes Geld, konservativ.<br><b>Margin-Konto:</b> nötig für die meisten Optionsstrategien (z.&nbsp;B. Puts verkaufen), aber mehr Risiko.",
     "diagramm ibkr konto"),

    ("IBKR-Umsetzung",
     "Wie gibst du bei IBKR Schritt für Schritt eine <b>Option-Order</b> auf?",
     "08_order_ablauf.png",
     "Basiswert (engl. <i>underlying</i>) → Optionskette (engl. <i>option chain</i>) → Verfall (30–45 Tage) → Strike (z.&nbsp;B. Delta ~0,30) → Sell → <b>Limit</b>-Order nahe Mid → prüfen (×100!) → Transmit.",
     "diagramm ibkr order"),

    ("Verfall & Andienung",
     "Wie läuft <b>Ausübung und Andienung</b> ab?",
     "09_andienung_sequence.png",
     "Käufer übt aus (engl. <i>exercise</i>) → Clearingstelle (engl. <i>clearing house</i>, OCC) teilt dem Stillhalter die Pflicht zu (engl. <i>assignment</i>) → Stillhalter liefert/kauft 100 Aktien zum Strike. Die Prämie bleibt dem Stillhalter.",
     "diagramm verfall andienung"),

    ("Risikomanagement",
     "Was sind die Säulen des <b>Risikomanagements</b> (engl. <i>risk management</i>)?",
     "10_risikomanagement.png",
     "Positionsgröße klein (engl. <i>position sizing</i>) · Diversifikation · nur Wunsch-Aktien · Timing bei hoher Volatilität · Gewinne früh mitnehmen (z.&nbsp;B. 50&nbsp;%).",
     "diagramm risiko"),
]

# ---------------------------------------------------------------------------
# VOKABEL-KARTEN (DE ⇄ EN):  (Unterdeck, Text mit {{c1::...}}, Hinweis, Tags)
# Deutscher Begriff sichtbar, englischer Fachbegriff als Lücke -> aktives
# Abrufen der englischen Vokabel.
# ---------------------------------------------------------------------------
VOKABEL_DECK = "Fachbegriffe (DE ⇄ EN)"
vokabeln = [
    (VOKABEL_DECK, "<b>Basiswert</b> → auf Englisch: {{c1::Underlying}}",
     "Der Wert, auf den sich die Option bezieht (z.&nbsp;B. eine Aktie).", "vokabel"),
    (VOKABEL_DECK, "<b>Aktie</b> → auf Englisch: {{c1::Stock}} (auch: Share)",
     "Ein einzelner Anteil an einer Firma.", "vokabel"),
    (VOKABEL_DECK, "<b>Ausübungspreis / Basispreis</b> → auf Englisch: {{c1::Strike (Price)}}",
     "Fester Preis für Kauf oder Verkauf der Aktie.", "vokabel"),
    (VOKABEL_DECK, "<b>Prämie</b> → auf Englisch: {{c1::Premium}}",
     "Der Preis der Option selbst.", "vokabel"),
    (VOKABEL_DECK, "<b>Kaufoption</b> → auf Englisch: {{c1::Call}}",
     "Recht, die Aktie zu kaufen.", "vokabel"),
    (VOKABEL_DECK, "<b>Verkaufsoption</b> → auf Englisch: {{c1::Put}}",
     "Recht, die Aktie zu verkaufen.", "vokabel"),
    (VOKABEL_DECK, "<b>Verkäufer / Stillhalter</b> → auf Englisch: {{c1::Seller / Writer}}",
     "Hat die Pflicht und kassiert die Prämie.", "vokabel"),
    (VOKABEL_DECK, "<b>Ausübung</b> → auf Englisch: {{c1::Exercise}}",
     "Der Käufer nutzt sein Recht.", "vokabel"),
    (VOKABEL_DECK, "<b>Andienung</b> → auf Englisch: {{c1::Assignment}}",
     "Dem Verkäufer wird die Pflicht zugeteilt.", "vokabel"),
    (VOKABEL_DECK, "<b>innerer Wert</b> → auf Englisch: {{c1::Intrinsic Value}}",
     "Der Teil der Prämie, der schon echtes Geld wert ist (nur ITM).", "vokabel"),
    (VOKABEL_DECK, "<b>Zeitwert</b> → auf Englisch: {{c1::Time Value}} (Extrinsic Value)",
     "Aufschlag für Restzeit &amp; Unsicherheit; schmilzt auf null.", "vokabel"),
    (VOKABEL_DECK, "<b>Zeitwertverfall</b> → auf Englisch: {{c1::Time Decay}}",
     "Täglicher Wertverlust der Option (Theta).", "vokabel"),
    (VOKABEL_DECK, "<b>implizite Volatilität</b> → auf Englisch: {{c1::Implied Volatility}} (IV)",
     "Vom Markt erwartete Schwankungsbreite.", "vokabel"),
    (VOKABEL_DECK, "<b>Verfall / Verfallstag</b> → auf Englisch: {{c1::Expiration}} (Expiry)",
     "Letzter Gültigkeitstag der Option.", "vokabel"),
    (VOKABEL_DECK, "<b>Restlaufzeit</b> → auf Englisch: {{c1::Days to Expiration (DTE)}}",
     "Verbleibende Tage bis zum Verfall.", "vokabel"),
    (VOKABEL_DECK, "<b>im Geld</b> → auf Englisch: {{c1::In The Money (ITM)}}",
     "Option hat inneren Wert.", "vokabel"),
    (VOKABEL_DECK, "<b>am Geld</b> → auf Englisch: {{c1::At The Money (ATM)}}",
     "Kurs ≈ Strike.", "vokabel"),
    (VOKABEL_DECK, "<b>aus dem Geld</b> → auf Englisch: {{c1::Out of The Money (OTM)}}",
     "Kein innerer Wert – nur Zeitwert.", "vokabel"),
    (VOKABEL_DECK, "<b>Geld-Brief-Spanne</b> → auf Englisch: {{c1::Bid-Ask Spread}}",
     "Abstand zwischen Bid (Geld) und Ask (Brief).", "vokabel"),
    (VOKABEL_DECK, "<b>Optionskette</b> → auf Englisch: {{c1::Option Chain}}",
     "Übersicht aller Strikes und Verfallstermine.", "vokabel"),
    (VOKABEL_DECK, "<b>gedeckelt (nach oben begrenzt)</b> → auf Englisch: {{c1::capped}}",
     "Z.&nbsp;B. der Gewinn beim Covered Call.", "vokabel"),
    (VOKABEL_DECK, "<b>eine Position rollen</b> → auf Englisch: {{c1::Rolling}}",
     "Alte Option zurückkaufen, neue mit späterem Verfall verkaufen.", "vokabel"),
    (VOKABEL_DECK, "<b>Gebühr</b> → auf Englisch: {{c1::Commission}} (Fee)",
     "Kosten pro Kontrakt bzw. pro Order.", "vokabel"),
    (VOKABEL_DECK, "<b>Konto (Depot)</b> → auf Englisch: {{c1::Account}}",
     "Cash-Konto oder Margin-Konto.", "vokabel"),
]


def esc(s: str) -> str:
    # In TSV dürfen keine Tabs/Newlines im Feld sein; wir nutzen <br> für Zeilen.
    return s.replace("\t", " ").replace("\n", "<br>")


def write_tsv(path, header_lines, rows):
    with open(path, "w", encoding="utf-8") as f:
        for h in header_lines:
            f.write(h + "\n")
        for row in rows:
            f.write("\t".join(esc(c) for c in row) + "\n")
    print(f"{os.path.basename(path)}: {len(rows)} Karten")


def main():
    out = os.path.join(HERE)
    os.makedirs(out, exist_ok=True)

    # BASIC: Spalten = Deck, Front, Back, Tags
    basic_rows = [(f"{DECK}::{d}", front, back, tags) for (d, front, back, tags) in basic]
    write_tsv(
        os.path.join(out, "optionen_basic.tsv"),
        ["#separator:tab", "#html:true", "#notetype:Basic",
         "#deck column:1", "#tags column:4"],
        basic_rows,
    )

    # CLOZE: Spalten = Deck, Text, Extra, Tags
    cloze_rows = [(f"{DECK}::{d}", text, extra, tags) for (d, text, extra, tags) in cloze]
    write_tsv(
        os.path.join(out, "optionen_cloze.tsv"),
        ["#separator:tab", "#html:true", "#notetype:Cloze",
         "#deck column:1", "#tags column:4"],
        cloze_rows,
    )

    # DIAGRAMM: Basic-Notetype. Front = Frage, Back = Bild + Erklärung.
    diagram_rows = []
    for (d, front, img, extra, tags) in diagram:
        back = f'<img src="{img}"><br><br>{extra}'
        diagram_rows.append((f"{DECK}::{d}", front, back, tags))
    write_tsv(
        os.path.join(out, "optionen_diagramme.tsv"),
        ["#separator:tab", "#html:true", "#notetype:Basic",
         "#deck column:1", "#tags column:4"],
        diagram_rows,
    )

    # VOKABELN: Cloze-Notetype. Deutscher Begriff sichtbar, englischer als Lücke.
    vokabel_rows = [(f"{DECK}::{d}", text, extra, tags) for (d, text, extra, tags) in vokabeln]
    write_tsv(
        os.path.join(out, "optionen_vokabeln.tsv"),
        ["#separator:tab", "#html:true", "#notetype:Cloze",
         "#deck column:1", "#tags column:4"],
        vokabel_rows,
    )

    total = len(basic_rows) + len(cloze_rows) + len(diagram_rows) + len(vokabel_rows)
    print(f"\nGesamt: {total} Karten "
          f"({len(basic_rows)} Basic, {len(cloze_rows)} Cloze, "
          f"{len(diagram_rows)} Diagramm, {len(vokabel_rows)} Vokabeln)")


if __name__ == "__main__":
    main()
