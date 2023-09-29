#Ejemplo 1: Funciones
def my_function():
    print("Hola Mundo desde una funcion")
    print("****************************")
miFuncion = my_function
print("Esta es: ", miFuncion())

def saludar():
    print("Hola muy Buenos Dias")
saludos = saludar
print("Me gusta saludar", saludos())

def saludar(nombre) :
    print(f'Hola muy buenos dias', nombre)
saludar('Juan')
#igual numero de parametros y argumentos
def sumar (x,y):                      #Estos son parametros
    suma = x + y
    return suma
resultado = sumar(4,5)                #Estos son argumentos
print("La suma es: ", resultado)

def areaRectangulo(base, altura):                      #Estos son parametros
    return base * altura
area = areaRectangulo(4,5)                             #Estos son argumentos
print('el area de un rectangulo', area)
print('\n')

#Ejemplo 2: Funcion para imprimir una lista
def imprimirLista(lista):
    for it in lista:
        print(it)
list1 = [1, 2, 'hola']
imprimirLista(list1)
print('\n')

#Ejemplo 3: Funcion para verificar si un numero es par
def es_par (numero):
    if numero % 2 == 0:
        return True
    else:
        False
num = 4

if es_par(num):
    print('El numero es par')
else:
    print('El numero es impar')
print('\n')

#Ejemplo 4: Funcion que regresa una lista de numeros pares
def lista_pares (n):
    listPares = []
    for it in range(n+1):
        if it % 2 == 0:
            listPares.append(it)
    return listPares
print(lista_pares(20))
print('\n')

#Ejemplo 5:Argumentos arbitrarios

def sumar(*notas):
    totalNotas = 0
    for notas in notas:
        totalNotas += int(notas)
        promedio = totalNotas/notas
    return promedio
notas = [6, 7, 8, 9, 6, 9, 8, 10]
promedioFinal = sumar(*notas)
print(promedioFinal)

def concatenar(*args):
    resultado = " ".join(args)
    return resultado
frutas = 'Guineo', 'Naranja', 'Limon'
MixFrutas = concatenar(*frutas)
print("Mix de frutas: ", MixFrutas)

def mediaArimetica(*args):
    total = sum(args)
    cantidad = len(args)
    media = total/cantidad
    return media
notass = [6, 7, 8, 9, 6, 9, 8, 10]
promedioFinal = mediaArimetica(*notass)
print('El promedio es: ',round(promedioFinal, 1))

def producto(*args):
    productos = 1
    for it in args:
      productos *= it
    return productos
numeros = [1, 3, 4, 5, 6, 7]
totalMultiplicacion = producto(*numeros)
print('El total es: ', totalMultiplicacion)
#Argumentos de palabras arbitrarias **kwargs
def crear_perfil(**kwargs):
    perfil = {}
    for clave, valor in kwargs.items():
        #    'key'    :  'value'
        perfil[clave] = valor
    return perfil

usuario = crear_perfil(nombre="Ana", edad=28, ciudad="Barcelona")
print("Perfil de usuario:", usuario)
#Recursividad
def factorial(n):
    print(" ->>",n)
    if n == 0:
        return 1  # Caso base: factorial de 0 es 1
    else:
        print('else se llama ella misma')
        return n * factorial(n - 1)  # Caso recursivo

numero = 3
resultado = factorial(numero)

print(f"El factorial de {numero} es {resultado}")
def suma_sin_recursividad(n):
    suma = 0
    for it in range(1, n + 1):
        suma += it
    return suma
def suma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + suma_recursiva(n - 1)
n = 4
print(f'Lasuma es : {suma_sin_recursividad(n)}')    
print(f'Lasuma es : {suma_recursiva (n)}')

#Lambda
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
f = lambda x : x**2 + 2*x +3
f(3)

#Filtrar listas funcion Lambda
id_empleados = [341, 45, 435, 676, 344, 346, 676, 365, 122, 234]
pares = filter(lambda x: x%2 == 0, id_empleados)
print(list(pares))

# //////////////////////////  Aplicacion de Conocimiento  /////////////////////////

#1
def suma(a, b):
    return a + b

y = int(input("Primer dato a Sumar: "))
z = int(input("Segundo dato a Sumar: "))

resultado = suma(y, z)
print(f"El resultado es: {resultado} ")


#2
def area_triangulo(a, b):
    return (a * b) / 2

y = int(input("Dime la Base del triangulo: "))
z = int(input("Dime la altura del triangulo: "))

resultado = area_triangulo(y, z)
print(f"El area del triangulo es: {resultado} ")


#3
def celcius_a_fahrenheit(c):
    return (9/5 * c) + 32

print("Bienbenido este es un conversor de grados celcius a fahrenheit \n")
c = int(input("Escribe los grados celcius a convertir: "))


fahrenheit = celcius_a_fahrenheit(c)
print(f"{c} Grados celcius = {fahrenheit} Grados fahrenheit ")

