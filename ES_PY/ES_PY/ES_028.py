"""Genera una lista contenente i quadrati perfetti dispari minori di 1000. """
import math

lista = []
quadrato_perfetto = [numero for numero in range(1001) if math.sqrt(numero) % 1 == 0]
lista.append(quadrato_perfetto)
print(lista)