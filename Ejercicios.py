lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for nombre in enumerate(lista_nombres):
    if nombre[1].startswith("M"):
        print(nombre[0])