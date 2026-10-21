# Ejercicio 5: Copiar "origen.txt" hacia "destino.txt" usando dos with anidados.

with open("origen.txt", "r", encoding="utf-8") as origen:
    with open("destino.txt", "w", encoding="utf-8") as destino:
        for linea in origen:
            destino.write(linea)

print("Archivo copiado correctamente a destino.txt")
