"""Scrivi un programma in Python che permetta all’utente di inserire 
il suo nome (tramite input) e stampi il nome in cui tutti i caratteri 
tranne il primo sono sostituiti da un *. """

nome = input("Inserisci un Nome: ")
temp = len(nome) - 1
print(nome[:1], end="")
k = 0
while k < temp:
    print("*", end="")
    k = k + 1

