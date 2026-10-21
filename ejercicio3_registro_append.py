# Ejercicio 3: Agregar nombre y edad al final de "registro.txt" sin borrar lo existente.

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

with open("registro.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{nombre} - {edad}\n")

print("Datos agregados a registro.txt")
