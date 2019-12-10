# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:29:02 2019

@author: a1628642
"""

# Zufallsgenerator importieren
import random

# Spiel soll definiert werden, das dem Spiel 'Schere, Stein oder Papier' gleichkommt 
def Spiel():
    # Definieren der Variablen
    Handzeichen = ['Schere', 'Stein', 'Papier']
    Spieler = input('Spiele so lange bis du oder Computer 3-mal gewonnen hat.\nBitte gebe "Schere", "Stein" oder "Papier" oder "exit" um das Spiel zu verlassen an:')
    Computer = random.choice(Handzeichen)

# Die Wahl des Computers soll der Spieler sehen können
    if Computer == Handzeichen[0] :
        print('Computer hat "Schere" gewählt')
    elif Computer == Handzeichen[1] :
        print('Computer hat "Stein" gewählt')
    else:
        print('Computer hat "Papier" gewählt')

#Möglichkeiten wenn Spieler 'Schere' gewählt hat:  
    if Spieler == Handzeichen[0] :
        if Computer == Handzeichen[0] :
            ergebnis = 'Unentschieden'
        elif Computer == Handzeichen[1] :
            ergebnis = 'Verloren'
        else :
            ergebnis = 'Gewonnen'

#Möglichkeiten wenn Spieler 'Stein' gewählt hat:
    elif Spieler == Handzeichen[1] :
        if Computer == Handzeichen[0] :
            ergebnis = 'Gewonnen'
        elif Computer == Handzeichen[1] :
            ergebnis = 'Unentschieden'
        else:
            ergebnis = 'Verloren'
            
# Möglichkeiten wenn Spieler 'Papier' gewählt hat:
    elif Spieler == Handzeichen[2]:
        if Computer == Handzeichen[0] :
            ergebnis = 'Verloren'
        elif Computer == Handzeichen[1] :
            ergebnis = 'Gewonnen'
        else:
            ergebnis = 'Unentschieden'
            
# Wenn Spieler sich vertippt:
    else:
        raise TypeError
    return str(ergebnis)

# Definieren neuer Variablen in Kleinschreibung, weil Spieler und spieler unterschiedliche Variablen sein sollen
spieler = 0
computer = 0

# Bis jemand 3-mal gewonnen hat, soll gespielt werden 
while spieler < 3 and computer < 3 :
    try:
        X = Spiel()
        if X == 'Gewonnen' :
            spieler = spieler + 1 
            print('Gewonnen')
        elif X == 'Verloren' :
            computer = computer + 1
            print('Verloren')
        else:
            print('Unentschieden')
    except TypeError:
        print('Bitte auf Rechtschreibung achten!')

# Gibt den Spieler das Ergebnis aus 
else:
    if spieler == 3 :
        print('Du hast das Spiel gewonnen')
    else: 
        print('Du hast das Spiel verloren')
