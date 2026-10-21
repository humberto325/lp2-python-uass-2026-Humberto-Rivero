# ===================== FUNCIONES =====================

# ------- Ejercicio 1: Estadisticas de una lista -------
# Crear una funcion estadisticas(numeros) que reciba una lista de numeros
# y retorne el valor maximo, el valor minimo y el promedio.

def estadisticas(numeros):
    mayor = max(numeros)
    menor = min(numeros)
    promedio = sum(numeros) / len(numeros)
    return mayor, menor, promedio


numeros = [10, 20, 30, 40, 50]
mayor, menor, promedio = estadisticas(numeros)
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
print(f"Promedio: {promedio}")


# ------- Ejercicio 2: Buscar un elemento -------
# Crear una funcion buscar(lista, valor) que retorne True si el valor
# existe en la lista y False si no existe.

def buscar(lista, valor):
    return valor in lista


alumnos = ["Ana", "Luis", "Carlos"]
print(buscar(alumnos, "Luis"))


# ------- Ejercicio 3: Eliminar duplicados -------
# Crear una funcion eliminar_duplicados(lista) que reciba una lista y
# retorne una coleccion sin elementos repetidos utilizando un set.

def eliminar_duplicados(lista):
    return set(lista)


print(eliminar_duplicados([1, 2, 2, 3, 3, 3, 4]))


# ------- Ejercicio 4: Frecuencia de elementos -------
# Crear una funcion contar_frecuencia(lista) que retorne un diccionario
# indicando cuantas veces aparece cada elemento.

def contar_frecuencia(lista):
    frecuencia = {}
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
    return frecuencia


print(contar_frecuencia(["a", "b", "a", "c", "a", "b"]))


# ------- Ejercicio 5: Promedio de notas -------
# Crear calcular_promedio(notas) que retorne el promedio.
# Crear estado(promedio) que indique "Aprobado" o "Reprobado" (>= 60).

def calcular_promedio(notas):
    return sum(notas) / len(notas)


def estado(promedio):
    if promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"


notas = [70, 80, 90, 60]
promedio_notas = calcular_promedio(notas)
print(f"Promedio: {promedio_notas}")
print(f"Estado: {estado(promedio_notas)}")


# ------- Ejercicio 6: Agenda telefonica -------
# Usar un diccionario para almacenar contactos, con funciones para
# agregar, buscar y mostrar contactos, mediante un menu.

agenda = {
    "Juan": "098111111",
    "Ana": "098222222"
}


def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    agenda[nombre] = telefono


def buscar_contacto():
    nombre = input("Nombre a buscar: ")
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else:
        print("Contacto no encontrado")


def mostrar_contactos():
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")


while True:
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos")
    print("4. Salir")
    opcion = input("Elija una opcion: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        mostrar_contactos()
    elif opcion == "4":
        break
    else:
        print("Opcion invalida")


# ------- Ejercicio 7: Producto mas caro -------
# Crear producto_mas_caro(productos) que retorne nombre y precio
# del producto mas caro de una lista de tuplas.

def producto_mas_caro(productos):
    nombre_mas_caro, precio_mas_caro = productos[0]
    for nombre, precio in productos:
        if precio > precio_mas_caro:
            nombre_mas_caro = nombre
            precio_mas_caro = precio
    return nombre_mas_caro, precio_mas_caro


productos = [
    ("Teclado", 150000),
    ("Mouse", 80000),
    ("Monitor", 1200000)
]
nombre, precio = producto_mas_caro(productos)
print(f"Producto: {nombre}")
print(f"Precio: {precio}")


# ------- Ejercicio 8: Inventario de productos -------
# Usar un diccionario de inventario con funciones para agregar stock,
# vender producto y consultar stock, mediante un menu.

inventario = {
    "Teclado": 10,
    "Mouse": 5,
    "Monitor": 2
}


def agregar_stock():
    producto = input("Producto: ")
    cantidad = int(input("Cantidad a agregar: "))
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad


def vender_producto():
    producto = input("Producto: ")
    cantidad = int(input("Cantidad a vender: "))
    if producto in inventario and inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
    else:
        print("Stock insuficiente o producto inexistente")


def consultar_stock():
    producto = input("Producto: ")
    if producto in inventario:
        print(f"Stock de {producto}: {inventario[producto]}")
    else:
        print("Producto no encontrado")


while True:
    print("1. Agregar stock")
    print("2. Vender producto")
    print("3. Consultar stock")
    print("4. Salir")
    opcion = input("Elija una opcion: ")

    if opcion == "1":
        agregar_stock()
    elif opcion == "2":
        vender_producto()
    elif opcion == "3":
        consultar_stock()
    elif opcion == "4":
        break
    else:
        print("Opcion invalida")


# ------- Ejercicio 9: Ranking de alumnos -------
# Con una lista de tuplas (nombre, nota), crear funciones para obtener
# el mejor alumno, el peor alumno y el promedio general.

alumnos_notas = [
    ("Juan", 85),
    ("Ana", 95),
    ("Pedro", 70)
]


def mejor_alumno(alumnos):
    mejor_nombre, mejor_nota = alumnos[0]
    for nombre, nota in alumnos:
        if nota > mejor_nota:
            mejor_nombre = nombre
            mejor_nota = nota
    return mejor_nombre, mejor_nota


def peor_alumno(alumnos):
    peor_nombre, peor_nota = alumnos[0]
    for nombre, nota in alumnos:
        if nota < peor_nota:
            peor_nombre = nombre
            peor_nota = nota
    return peor_nombre, peor_nota


def promedio_general(alumnos):
    suma = 0
    for nombre, nota in alumnos:
        suma += nota
    return suma / len(alumnos)


nombre, nota = mejor_alumno(alumnos_notas)
print(f"Mejor alumno: {nombre} ({nota})")

nombre, nota = peor_alumno(alumnos_notas)
print(f"Peor alumno: {nombre} ({nota})")

print(f"Promedio general: {round(promedio_general(alumnos_notas), 2)}")


# ------- Ejercicio 10: Sistema de gestion de estudiantes -------
# Usar un diccionario {nombre: [notas]} con funciones para agregar
# estudiante, calcular promedios, mostrarlos y ver el mejor, con menu.

estudiantes = {
    "Juan": [70, 80, 90],
    "Ana": [100, 95, 90]
}


def agregar_estudiante():
    nombre = input("Nombre del estudiante: ")
    cantidad = int(input("Cantidad de notas a ingresar: "))
    notas = []
    for i in range(cantidad):
        nota = float(input(f"Nota {i + 1}: "))
        notas.append(nota)
    estudiantes[nombre] = notas


def promedio_estudiante(notas):
    return sum(notas) / len(notas)


def mostrar_promedios():
    for nombre, notas in estudiantes.items():
        print(f"{nombre}: {promedio_estudiante(notas)}")


def mejor_estudiante():
    mejor_nombre = None
    mejor_promedio = -1
    for nombre, notas in estudiantes.items():
        promedio = promedio_estudiante(notas)
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_nombre = nombre
    print(f"Mejor estudiante: {mejor_nombre} ({mejor_promedio})")


while True:
    print("1. Agregar estudiante")
    print("2. Mostrar promedios")
    print("3. Mostrar mejor estudiante")
    print("4. Salir")
    opcion = input("Elija una opcion: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_promedios()
    elif opcion == "3":
        mejor_estudiante()
    elif opcion == "4":
        break
    else:
        print("Opcion invalida")


# ------- Desafio Extra: Sistema de votacion -------
# Registrar votos por candidato en un diccionario. Mostrar cantidad de
# votos por candidato, el candidato ganador y el total de votos.

votos_por_candidato = {}


def registrar_voto():
    candidato = input("Ingrese el candidato por el que vota: ")
    if candidato in votos_por_candidato:
        votos_por_candidato[candidato] += 1
    else:
        votos_por_candidato[candidato] = 1


while True:
    continuar = input("¿Desea registrar un voto? (s/n): ")
    if continuar.lower() != "s":
        break
    registrar_voto()

total_votos = 0
ganador = None
votos_ganador = -1

for candidato, votos in votos_por_candidato.items():
    print(f"{candidato}: {votos} votos")
    total_votos += votos
    if votos > votos_ganador:
        votos_ganador = votos
        ganador = candidato

print(f"Candidato ganador: {ganador}")
print(f"Total de votos registrados: {total_votos}")
