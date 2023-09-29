#Sentencias
#If (Verificar el numero dado)
numero = int(input("inserte el numero a verificar"))
if numero % 2 == 0 :
    print(f" El numero es Par: {numero}")

#If (Verificar una contraseña)
contraseña = input("Ingrese la contraseña: ")
if contraseña == "1" :
    print("Contraseña correcta")

#If , Elif , Else (Condiciones, pasos para llegar a un fin)
x = 3
y = 7
if x > y :
    print(f"El numero mayor es x = {x}")
elif x == y :
    print(f"Los numero son iguales ")
else:
    print(f"El numero mayor es y = {y}")
print('\n')

#Practica
X , Y = 5 , -6
numero = X + Y
if numero > 0 :
    print(f"El numero es Positivo {numero}")
elif numero < 0 :
    print(f"El numero es Negativo {numero}")
else:
    print(f"El numero es Igual a Cero {numero}")
print('\n')

numero = float(input("Ingrese un numero"))
if numero > 0:
    print("El numero es POSITIVO")
elif numero < 0:
    print("El numero es NEGATIVO")
else:
    print("Numero es igual a cero")
print('\n')

#En una sola linea
#If (Se ejecutara siempre y cuando sea verdadero(True))
a , b = 2 , 3 
if a > b : print("a is great b")
#elif (Esta se ejecutara despues de un If o antes de un Else (false))
elif a < b : print("a is not great b")
#Else (Se ejecuta por defecto cuando no se completa nuinguna condicion (None))
A = -3
print("a es Positivo") if A > 0 else print("A es Negativo")
print('\n')

#Imprimir el mayor de los numero a o b
a = 5
b = 4
print("El mayor es A") if a > b else print("El mayor es B") if a == b else print("Son Iguale")

#Un numero es par o no
numero = 6
print(f"El numero {numero} es PAR") if numero % 2 == 0 else print(f"El numero {numero} es IMPAR")
n1 = 3
print('el numero es par') if n1 % 2 == 0 else print('el numero es impar')
print('\n')

#Calcular el descuento de una compra
valorCompra = 46
if valorCompra >= 100 :
    descuento = 0.15
    precioFinal = valorCompra - valorCompra * descuento
    print(f"El precio final es: {precioFinal}")
else:
    descuento = 0.10
    precioFinal = valorCompra - valorCompra * descuento
    print(f"El precio final es: {precioFinal}")
print('\n')
descuento = 0.20 if valorCompra >= 100 else 0.5 ; precioFinal = valorCompra - valorCompra*descuento
print(f"El precio final es: {precioFinal}")
print('\n')

#Calculo del salario de un empleado
ingreso = 8700
impuesto = 0.30 if ingreso > 10000 else 0.20 if ingreso > 5000 else 0.10
impuestoApagar = ingreso * impuesto
salario = ingreso - impuestoApagar
print(f"El salario del empleado es: {salario}")
print('\n')

#If operador logico And (Ambas condiciones deben ser verdaderas)
a = 32
b = 33
c = 500
if a > b and c > a :
    print("Ambas condiciones son verdaderas")
else:
    print("Una condicion es falsa")
print('\n')
#Juegos Mecanicos Apto o no
edad = 20
estatura = 165
if edad >= 18 and estatura >= 160:
    print("Puedes subir al Juego Mecanico")
else :
    print("No Puedes subir al Juego Mecanico")
print('\n')
#Pago y menbresia validos
pago      = True
menbresia = True
acceso_a_contenido = menbresia and pago
if acceso_a_contenido:
    print("Bienvenido")
else:
    print("Pago o Membresia Invalida")
print('\n')

#Calculo nota final (Rango de numero de 0 a 10)
nota = 7
if nota >= 0 and nota <=10:
    print("Nota Valida")
elif nota == 0:
    print("Nota es 0")
else:
    print("Nota invalida")
print('\n')


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
