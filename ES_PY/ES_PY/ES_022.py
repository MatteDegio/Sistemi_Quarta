maxEl = int(input("Inserisci il numero di numeri da inserire: "))
lista = []
cont = 0

while(cont < maxEl):
    num = float(input(f"Inserisci il numero: "))
    lista.append(num)
    cont = cont + 1
print(lista)

max = lista[0]
min = lista[0]

for maxEl in lista:
    if max < maxEl:
        max = maxEl
    
    if min >  maxEl:
        min = maxEl

print(f"Il massimo è {max}.")
print(f"Il minimo è {min}.")