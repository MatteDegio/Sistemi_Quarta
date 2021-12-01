""" Data una lista di stringhe estrai da essa la lista di stringhe che sono palindrome e la lista di stringhe che hanno iniziale maiuscola."""
lista = ["ciao", "Matteo", "anna", "Marco", "simo"]
listaPal = []
listaMaiusc = []
n = 0
for i in lista:
    s = lista[i]
    if s[0] == s[-1]:
        listaPal.append(s)
    if s[0] >= 'A':
        if s[0] <= 'Z':
            listaMaiusc.append(s)
print(listaPal)
print(listaMaiusc)