lista = ['Juan', 'Maria', 'Ana', 'Ricardo', 'Carlos']
for nombre in lista:
    numero_nombre = lista.index(nombre) + 1
    print(f"Nombre {numero_nombre}: {nombre}")

for nombre in lista:
    if nombre.lower().startswith('c'):
        print(nombre)
    else:
        print("Nombre que no comienza con c")

numeros = [1, 2, 3, 4, 5]
mi_valor = 0
for numero in numeros:
    mi_valor += numero
print(mi_valor)

palabra = 'python'
for letra in palabra:
    print(letra)

for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)
dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for a, b in dic.items():
    print(f"{a}: {b}")