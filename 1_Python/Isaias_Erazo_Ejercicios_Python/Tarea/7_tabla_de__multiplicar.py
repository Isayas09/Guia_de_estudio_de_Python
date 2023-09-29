def multiplicacion(a, b):
    return a * b


tablas_multiplicar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Bienvenido aqui encontraras las tablas de multiplicar del 1 al 10\n")


numero = int(input("Que tabla deseas ver: "))
if numero in tablas_multiplicar:
    print(f"tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = multiplicacion(numero, i)
        print(f"{numero} x {i} = {resultado}")
else:
    print("Por favor ingresa un numero del 1 al 10")
