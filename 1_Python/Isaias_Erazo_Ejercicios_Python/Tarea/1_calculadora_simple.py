def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No es posible dividir entre cero"


while True:
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Ingresa el número de la operación deseada: ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    n1 = float(input("Ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", suma(n1, n2))
    elif opcion == "2":
        print("Resultado:", resta(n1, n2))
    elif opcion == "3":
        print("Resultado:", multiplicacion(n1, n2))
    elif opcion == "4":
        print("Resultado:", division(n1, n2))
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
