# //////////////////////////  Aplicacion de Conocimiento  /////////////////////////

#El numero es par y entero positivo, impar y entero positivo, cero o negativo
valor = 56
if valor > 0 and valor % 2 == 0:
    print("Es un numero par positivo")
elif valor > 0 and valor % 2 != 0 :
    print("Es un numero impar positivo")
elif valor == 0:
    print("El numero es 0")
else:
    print("Elnumero es negativo")
print('\n')

#If Operador logico Or (Una condicion debe ser cierta)
if a > b or a > c:
    print("Una condicion es verdadera")
else:
    print("Ninguna es Verdadera")
print('\n')

#verificar el año bisiesto
year = 2000
yearBisiesto = True if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else False
print(yearBisiesto)
print('\n')

#Triangulo, Equilatero (3 lados iguales) Isoceles (2 lados iguales) Escaleno (0)
lado1 = 4
lado2 = 4
lado3 = 4
if lado1 == lado2 == lado3:
    print("Triangulo Equilatro")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triangulo Isoceles")
else:
    print("Triangulo Escaleno")
print('\n')

#if operador logico Not
a = 33
b = 200
if not a > b:
    print("a es mayor que b")
if a < b:
    print("a es mayor que b")
    print('\n')

#Sentencia If anidados
a = 10
if a > 0:
    if a % 2 == 0:
        print("Es par y positico")
    else:
        print("impar y positivo")
elif a == 0:
    print("El numero es 0")
else:
    print("es negativo")
print('\n')

#Validacion de un ticket
validacionEntrada = False
validacionPelicula = True
if validacionEntrada and validacionPelicula:
    print("Tienes derecho al descuento del parqueo")
else:
    print("te toca pagar las 4 horas de paqueo")
print('\n')

#Declaracio Pass (No hace nada, actua como marcador de posicion)
condicionPrincipal = True
condicionAlternativa = True
if condicionPrincipal:
    pass
elif condicionAlternativa:
    pass
else:
    pass
print('\n')

#Practica
mi_edad = int(input('Ingresa mi edad: '))
tu_edad = int(input("Ingresa tu edad"))
if mi_edad > tu_edad:
    resultado = mi_edad-tu_edad
    print(f'tengo {resultado} años mas que tu')
    if mi_edad != tu_edad + 1:
        print('tienes un año mas que yo')
elif mi_edad < tu_edad:
    resultado = tu_edad - mi_edad
    print(f'tu tienes {resultado} años mas que yo')
else:
    print('Tenemos la misma edad')