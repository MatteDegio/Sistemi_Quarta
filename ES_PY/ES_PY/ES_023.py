numero = int(input("Inserisci un numero per vedere se è primo: "))

def nPrimi(num):
    k = 2
    continua = True
    while continua == True and k < num:          
        if num % k == 0:
            continua = False
        k = k + 1

    return continua

if nPrimi(numero) == True:
    print("Il numero è primo.")
else:
    print("Il numero non è primo")