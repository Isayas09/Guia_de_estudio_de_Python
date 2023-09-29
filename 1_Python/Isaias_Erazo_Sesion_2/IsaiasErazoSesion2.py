resultado = max( 5, 10, 3, 8)
print(resultado)
resultado = round (3.14159, 2)
print (resultado)
resultado = min(5, 10, 3, 8)
print (resultado)
print('\n')

nombre = "Isaias"
edad = 23
print("Mi nombre es",nombre,"y Mi edad es:",edad)
mensaje = "Buenas Tardes, Soy Isaias y este es un Hola Mundo"
longitud = len(mensaje)
print("La longitud del mensaje es",longitud)
print('\n')

valor = 23
mensaje = "Buenas Tardes, Soy Isaias y este es un Hola Mundo"
print ("El tipo de de dato de la variable valor es:",type(valor))
print ("El tipo de dato de la variable mensaje es",type(mensaje))
cadena = "123"
print ("El tipo de dato de la variable cadena es:",type(cadena))
cadena = int(cadena)
print("El tipo de dato de la variable cadena es:", type(cadena))
print('\n')

valor = 5
if valor > 23:
    print("El numero es mayor que 5")
    if valor % 2 == 5:
        print("El numero es par")
    else:
        print("El numero es impar")
else:
    print("El numero es mayor que 5")
print('\n')


# a las 3:00pm se tomo un descanso

#Veremos la funcion print

x, y, z = "Sandia", 23, "Melocoton"
print(x , y , z)
print('\n')

#Imprimir varias variables en una linea

nombre = "Isaias Erazo"
edad = 23
print ("Mi nombre es",nombre, "y tengo", edad, "años")
print('\n')

valorHora = 17.5
totalHoras = 8
sueldoDiario = valorHora*totalHoras
print("Nombre del Empleado", nombre,'\n' 'El precio por hora trabajada', valorHora,'\n'"y el sueldo diario es:", sueldoDiario,'\n')
print('\n')

#Formato de Cadena F-String

print (f'Mi nombre es {nombre} y tengo {edad} años')
print('\n')

#Imprimir por tipo de Variable (%) [%s = letras][%d = Numero] debo tener cuidado con el orden

nombre = "Isaias"
edad = 23
peso = 150
print("Mi nombre es %s y tengo %d años y peso %d.\n\n"%(nombre, peso, edad))
print('\n')

#Tabulacion en la Impresion

print("Nombre: \n\t Isaias \n Edad \n\t 23")
print('\n')

# ////////////////////////////Aplicacion de Conocimiento //////////////////////////

print("Tarea\n")
#Variables
Nombres = "Isaias Alexander"
PrimerApellido = "Erazo"
SegundoApellido = "Martinez"
Edad = 23
Nacionalidad = "Salvadoreño"
Sexo = "Masculino"

#Ejemplo 1
print("Información personal:")
print("Nombres:", Nombres)
print("Primer Apellido:", PrimerApellido)
print("Segundo Apellido:", SegundoApellido)
print("Edad:", Edad)
print("Nacionalidad:", Nacionalidad)
print("Sexo:", Sexo)
print("\n")

#Ejemplo 2
print (f"Informacion Personal \nNombre: {Nombres} \nPrimer Apellido: {PrimerApellido} \nSegundo Apellido:{SegundoApellido} \nEdad: {Edad} \nNacionalidad: {Nacionalidad} \nSexo: {Sexo}")

