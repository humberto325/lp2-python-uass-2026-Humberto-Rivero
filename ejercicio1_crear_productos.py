# Ejercicio 1: Crear "productos.txt" y guardar nombre y precio de 5 productos.

with open("productos.txt", "w", encoding="utf-8") as archivo:
    for i in range(5):
        nombre = input(f"Ingrese el nombre del producto {i + 1}: ")
        precio = input(f"Ingrese el precio del producto {i + 1}: ")
        archivo.write(f"{nombre} - {precio}\n")

print("Archivo productos.txt creado correctamente.")
