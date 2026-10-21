# EJERCICIOS DE BUCLES - FOR Y WHILE

# ===================== BUCLES FOR =====================

# Ejercicio 1: Contador ascendente
# Solicita un numero entero positivo e imprime del 1 hasta ese numero con un for.

n = int(input("Ingrese un numero entero positivo: "))

for i in range(1, n + 1):
    print(i)


# Ejercicio 2: Suma de numeros naturales
# Solicita un numero N y calcula la suma de todos los numeros desde 1 hasta N.

n = int(input("Ingrese un numero entero positivo: "))
suma = 0

for i in range(1, n + 1):
    suma += i

print(f"La suma es: {suma}")


# Ejercicio 3: Tabla de multiplicar
# Solicita un numero e imprime su tabla de multiplicar del 1 al 10.

n = int(input("Ingrese un numero entero: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# Ejercicio 4: Contador de vocales
# Solicita una palabra o frase e indica cuantas vocales contiene.

texto = input("Ingrese una palabra o frase: ")
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
contador_vocales = 0

for letra in texto:
    if letra in vocales:
        contador_vocales += 1

print(f"Cantidad de vocales: {contador_vocales}")


# Ejercicio 5: Triangulo de asteriscos
# Solicita un numero positivo y genera un triangulo de asteriscos.

n = int(input("Ingrese un numero entero positivo: "))

for i in range(1, n + 1):
    print("*" * i)


# ===================== BUCLES WHILE =====================

# Ejercicio 1: Contador ascendente
# Solicita un numero entero positivo e imprime del 1 hasta ese numero con un while.

n = int(input("Ingrese un numero entero positivo: "))
i = 1

while i <= n:
    print(i)
    i += 1


# Ejercicio 2: Suma acumulada
# Solicita numeros y acumula la suma. Finaliza cuando se ingresa 0.

suma = 0

while True:
    numero = int(input("Ingrese un numero (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print(f"Suma total: {suma}")


# Ejercicio 3: Validacion de contraseña
# Solicita una contraseña hasta que sea "python123".

contrasena = input("Ingrese la contraseña: ")

while contrasena != "python123":
    contrasena = input("Contraseña incorrecta, intente de nuevo: ")

print("Acceso concedido")


# Ejercicio 4: Control de asistencia
# Solicita la cantidad de estudiantes presentes por clase. Finaliza con -1.

total_asistencias = 0
cantidad_clases = 0

while True:
    asistencia = int(input("Ingrese la cantidad de estudiantes presentes (-1 para terminar): "))
    if asistencia == -1:
        break
    total_asistencias += asistencia
    cantidad_clases += 1

print(f"Total de asistencias: {total_asistencias}")
print(f"Cantidad de clases: {cantidad_clases}")

if cantidad_clases > 0:
    promedio = total_asistencias / cantidad_clases
    print(f"Promedio de asistencia: {promedio}")


# Ejercicio 5: Caja registradora
# Solicita el precio de productos comprados. Finaliza con 0.

cantidad_productos = 0
monto_total = 0

while True:
    precio = float(input("Ingrese el precio del producto (0 para terminar): "))
    if precio == 0:
        break
    monto_total += precio
    cantidad_productos += 1

print(f"Productos comprados: {cantidad_productos}")
print(f"Total a pagar: {monto_total}")
