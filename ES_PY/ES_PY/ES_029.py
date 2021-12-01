"""Utilizza le list comprehension per generare la tavola pitagorica."""
num = 0
i = 0
table = [num*i for num in range(1,11) for i in range(1,11)]
print(table)
