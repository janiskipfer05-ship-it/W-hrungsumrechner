import tkinter as tk
import Numpy as np

root = tk.Tk()

auswahl = tk.StringVar()
auswahl.set("Option 1")  # Standardwert

dropdown = tk.OptionMenu(root, auswahl, "Option 1", "Option 2", "Option 3")
dropdown.pack()

def anzeigen():
    print(auswahl.get())

button = tk.Button(root, text="Auswahl anzeigen", command=anzeigen)
button.pack()

root.mainloop()



def umrechnen(Von, betrag, Zu):
    basevon =     
    basezu = 
    
    inCHF = betrag / basevon
    ergebniss = inCHF * basezu
    
    return ergebniss