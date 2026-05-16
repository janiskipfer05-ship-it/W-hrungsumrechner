import tkinter as tk
# import Numpy as np  # aktuell nicht verwendet

# --------------------------------------------------------------------
# Wechselkurse-Dictionary (Basis: CHF = 1.00)
# Jeder Wert sagt: wie viel 1 Einheit dieser Währung in CHF wert ist
# --------------------------------------------------------------------
wechselkurse = {
    "CHF": 1.00,
    "USD": 1.28,
    "EUR": 1.09,
    "TRY": 57.69,
    "NOK": 11.80,
    "COP": 4726.54
}

# --------------------------------------------------------------------
# Hauptfenster erstellen
# --------------------------------------------------------------------
root = tk.Tk()
root.title("Währungsumrechner")


# --------------------------------------------------------------------
# "Von Währung" Auswahl (Dropdown)
# --------------------------------------------------------------------
label_von = tk.Label(root, text="Von Währung")
label_von.pack()

auswahl1 = tk.StringVar()
auswahl1.set("USD")  # Standardwert

dropdown1 = tk.OptionMenu(
    root,
    auswahl1,
    "CHF", "USD", "EUR", "TRY", "NOK", "COP"
)
dropdown1.pack()


# --------------------------------------------------------------------
# "Zu Währung" Auswahl (Dropdown)
# --------------------------------------------------------------------
label_zu = tk.Label(root, text="Zu Währung")
label_zu.pack()

auswahl2 = tk.StringVar()
auswahl2.set("CHF")  # Standardwert

dropdown2 = tk.OptionMenu(
    root,
    auswahl2,
    "CHF", "USD", "EUR", "TRY", "NOK", "COP"
)
dropdown2.pack()


# --------------------------------------------------------------------
# Eingabefeld für Betrag
# --------------------------------------------------------------------
label_betrag = tk.Label(root, text="Betrag")
label_betrag.pack()

eingabe = tk.Entry(root)
eingabe.insert(0, "123")  # Standardwert im Feld
eingabe.pack()


# --------------------------------------------------------------------
# Label für Kursanzeige (zeigt aktuelle Wechselkurse)
# --------------------------------------------------------------------
kurs_label = tk.Label(root, text="")
kurs_label.pack()


def update_kurs(*args):
    # Holt aktuelle Auswahl aus beiden Dropdowns
    kursvon = wechselkurse[auswahl1.get()]
    kurszu = wechselkurse[auswahl2.get()]

    # Zeigt beide Kurse im Label an
    kurs_label.config(
        text=f"{auswahl1.get()}: {kursvon}   |   {auswahl2.get()}: {kurszu}"
    )


# Wenn sich Dropdown ändert → Kurs aktualisieren
auswahl1.trace_add("write", update_kurs)
auswahl2.trace_add("write", update_kurs)

update_kurs()  # einmal direkt beim Start ausführen


# --------------------------------------------------------------------
# Label für Ergebnisanzeige
# --------------------------------------------------------------------
ergebnis_label = tk.Label(root, text="Ergebniss")
ergebnis_label.pack()


# --------------------------------------------------------------------
# Umrechnungsfunktion (wird beim Button gedrückt)
# --------------------------------------------------------------------
def klick1():

    # Betrag aus Eingabefeld holen (String → float)
    betrag = float(eingabe.get())

    # Wechselkurse holen
    basevon = wechselkurse[auswahl1.get()]
    basezu = wechselkurse[auswahl2.get()]

    # Umrechnung über CHF als Basis
    inCHF = betrag / basevon
    ergebniss = inCHF * basezu

    # Ergebnis anzeigen
    ergebnis_label.config(text=ergebniss)


# Button zum Auslösen der Umrechnung
button1 = tk.Button(root, text="Umrechnen", command=klick1)
button1.pack()


# --------------------------------------------------------------------
# Fehleranzeige Label
# --------------------------------------------------------------------
Fehler_label = tk.Label(root, text="")
Fehler_label.pack()


def fehler_pruefen(*args):

    # Versuch: Eingabe in Zahl umwandeln
    try:
        betrag = float(eingabe.get())
    except:
        Fehler_label.config(text="Fehler: Ungültige Eingabe")
        return

    # Fehler 1: gleiche Währungen
    if auswahl1.get() == auswahl2.get():
        Fehler_label.config(text="Fehler: Identische Währungen")

    # Fehler 2: negativer Betrag
    elif betrag < 0:
        Fehler_label.config(text="Fehler: Negative Zahl")

    # kein Fehler
    else:
        Fehler_label.config(text="")


# Funktion wird automatisch bei Änderungen ausgeführt
auswahl1.trace_add("write", fehler_pruefen)
auswahl2.trace_add("write", fehler_pruefen)
eingabe.bind("<KeyRelease>", fehler_pruefen)

fehler_pruefen()  # einmal beim Start prüfen


# --------------------------------------------------------------------
# Start der GUI
# --------------------------------------------------------------------
root.mainloop()