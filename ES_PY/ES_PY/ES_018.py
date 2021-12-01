"""Scrivi un programma in Python che permetta all’utente di inserire un numero intero e una stringa:
concatena la stringa con sé stessa tante volte quante il numero e stampa il risultato."""

n = int (input("Inserisci un numero qualsiasi: "))
parola = input("Inserisci un parola qualsiasi: ")

parola = parola * n

print(parola)
