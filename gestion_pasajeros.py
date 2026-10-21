print("-------Bienvenidos a la gestion de pasajeros de Humberto Rivero-----------")

#Cargamos los  datos del pasajero usando una funcion
def Agregar_pasajeros(Pasajeros):
    Nombre = input("Nombre del pasajero: ")
    Dni = int(input("Ingrese el Dni del pasajero: "))
    Destino = input("Ingrese el destino del pasajero: ")

    pasajero = (Nombre, Dni, Destino)
    Pasajeros.append(pasajero)
    print("Pasajero agregado correctamente")


#Cargamos una ciudad y su pais usando una funcion
def Agregar_ciudad(Ciudades):
    Ciudad = input("Ingrese el nombre de la ciudad: ")
    Pais = input("Ingrese el pais al que pertenece: ")

    ciudad_pais = (Ciudad, Pais)
    Ciudades.append(ciudad_pais)
    print("Ciudad agregada correctamente")


#Buscamos a que ciudad viaja un pasajero segun su Dni
def Buscar_ciudad_por_dni(Pasajeros):
    Dni = int(input("Ingrese el Dni del pasajero: "))

    for Nombre, dni_pasajero, Destino in Pasajeros:
        if dni_pasajero == Dni:
            print(f"El pasajero {Nombre} viaja a {Destino}")
            return

    print("No se encontro un pasajero con ese Dni")


#Contamos cuantos pasajeros viajan a una ciudad
def Contar_pasajeros_por_ciudad(Pasajeros):
    Ciudad = input("Ingrese el nombre de la ciudad: ")
    contador = 0

    for Nombre, Dni, Destino in Pasajeros:
        if Destino == Ciudad:
            contador += 1

    print(f"Cantidad de pasajeros que viajan a {Ciudad}: {contador}")


#Buscamos a que pais viaja un pasajero segun su Dni, usando la ciudad de destino
def Buscar_pais_por_dni(Pasajeros, Ciudades):
    Dni = int(input("Ingrese el Dni del pasajero: "))
    Destino_pasajero = None

    for Nombre, dni_pasajero, Destino in Pasajeros:
        if dni_pasajero == Dni:
            Destino_pasajero = Destino

    if Destino_pasajero is None:
        print("No se encontro un pasajero con ese Dni")
        return

    for Ciudad, Pais in Ciudades:
        if Ciudad == Destino_pasajero:
            print(f"El pasajero viaja a {Pais}")
            return

    print("No se encontro el pais de esa ciudad")


#Contamos cuantos pasajeros viajan a un pais
def Contar_pasajeros_por_pais(Pasajeros, Ciudades):
    Pais = input("Ingrese el nombre del pais: ")
    contador = 0

    for Nombre, Dni, Destino in Pasajeros:
        for Ciudad, pais_ciudad in Ciudades:
            if Ciudad == Destino and pais_ciudad == Pais:
                contador += 1

    print(f"Cantidad de pasajeros que viajan a {Pais}: {contador}")


Pasajeros = [
    ("Manuel Juarez", 19823451, "Liverpool"),
    ("Silvana Paredes", 22709128, "Buenos Aires"),
    ("Rosa Ortiz", 15123978, "Glasgow"),
    ("Luciana Hernandez", 38981374, "Lisboa")
]

Ciudades = [
    ("Buenos Aires", "Argentina"),
    ("Glasgow", "Escocia"),
    ("Lisboa", "Portugal"),
    ("Liverpool", "Inglaterra"),
    ("Madrid", "España")
]

while True:
    print("1. Agregar pasajeros a la lista de viajeros")
    print("2. Agregar ciudades a la lista de ciudades")
    print("3. Ver a que ciudad viaja un pasajero (por Dni)")
    print("4. Ver cantidad de pasajeros que viajan a una ciudad")
    print("5. Ver a que pais viaja un pasajero (por Dni)")
    print("6. Ver cantidad de pasajeros que viajan a un pais")
    print("7. Salir")

    Opcion = input("Elija una opcion: ")

    if Opcion == "1":
        Agregar_pasajeros(Pasajeros)
    elif Opcion == "2":
        Agregar_ciudad(Ciudades)
    elif Opcion == "3":
        Buscar_ciudad_por_dni(Pasajeros)
    elif Opcion == "4":
        Contar_pasajeros_por_ciudad(Pasajeros)
    elif Opcion == "5":
        Buscar_pais_por_dni(Pasajeros, Ciudades)
    elif Opcion == "6":
        Contar_pasajeros_por_pais(Pasajeros, Ciudades)
    elif Opcion == "7":
        break
    else:
        print("Opcion invalida")
