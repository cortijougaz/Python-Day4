numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        continue
    numero -= 1

monedas = 5
billetes = 0

while monedas > 0:
    print(f"Tengo {monedas} monedas.")
    monedas -= 1
    if monedas == 0:
        break
else:
    print("Me quedé misio.")


while True:
    print(f"Billete: {billetes}.")
    if billetes == 0:
        break
    billetes -= 1



nombre = input("Ingrese su nombre: ")
for letra in nombre:
    if letra.lower() == 'r':
        break
    if letra.lower() == 'c':
        continue
    print(letra)

respueta = 'a'
print("Antes del while")
while respueta == 's':
    pass
print("Después del while")