x = int(input("Inserisci un numero: "))

y = int(input("Inserisci un numero: "))

l = []
l.append((x**2) + (y**2))
l.append(((x + y)**2))
l.append((x**2) - (y**2))
l.append((x - y)**2)

print(l)