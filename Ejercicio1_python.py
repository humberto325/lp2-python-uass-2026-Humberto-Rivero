# TAREA DEL PROFESOR PYTHON EMMM  CONDICIONALES !!!!!!!!
# BUENO UNA PERSONA QUIERE INGRESAR A LA WEB DEL MINISTERIO XD

# SOLICITE AL USUARIO SU EDAD Y SI POSEE DOCUMENTO DE IDENTIDAD
# PERMITIR EL INGRESO SOLO SI TIENE MAS DE 18 Y POSEE DOCUEMTNO DE IDENTIDAD

#EJERCICIO 1

edad = int(input("Ingrese su edad: "))

Documento_identidad = int(input("Ingrese su documento de identidad: "))



#verificamos que la persona cumpla con los requisitos para ingresar a la web del Ministerio
if edad >= 18 and Documento_identidad > 0 and  len((str(Documento_identidad))) == 8:
    print("Bienvenido a la web del Ministerio")

else:
    # 1. Si es menor o igual a 0, mostramos este error y PARAMOS aquí para esa validación
    if Documento_identidad <= 0:
        print("Usted no posee documento de identidad, no puede ingresar a la web del Ministerio")

    # 2. Si es positivo pero la longitud no es 8, mostramos este otro error
    elif len(str(Documento_identidad)) != 8:
        print("Usted no posee un documento de identidad válido, no puede ingresar a la web del Ministerio")

    # 3. La edad se evalua aparte porque es un requisito totalmente distinto
    if edad < 18:
        print("Usted es menor de edad, no puede ingresar a la web del Ministerio")


#Ejercicio 2: Descuento en una tienda
#Solicite el monto de una compra.

#Aplicar los siguientes descuentos:

#20% si supera Gs. 500.000
#10% si supera Gs. 200.000
#Sin descuento en cualquier otro caso
#Mostrar:

#Monto original
#Descuento aplicado
#Total a pagar

monto = float(input("Ingresá el monto de la compra: "))

if monto > 500000:
    descuento = monto * 0.20
    porcentaje = "20%"
elif monto > 200000:
    descuento = monto * 0.10
    porcentaje = "10%"
else:
    descuento = 0
    porcentaje = "0%"

total = monto - descuento

print(f"Monto original: Gs. {monto}")
print(f"Descuento aplicado ({porcentaje}): Gs. {descuento}")
print(f"Total a pagar: Gs. {total}")




#Ejercicio 3 semaforo inteligente
#uso la funcion para que no importe si ingresas un valor en mayusculas o minicuslas
color = input("Ingresá el color del semáforo (Verde, Amarillo, Rojo): ").capitalize()

if color == "Verde":
    print("Acción: Avanzar")
elif color == "Amarillo":
    print("Acción: Reducir velocidad")
elif color == "Rojo":
    print("Acción: Detenerse")
else:
    print("Error: El color ingresado no es válido.")


#Ejercicio 4 Nivel de batería

bateria = int(input("Ingresá el porcentaje de batería del teléfono (0 a 100): "))

if bateria < 0 or bateria > 100:
    print("Error: El porcentaje ingresado no es correcto (debe ser entre 0 y 100).")
elif bateria <= 10:
    print("Nivel de batería: Crítica (0% a 10%)")
elif bateria <= 30:
    print("Nivel de batería: Baja (11% a 30%)")
elif bateria <= 80:
    print("Nivel de batería: Normal (31% a 80%)")
else:
    print("Nivel de batería: Alta (81% a 100%)")



#Ejercicio 5 Evaluación climática
temp = float(input("Ingresá la temperatura actual (°C): "))

if temp < 10:
    print("Clima: Mucho frío (menos de 10°C)")
elif temp <= 24:
    print("Clima: Templado (10°C a 24°C)")
elif temp <= 34:
    print("Clima: Caluroso (25°C a 34°C)")
else:
    print("Clima: Muy caluroso (35°C o más)")
