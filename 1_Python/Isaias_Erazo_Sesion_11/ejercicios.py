# ///////////////////// Tarea //////////////////////////
import math

class RaizNegativaError(Exception):
    pass

class ValorNoNumericoError(Exception):
    pass


def calcular_raiz(numero):
    if numero < 0:
        raise RaizNegativaError('No se puden calcular raices de números negativos')
    return math.sqrt(numero)

try:
    numero = float(input('Ingresa el numero al que calcularas la la raiz cuadrada: '))
    
    resultado = calcular_raiz(numero)
    
except RaizNegativaError as err:
    print('!!!!Error:', err)
    
except ValueError:
    print('Error: Ingrese un valor numérico Valido')

else:
    print(f'La raiz cuadrada de {numero} es: {resultado : .2f} ')

finally:
    print(43*'*')
    print('\n Ejecucion terminada con exito\n')
    print(43*'*')