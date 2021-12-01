"""Scrivi un programma in Python che permetta all’utente di inserire le coordinate
di due punti del piano cartesiano. I punti devono essere salvati all’interno di tuple. 
Stampa la distanza euclidea tra i due punti."""

import math

x0 = float (input("Inserisci la coordinata x0: "))
y0 = float (input("Inserisci la coordinata y0: "))
x1 = float (input("Inserisci la coordinata x1: "))
y1 = float (input("Inserisci la coordinata y1: "))

tuple = (x0, x1, y0, y1)

distanza = math.sqrt((tuple[0] - tuple[1])**2 + (tuple[2] - tuple[3])**2)

print(distanza)