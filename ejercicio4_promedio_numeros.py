# Ejercicio 4: Leer "numeros.txt" (un numero por linea), calcular el promedio
# y guardarlo en "resultado.txt".

numeros = []

with open("numeros.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        numeros.append(float(linea.strip()))

promedio = sum(numeros) / len(numeros)

with open("resultado.txt", "w", encoding="utf-8") as archivo:
    archivo.write(f"Promedio: {promedio}\n")

print(f"Promedio calculado: {promedio}")
