# Ejercicio 2: Leer "productos.txt" y mostrar cada linea sin saltos sobrantes.

with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())
