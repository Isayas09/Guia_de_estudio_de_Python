def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primos_menores_que_n(numero):
    primos = []
    for i in range(2, numero):
        if es_primo(i):
            primos.append(i)
    return primos

numero = int(input("Ingrese un número: "))

if numero <= 2:
    print("No hay números primos menores que", numero)
else:
    primos = numeros_primos_menores_que_n(numero)
    print("Números primos menores que", numero, "son:", primos)
