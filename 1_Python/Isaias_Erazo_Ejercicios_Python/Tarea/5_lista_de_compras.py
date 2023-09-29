lista_compras = []

print("Esta es una lista de Compras")

while True:
    productos = input("Ingresa los productos de Hoy (y 'listo' cuando termines): ")

    if productos.lower() == "listo":
        break

    lista_compras.append(productos)

print("\nLa lista completa es:")
for it, productos in enumerate(lista_compras, start=1):
    print(f"{it}. {productos}")
