palabra = 'python'
lista = [letra for letra in palabra]

print(lista)

lista_numeros = [(n / 2) if (n * 2 > 10) else 'no' for n in range(0, 21, 2) ]
print(lista_numeros)

pies = [10, 20, 30, 40, 50]
metros = [n / 3.281 for n in pies]

print(metros)