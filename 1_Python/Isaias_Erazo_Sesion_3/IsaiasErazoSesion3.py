#Inicio de Clase - Tipos de Variables

#Repaso - Ejercicio 1
NombreUsuario = "Isaias Alexander Erazo Martinez"
print (f" !Hola, {NombreUsuario} ! Bienvenido a Nuestro Programa.")
print (" !Hola," , NombreUsuario,"! Bienvenido a Nuestro Programa.")
print (" !Hola, %s! Bienvenido a Nuestro Programa."%(NombreUsuario))
print('\n')

# Ejercicio 2
Base = 5
Altura = 7
areaTriangulo = Base*Altura/2
print("El Area de tu triangulo es:", (Base*Altura)/2)    #Un decimal
print("El area del triaungulo es: %.2f"%(areaTriangulo)) #Dos decimales
print('\n')

#Ejercicio 3
nombreUsuario    = "Isaias Erazo" 
edadUsuario      = "23"
ciudadResidencia = "Ilopango"
print(f"{nombreUsuario},{edadUsuario},{ciudadResidencia}")
print('\n')

#Tipos de Variables - (Type - identificar variables/clase)
x = 1               # int - entero
y = 1.45654         # float - decimales
z = 2j              # complex - numero con incognita
print(type(x), type(y), type(z))
print('\n')

# Practica en Clase, (Clases de Variables)
print(type(1))                                #int     - Numero Entero
print(type(3.14))                             #float   - Numero Decimal
print(type(1 + 8j))                           #complex - Numero Cientifico
print(type("Hello World,"))                   #str     - Texto
print(type([1, 2, 3]))                        #list    - Lista Numeros o Textos
print(type({1: "one", 2: "two", 3: "three"})) #dict    - Estructura Pares clave y Valor
print(type({1, 2, 3}))                        #set     - Estructuara Elementos Unicos
print(type((1, 2, 3)))                        #tuple   - Lista Inmutable
print('\n')

# Receso - Conversion de Datos Numericos
X = 1
Y = 2.8
Z = 3j
convertX = float(X)
convertY = complex(Y)
#convertZ = no es posible convertir un numero complejo a uno normal.
print(type(convertX),type(convertY))
print('\n')

edadUsuario = int(23)       # Ojo int del principio (declaro la clase, demanera logica)
print(type(edadUsuario))    #Conversion de Srt -> Int
print("La edad es:", edadUsuario)
print('\n')

#Ejercios:

#1
mensaje = "Bienvenido a Python"
print(mensaje)
print('\n')

#2
poema = """
¿Qué es poesía?, dices mientras clavas
en mi pupila tu pupila azul.
¿Qué es poesía? ¿Y tú me lo preguntas?
Poesía... eres tú
"""
print(poema)
print('\n')

#3
cadena = "programacion en python"
lenguaje = cadena[-6:] # o tambien [16:22]
print(lenguaje)
print('\n')
#4
cadena = "abcdefghijk"
subCadena = cadena[2:6] # o tambien [-9:-5]
print(subCadena)
print('\n')
#5
Cadena = "python es genial"
parte = Cadena[-9:] # o tambien [6:16]
print(parte)
print('\n')

#Cadenas
#Convertir todo en Mayuscula
a = "Hola Mundo"
print(a.upper())
#Convertir todo en Minuscula
print(a.lower())
#Eliminar espacios en Blanco
A = "   Hola Mundo   hola"
print(A)
print(A.strip())
#Reemplazar Cadena
print(a.replace("H", "F"))
#Cadena Dividida
print(a.split())
print('\n')

# ////////////////////////////Aplicacion de Conocimiento //////////////////////////

#1
Frase = """Programacion es arte y ciencia, un lenguaje que crea la relaidad, una forma de dar vida a la inteligencia, y al mundo digital una identidad"""
print(Frase.split())
print('\n')

#2
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
primeras = abecedario[:10]
ultimas = abecedario[-10:]
alreves = abecedario [::-1]
print("Las Primeras 10 letras del Abecedario Son:", primeras)
print("Las Ultimas 10 Letras del Abecedario Son:", ultimas)
print("El Abecedario al reves es:", alreves)
