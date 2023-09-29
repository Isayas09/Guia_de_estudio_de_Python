entrada = input("Ingrese un conjunto de números separados por comas: ")

numeros = [float(numero) for numero in entrada.split(',')]

if len(numeros) == 0:
    print("La lista está vacía.")
else:
    maximo = max(numeros)
    minimo = min(numeros)

    print(f"El número más grande es: {maximo}")
    print(f"El número más pequeño es: {minimo}")
