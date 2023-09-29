def imprimir_secuencia(n):
    for i in range(1, n + 1):
        linea = " ".join(["1"] * i)
        print(linea)

n = int(input("Ingresa un numero: "))
imprimir_secuencia(n)
