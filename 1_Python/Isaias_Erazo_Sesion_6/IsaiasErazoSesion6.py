#Ejercicios

#1 (Los Dos Puntos)
if 10 :
  print("Numero esigual a 10")

#2 (Asignar variable)
numero = 2
if numero < 10:
  print("Numero es menos que 10")

#3 (Se agrego Else)
numero = 8
if numero > 5:
  print("El numero es mayo que 5")
else:
  print("El numero es menor que 5")

#4 (Se agrego Else)
numero = 3
if numero % 2 == 0 :
  print("Numeor es par")
else:
  print("Numero es impar")

#5 (Igual al 4)
numero = 3
if numero % 2 == 0 :
  print("Numeor es par")
else:
  print("Numero es impar")

#6 (el simbolo de diferente se cambio por igual)
valor = "Python"
if valor != "python" :
  print("El valor es python")

#7 (El tipo de dato de edad)
edad = 18
if edad == 18 :
  print("Tienes 18 años")
else:
  print("Tienes otra cosa")

#8 (mayor que por menor que)
if numero < 5:
  print("El numero es mayor que 5")
print('\n')

#Ciclo While == hacer mientras  (Condicion)
flag = 4
while flag < 5:
  print(flag)
  flag = flag + 1

while flag < 5:
  print(flag)
  flag += 1
else :
  print(f"El valor de flag es: {flag}")

#Ejercicio
flag = 4
numero = int(input("Digita el numero para Adivinar: "))
while numero != flag:
  numero = int(input("Intenta de nuevo: "))
else:
  print("Felicidades Adivinaste")

i    = 1
suma = 0
while i <= 4 :
  suma += i
  i    += 1
print(f"Lasuma de los numero es {suma}")

#Calcular el factorial de un Numero
n         = 7                                          #Numero que necesito factorial
factorial = 1
contador  = 1
while contador <= n:
    factorial *= contador
    contador += 1
print(f"El factorial del numer {n} es: {factorial}")

#Condicion Break
flag = 0
while flag < 100:
  print(flag)
  flag += 1
if flag == 34 :
    print("Valor de break" , flag)

print("\n")

# //////////////////////////  Aplicacion de Conocimiento  /////////////////////////

suma = 0
while True:
    numero = int(input("Ingrese un número entero (ingrese un número negativo para salir): "))
    
    if numero < 0:
        break  
    
    suma += numero

print(f"La suma de los números ingresados es: {suma}")