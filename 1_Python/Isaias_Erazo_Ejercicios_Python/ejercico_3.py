def sin_duplicados(lista):
    lista_sin_duplicados = []
    for n in lista:
        if n not in lista_sin_duplicados:
            lista_sin_duplicados.append(n)
    return lista_sin_duplicados

n = [1, 2, 2, 3, 3, 4, 4, 4, 5]
resultado = sin_duplicados(n)
print(resultado)