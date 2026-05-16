import tkinter as tk
# import Numpy as np

wechselkurse = {
    "CHF": 1.00,
    "USD": 1.28,
    "EUR": 1.09,
    "TRY": 57.69,
    "NOK": 11.80,
    "COP": 4726.54
}

root = tk.Tk()
root.title("Währungsumrechner")


# -----------------------------------------------------------------------------
#   Von Währung GUI
#

label_von = tk.Label(root, text="Von Währung")
label_von.pack()

auswahl1 = tk.StringVar()
auswahl1.set("USD")

dropdown1 = tk.OptionMenu(
    root,
    auswahl1,
    "CHF", "USD", "EUR", "TRY", "NOK", "COP"
)
dropdown1.pack()


# -----------------------------------------------------------------------------
#   Zu Währung GUI
#

label_zu = tk.Label(root, text="Zu Währung")
label_zu.pack()

auswahl2 = tk.StringVar()
auswahl2.set("CHF")

dropdown2 = tk.OptionMenu(
    root,
    auswahl2,
    "CHF", "USD", "EUR", "TRY", "NOK", "COP"
)
dropdown2.pack()

# -----------------------------------------------------------------------------
#   Fehlererkennung für die Währungen
#

if (auswahl1.get() == auswahl2.get()):
    fehler = True
    grund = "Identische Wärungen"
    
else :
    fehler = False

# -----------------------------------------------------------------------------
#   Eingabefeld
#

label_betrag = tk.Label(root, text="Betrag")
label_betrag.pack()

eingabe = tk.Entry(root)
eingabe.insert(0, "123")
eingabe.pack()


# -----------------------------------------------------------------------------
#   Fehlererkennung für Negativer Betrag
#
# grund = " "
betrag = float(eingabe.get())

if betrag < 0:
    fehler = True
    grund = "Negative Zahl"

else:
    fehler = False

# -----------------------------------------------------------------------------
#   Kurs anzeigen
#

kurs_label = tk.Label(root, text="")
kurs_label.pack()


def update_kurs(*args):

    kursvon = wechselkurse[auswahl1.get()]
    kurszu = wechselkurse[auswahl2.get()]

    kurs_label.config(text=f"{auswahl1.get()}: {kursvon}   |   {auswahl2.get()}: {kurszu}"
    )


auswahl1.trace_add("write", update_kurs)
auswahl2.trace_add("write", update_kurs)

update_kurs()


# -----------------------------------------------------------------------------
#   Ergebniss anzeigen
#

ergebnis_label = tk.Label(root, text="Ergebniss")
ergebnis_label.pack()


# -----------------------------------------------------------------------------
#   Umrechnen
#

def klick1():

    betrag = float(eingabe.get())

    basevon = wechselkurse[auswahl1.get()]
    basezu = wechselkurse[auswahl2.get()]

    inCHF = betrag / basevon
    ergebniss = inCHF * basezu

    ergebnis_label.config(text=ergebniss)


button1 = tk.Button(root, text="Umrechnen", command=klick1)
button1.pack()

# -----------------------------------------------------------------------------
#   Fehler anzeigen
#

Fehler_label = tk.Label(root, text="")
Fehler_label.pack()

def fehler_pruefen(*args):

    try:
        betrag = float(eingabe.get())
    except:
        Fehler_label.config(text="Fehler: Ungültige Eingabe")
        return

    if auswahl1.get() == auswahl2.get():
        Fehler_label.config(text="Fehler: Identische Währungen")

    elif betrag < 0:
        Fehler_label.config(text="Fehler: Negative Zahl")

    else:
        Fehler_label.config(text="")
        
auswahl1.trace_add("write", fehler_pruefen)
auswahl2.trace_add("write", fehler_pruefen)

eingabe.bind("<KeyRelease>", fehler_pruefen)

fehler_pruefen()
        

root.mainloop()