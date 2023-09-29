# //////////////////////////  Aplicacion de Conocimiento  /////////////////////////

suma = 0
while True:
    numero = int(input("Ingrese un número entero (ingrese un número negativo para salir): "))
    
    if numero < 0:
        break  
    
    suma += numero

print(f"La suma de los números ingresados es: {suma}")

