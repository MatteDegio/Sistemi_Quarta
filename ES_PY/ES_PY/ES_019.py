print("0 = Somma, 1 = Sottrazione, 2 = Moltiplicazione, 3 = divisione")
n1 = int(input("Inserisci un numero: "))
n2 = int(input("Inserisci un numero: "))
x = int(input("quale operazione vuoi usare: "))

if x == 0:
    ris  = n1 + n2
    print(f"il risultato è = {ris}")

elif x == 1:
    ris = n1 - n2
    print(f"il risultato è = {ris}")

elif x == 2:
    ris = n1 * n2
    print(f"il risultato è = {ris}")

elif x == 3: 
    ris = n1 / n2
    print(f"il risultato è = {ris}")

else: print("Questa operazione non esiste.")


