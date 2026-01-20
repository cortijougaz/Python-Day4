import random

# randint(): Genera un entero entre 1 y 5 (ambos inclusive).
entero_aleatorio = random.randint(1, 5)
print(f"randint(1, 5): {entero_aleatorio}")

# uniform(): Genera un flotante entre 1 y 5.
# Lo redondeamos a 2 decimales para mayor claridad.
flotante_aleatorio = round(random.uniform(1, 5), 2)
print(f"uniform(1, 5) (redondeado): {flotante_aleatorio}")

# random(): Genera un flotante entre 0.0 y 1.0.
flotante_base = random.random()
print(f"random(): {flotante_base}")

# choice(): Elige un elemento al azar de una secuencia.
colores = ['azul', 'rojo', 'verde', 'amarillo']
color_elegido = random.choice(colores)
print(f"choice(['azul', ...]): {color_elegido}")

# shuffle(): Mezcla una secuencia en su lugar (in-place).
# La función modifica la lista directamente y no devuelve nada (retorna None).
numeros = list(range(5,50,5))
print(f"Lista original: {numeros}")
random.shuffle(numeros)
print(f"shuffle(lista): {numeros}")