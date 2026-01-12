nombres = ['Ana', 'Hugo', 'Maria']
edades = [65, 29, 42, 2]
ciudades = ['Lima', 'Madrid', 'Mexico']

combinados = list(zip(nombres, edades, ciudades))
for nombre, edad, ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')