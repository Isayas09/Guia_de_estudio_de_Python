import funciones_bibliotecas as fb

print("Bienvenido al sistema de La Biblioteca")

while True:
    print(
        "Dijite la opcion a utilizar: \n 1-Agregar Libros a La biblioteca: \n 2-Mostrar Libros en Biblioteca: \n 3-Buscar Libros en Biblioteca: \n 4-Eliminar Libro: \n 0-Salir del Sistema: "
    )

    opcion = int(input("Ingrese el numero de la Opcion: "))

    if opcion == 0:
        print("\n Gracias por usar el Sistema")
        break

    elif opcion == 1:
        titulo = input("Ingrese es titulo del Libro: ")
        autor = input("Ingrese es nombre del autor: ")
        fecha = input("Ingrese la fecha de publicacion AAAA-MM-DD: ")
        fb.agregar_libros(titulo, autor, fecha)

    elif opcion == 2:
        print("El libro a mostrar es: \n")
        fb.mostrar_libro()

    elif opcion == 3:
        busqueda = input("Dijite el nombre del titulo: \n")
        fb.buscar_libro(busqueda)

    elif opcion == 4:
        eliminar = input("Dijite el Titulo que deseas eliminar: ")
        fb.eliminar_libro(eliminar)
        print("libro eliminado con exito")

    else:
        print("La opcion no existe")
