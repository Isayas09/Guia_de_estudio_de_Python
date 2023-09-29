# import librarys.mymodule as mm
import librarys.areas as ar


# print('El resultado es : ', mm.sumar(4, 5))
# print('El resultado es : ', mm.restar(4, 5))
# print('El Area de un rectangulo es : ', ar.area_rectangulo(4, 5))


import librarys.mixmodulo as mx

archivo = "Power.csv"

carga_datos = mx.cargar_datos(archivo)
print(carga_datos.head())


lst = [1, 2, 3, 4, 5]
prom = mx.calcular_promedio(lst)

print('EL promedio es : ', prom)
