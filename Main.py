import tkinter as tk
#import Numpy as np

wechselkurse = {
    "CHF": 1.00,
    "USD": 1.28,
    "EUR": 1.09,
    "TRY": 57.69,
    "NOK": 11.80,
    "COP": 4726.54
}

betrag = 0    

root = tk.Tk()        # Hauptfenster erstellen
root.title("Wärungsumrechner")


# -----------------------------------------------------------------------------
#   Von Wärung GUI
#
label = tk.Label(root, text="Von Währung")
label.pack()


auswahl1 = tk.StringVar()
auswahl1.set("USD")  #Strtwährung festlegen

def update_kurs(*args):
    kurs = wechselkurse[auswahl1.get()]
    label.config(text=f"Kurs: {kurs}")

auswahl1.trace_add("write", update_kurs)

dropdown = tk.OptionMenu(root, auswahl1, "CHF", "USD","EUR", "TRY", "NOK", "COP")
dropdown.pack()


# -----------------------------------------------------------------------------
#   ZU Wärung GUI
#
label = tk.Label(root, text="Zu Währung")
label.pack()


auswahl2 = tk.StringVar()
auswahl2.set("CHF")  #Strtwährung festlegen

dropdown = tk.OptionMenu(root, auswahl2, "CHF", "USD","EUR", "TRY", "NOK", "COP")
dropdown.pack()


#------------------------------------------------------------------------------
#   Eingabefeld
#

label = tk.Label(root, text="Betrag")
label.pack()

eingabe = tk.Entry(root)
eingabe.insert(0,"123")
eingabe.pack()


#------------------------------------------------------------------------------
#   Kurs anzeigen
#

label = tk.Label(root, text="")
label.pack()

kursvon = wechselkurse[auswahl1.get()]

label.pack()

kurszu = wechselkurse[auswahl2.get()]

label = tk.Label(root, text=f"Kurs zu CHF: {kurszu} ")
label.pack()


#------------------------------------------------------------------------------
#   Umrechnen
#

def klick1():
    # --- Was Passiert wen gedrückt---
    
    betrag = float(eingabe.get())
    basevon = wechselkurse[auswahl1.get()]  
    basezu = wechselkurse[auswahl2.get()]
    
    inCHF = betrag / basevon
    ergebniss = inCHF * basezu
    label.config(text=ergebniss)
    return

#------------------------------------------------------------------------------
#   Ergebins anzeigen
#

button1 = tk.Button(root, text="Umrechnen", command=klick1)
button1.pack()


label = tk.Label(root, text="Ergebins")
label.pack()



root.mainloop()       # Fenster anzeigen


