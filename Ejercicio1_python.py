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

print("--------------Bienvenido a la tienda Humberto Rivero calculemos su descuento --------------")

monto = float(input("Ingrese el monto de su compra: "))

if monto > 500000:
    descuento = monto * 0.20 
elif monto > 200000:
    descuento = monto * 0.10
else:
    print("no hay descuento aplicable para ese monto ingresado")

Total_pago = monto - descuento

print(f"Monto original:{(int(monto))}")
print(f"Descuento aplicado:{(int(descuento))}")
print(f"El total a pagar  con el descuento aplicado es:{(int(Total_pago))}")    



