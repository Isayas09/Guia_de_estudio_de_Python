##Operaciones Arimeticas
# Suma
a = 5  # a , b = 5 , 3
b = 3
c = a + b
print(c)
# Resta
c = a - b
print(c)
c = b - a
print(c)
# Multiplicacion
c = a * b
print(c)
# Divicion         (Division Normal, Calculadora)
c = a / b
print(c)
# Divicion Entera  (El entero de la division)
c = a // b
print(c)
# Modulo           (El Residuo de la Division)
c = a % b
print(c)
# Potenciacion      (Exponentes)
c = a**b
print(c)
print("\n")

##Combinacines de Operadores Arimeticos (Practica) (Uso de Agrupaciones)

A = (4 + 6) * 2
print(A)

B = 10**2 / 5  # Division da Numero Flotante
print(B)

C = (15 - 3) * 4 / 2
print(C)

D = (27 % 5) + 10
print(D)

E = 19 // 3 - 2
print(E)

F = ((5 + 2) * 3) ** 2 / (10 % 3)
print(F)

X = 4
G = (2 * X) + (3 * X) - (5 / X)
print(G)
print("\n")

# Operadores de Asignacion (Practica)
# Ejercicio 1
precioOriginal = 165  # Variable de Entrada
porcentajeDescuento = 40  # Variable de Entrada
descuento = precioOriginal * (porcentajeDescuento / 100)  # Variable de Proceso
precioFinal = precioOriginal - descuento  # Variable de Salida
print(precioFinal)
print("\n")

# Operadores Logicos (El uso de parentesis es para un orden de Operacion)
# Ejemplo de And (Dos condiciones Ciertas para ser Cierto)
x = 10
y = 17
z = 40
print(x < y and y < z)  # True
print(x < y and y > z)  # False
print(x > y and y < z)  # False
print("\n")

# Ejemplo de Or (Almenos una condicion Cierta para ser Cierto)
print(x < y or y < z)  # True
print(x > y or y < z)  # True
print(x > y or y > z)  # False
print("\n")

# Ejemplo de Not (Invierte Respuesta)
print(not x < y)  # False (Cuando enrealidad deberia ser True)
print(x < y)  # True
print(not x > y)  # True (Cuando enrealidad deberia ser False)
print(x > y)  # False
print("\n")

# Operadores de Identidad (is y is not)
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)  # True
print(x is not z)  # True
print("\n")

# Practica
# Ejercicio 1
precioOriginal = 165  # Variable de Entrada
porcentajeDescuento = 40  # Variable de Entrada
descuento = precioOriginal * (porcentajeDescuento / 100)  # Variable de Proceso
precioFinal = precioOriginal - descuento  # Variable de Salida
print(precioFinal)
print("\n")

# Ejercicio 2
inf_positivo = float("inf")
Peso = 60
Estatura = 1.73
Calculo = Peso / (Estatura) ** 2
print("Tu IMC es:", round(Calculo, 2))
if Calculo < 18.5:
    print("Tienes un nivel de peso = Bajo")
if Calculo > 18.5 and Calculo < 24.9:
    print("Tienes un nivel de peso = Normal")
if Calculo > 25.0 and Calculo < 29.9:
    print("Tienes un nivel de peso = Sobrepeso")
if Calculo > 30 and Calculo < inf_positivo:
    print("Tienes un nivel de peso = Obesidad")
print("\n")

# ////////////////////////////Aplicacion de Conocimiento //////////////////////////

#1
a, b, c = 5, 3, 8
resultado1 = a + (b * c)
resultado2 = (a + b) * c
resultado3 = (a / b) * c
resultado4 = a / (b * c)
resultado5 = (a**b) + c
resultado6 = a ** (b + c)
print("Resultado 1:", resultado1)
print("Resultado 2:", resultado2)
print("Resultado 3:", round(resultado3, 2))  # funcion Round,decimales a mostrar.
print("Resultado 4:", round(resultado4, 2))
print("Resultado 5:", resultado5)
print("Resultado 6:", resultado6)
