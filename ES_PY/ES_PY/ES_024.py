lista = []
def nPrimi(num):
    k = 2
    continua = True
    while continua == True and k < num:          
        if num % k == 0:
            continua = False
        k = k + 1

    return continua

contNPrimi = 0

for i in range(1000):
    nPrimi(i)
    if nPrimi(i) == True:
        contNPrimi += 1
print(f"I numeri primi prima di 1000 sono {contNPrimi}")
