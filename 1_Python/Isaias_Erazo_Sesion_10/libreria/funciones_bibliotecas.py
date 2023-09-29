# Archivo principal del projecto (Automatizar procesos de una biblioteca)
# Funciones (Agregar_libro, Mostrar_libro, Buscar_Libro)

# import datetime  # datetime para control de tiempo

libro = []  # informacionde los libros


def agregar_libros(titulo, autor, fecha):
    libro.append({"titulo": titulo, "autor": autor, "fecha": fecha})


def mostrar_libro():
    for it in libro:
        print(
            f'titulo: {it["titulo"]}, autor {it["autor"]}, fecha de publicacion: {it["fecha"]}'
        )


def buscar_libro(titulo):
    encontrado = False
    for it in libro:
        if titulo.lower() in it["titulo"].lower():
            print(
                f'titulo: {it["titulo"]}, autor {it["autor"]}, fecha de publicacion: {it["fecha"]}'
            )
        encontrado = True
        break

    if not encontrado:
        print("No existe el libro")


def eliminar_libro(titulo):
    encontrado = False
    for it in libro:
        if titulo.lower() in it["titulo"].lower():
            print(f"Eliminando libro:")
            print(
                f"titulo: {it['titulo']}, autor: {it['autor']}, fecha_de_publicacion: {it['fecha']}"
            )
            libro.remove(it)
            encontrado = True
            break
    if not encontrado:
        print("Libro no encontrado")
