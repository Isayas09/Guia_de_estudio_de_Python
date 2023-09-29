usuarios = []  # informacionde los libros


def agregar_usuario(titulo, autor, fecha):
    usuarios.append({"titulo": titulo, "autor": autor, "fecha": fecha})


def mostrar_usuario():
    for it in usuarios:
        print(
            f'titulo: {it["titulo"]}, autor {it["autor"]}, fecha de publicacion: {it["fecha"]}'
        )


def buscar_usuario(titulo):
    encontrado = False
    for it in usuarios:
        if titulo.lower() in it["titulo"].lower():
            print(
                f'titulo: {it["titulo"]}, autor {it["autor"]}, fecha de publicacion: {it["fecha"]}'
            )
        encontrado = True
        break

    if not encontrado:
        print("No existe el libro")
