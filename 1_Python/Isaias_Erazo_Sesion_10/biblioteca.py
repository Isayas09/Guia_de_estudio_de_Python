# Archivo principal del proyecto
"""
Esta sistema se ha desarrollado para automatizar los procesos en una 
biblioteca ; contiene las funciones basicas para llevar el control de el 
usuario
"""

import libreria.funciones_bibliotecas as fb

print('Bienvenido al Sistema de Biblioteca\n')

while True:
    
    print('Digite la opcion a utilizar:\n 1- Agregar Libros a la Biblioteca\n 2-Mostrar libros en biblioteca\n 3-Buscar libros en biblioteca\n 4- Borrar un libro\n 0- Salir del sistema')

    opcion = int(input('Ingrese el número de la opción:'))

    if opcion == 0:
        print('\n Gracias por usar el sistema!!!')
        break
    elif opcion == 1:
        titulo = input('Ingrese el titulo del libro: ')
        autor = input('Ingrese el nombre del Autor: ')
        fecha = input('Ingrese la Fecha de publicacion AAAA-MM-DD: ')
        fb.agregar_libros(titulo, autor, fecha)

    elif opcion == 2:
        print('El libro a mostrar es: \n\n')
        fb.mostrar_libro()

    elif opcion == 3:
        busqueda = input('digite en nombre del Titulo a buscar: \n')
        fb.buscar_libros(busqueda)

    elif opcion == 4:
        libroT = input('digite en nombre del Titulo a eliminar1: \n')
        fb.Eliminar_Libro(libroT)
        print('libro eliminado con exito\n')

    else:
        print('Opcion Inválida')
