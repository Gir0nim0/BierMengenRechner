from tkinter import *

def buttonBerechnenClick():
    # Übernahme der Daten
    klein = int(entryFlascheKlein.get())
    mittel = int(entryFlascheMittel.get())
    gross = int(entryFlascheGross.get())

    # Verarbeitung der Daten
    LiterWert = (klein * 0.33) + (mittel * 0.5) + (gross * 0.75)
    LiterWert = round(LiterWert, 2)
    # Anzeige der Daten
    labelLiterWert.config(text = LiterWert)

# Löschen des Eingabefelds beim anklicken mit der linken Maustaste
def loeschen_entryFlascheKlein(event):
    entryFlascheKlein.delete(0, END)

def loeschen_entryFlascheMittel(event):
    entryFlascheMittel.delete(0, END)

def loeschen_entryFlascheGross(event):
    entryFlascheGross.delete(0, END)

# Fenster
tkFenster = Tk()
tkFenster.title('BierMengenRechner')
tkFenster.geometry('250x250')

# Label mit Aufschrift 0,33L Flaschen
labelFlascheKlein = Label(master=tkFenster, text='Wieviele 0,33L Flaschen?')
labelFlascheKlein.place(x=30, y=24, width=130, height=27)

# Label mit Aufschrift 0,5L Flaschen
labelFlascheMittel = Label(master=tkFenster, text='Wieviele 0,5L Flaschen?')
labelFlascheMittel.place(x=30, y=64, width=130, height=27)

# Label mit Aufschrift 0,75L Flaschen
labelFlascheGross = Label(master=tkFenster, text='Wieviele 0,75L Flaschen?')
labelFlascheGross.place(x=30, y=104, width=130, height=27)

# Entry für 0,33L Flaschen
entryFlascheKlein = Entry(master=tkFenster, bg='white')
entryFlascheKlein.place(x=164, y=24, width=40, height=27)
entryFlascheKlein.insert(0,'0')
entryFlascheKlein.bind('<Button-1>', loeschen_entryFlascheKlein)

# Entry für 0,5L Flaschen
entryFlascheMittel = Entry(master=tkFenster, bg='white')
entryFlascheMittel.place(x=164, y=64, width=40, height=27)
entryFlascheMittel.insert(0,'0')
entryFlascheMittel.bind('<Button-1>', loeschen_entryFlascheMittel)

# Entry für 0,75L Flaschen
entryFlascheGross = Entry(master=tkFenster, bg='white')
entryFlascheGross.place(x=164, y=104, width=40, height=27)
entryFlascheGross.insert(0,'0')
entryFlascheGross.bind('<Button-1>', loeschen_entryFlascheGross)

# Button zum Berechnen
buttonBerechnen = Button(master=tkFenster, bg='#e5e5e5', text='Biermenge berechnen', command=buttonBerechnenClick)
buttonBerechnen.place(x=30, y=144, width=130, height=27)

# Label mit Aufschrift Liter
labelLiter = Label(master=tkFenster, text='Liter')
labelLiter.place(x=170, y=144, width=100, height=27)

# Label für den Liter Wert
labelLiterWert = Label(master=tkFenster, text='')
labelLiterWert.place(x=164, y=144, width=40, height=27)

# Label Info

labelInfo = Label(master=tkFenster, anchor=CENTER, wraplength=200, fg="blue", text='Dies ist ein kleines Tool zum berechnen der Biermenge anhand der abgefüllten Flaschen.')
labelInfo.place(x=20, y=190, width=200, height=50)

# Aktivierung des Fensters
tkFenster.mainloop()
