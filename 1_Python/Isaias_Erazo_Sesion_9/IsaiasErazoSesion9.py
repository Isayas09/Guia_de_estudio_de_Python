#Modulo (Conjunto de funciones)
import math 
raiz = math.sqrt(4)
print('La raiz cuadrada es: ', raiz)

print(math.log10(20))



#Llamar modulos
from math import e, sqrt
from statistics import *
ages = [30, 25, 40, 20, 26]
print(stdev(ages))

from random import random, randint
print(random ())

from Modulos import suma 
print(suma(4,5))

from Modulos import resta
print(resta(5,7))

from Modulos import division
print(division(24,3))

print('\n')
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
