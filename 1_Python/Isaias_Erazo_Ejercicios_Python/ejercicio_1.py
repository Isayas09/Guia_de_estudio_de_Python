lista = [1, 3, 6, 3, 23, 22, 68, 4, 2, 1]

sumaPares = 0
for n in lista:
    if n % 2 == 0:
        sumaPares += n

print("La suma de los numeros pares es: ", sumaPares)