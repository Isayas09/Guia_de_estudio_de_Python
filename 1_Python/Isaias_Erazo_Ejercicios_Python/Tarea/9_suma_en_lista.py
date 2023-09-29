lista_numeros = []
resultado = 0

while True:
    numeros = int(input("Ingresa los numeros que sumaras (y '00' para terminar): "))

    if numeros == 00:
        break

    lista_numeros.append(numeros)

for numero in lista_numeros:
    resultado += numero
print("La suma de los numeros es:", resultado)
