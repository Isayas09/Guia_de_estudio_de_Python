# Division segura
def divicion_segura(Numerador, denominador):
    try:
        resultado = Numerador / denominador
        return resultado
    except ZeroDivisionError:
        print('no se puede dividir entre 0')
    except ValueError:
        print('ha ocrruido un problema')
    except:
        print('Ha ocurrido un problema')
try:
    x = int(input('Digite numerador: '))
    y = int(input('Digite denominador: '))
    divicion_segura(x,y)
except ValueError:
    print('Debe ingresar numeros enteros')


def convert_2_int(cadena):
    try:
        entero = int(cadena)
    except ValueError:
        print("Erro:La cadena no es valida")


cad = "2sd"
intCad = convert_2_int(cad)
print(type(intCad))
print("\n")

# Else en el manejo de excepcones
entrada = input("Ingrese un numero: ")
try:  # Lleva todo referente a operaciones
    numero = int(entrada)
    print(numero)
except ValueError:  # Mensaje de los errores
    print("error en la entrada")

else:  # Respuesta positiva
    print("La conversion fue exitosa")

# Finally
try:
    numerador = float(input("Ingrese el Numerador: "))
    denominador = float(input("Ingrese el denominador: "))

    resultado = numerador / denominador

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")

else:
    print("El resultado es: ", resultado)

finally:
    print("El codigo ha sido ejecutado con éxito")
print("\n")


# ejercicios
def numero_positivo():
    while True:
        try:
            numero = float(input("Ingresa un número positivo: "))
            if numero < 0:
                print("El número debe ser positivo.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")


numero = numero_positivo()
print("Has ingresado el número positivo:", numero)

# ///////////////////// Tarea //////////////////////////
import math


class RaizNegativaError(Exception):
    pass


class ValorNumericoError(Exception):
    pass


def calcular_raiz(numero):
    if numero < 0:
        raise RaizNegativaError("No se pueden calcular raices de numeros negativos")
    return math.sqrt(numero)


try:
    numero = float(input("ingresa el numero a que calcularas la raiz cuadrada: "))
    resultado = calcular_raiz(numero)

except RaizNegativaError as err:
    print("Error", err)
except ValueError:
    print("Error: Ingrese un valor numerico valido")

else:
    print(f"La raiz cuadrad es: {numero} es: {resultado}: ")

finally:
    print(24 * "*")
    print("\n\n Ejecucion terminada con exito \n\n")
    print(24 * "*")
