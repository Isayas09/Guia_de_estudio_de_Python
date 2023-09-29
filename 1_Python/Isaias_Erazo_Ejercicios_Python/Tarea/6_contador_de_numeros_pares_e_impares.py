pares = []
impares = []

print("Bienvenido este es un contador de pares e impares\n")

while True:
    Numeros = int(input("Dijita los numeros alcontador (y '0' para terminar): "))
    if Numeros == 0:
        break
    if Numeros % 2 == 0:
        pares.append(Numeros)
    if Numeros % 2 != 0:
        impares.append(Numeros)

print(
    f"Estos son los pares de la lista escrita:{pares} (Numero de Datos:{len(pares)})\nEstos don los impares de la lista escrita:{impares} (Numero de Datos:{len(impares)})"
)
