import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1):
    (random.choice(numeros))
adivina = random.choice(numeros)

while True:
    print("Hora de jugar, Adivina el numero del 1 al 10")
    tu_numero = int(input("Escribe tu numero porfavor: "))
    if tu_numero > adivina:
        print("Tu numero es mayor, intenta de nuevo: ")
    elif tu_numero < adivina:
        print("Tu numero es menor, intenta de nuevo: ")

    if tu_numero == adivina:
        print("Felicidades Has Ganado")
        break
