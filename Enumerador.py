lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice, item)
    indice = indice + 1

for item in enumerate(lista):
    print(item[0], item[1])

for item in enumerate(range(1,10)):
    print(item)

mis_tuples = list(enumerate(lista))
print(mis_tuples[0][1])