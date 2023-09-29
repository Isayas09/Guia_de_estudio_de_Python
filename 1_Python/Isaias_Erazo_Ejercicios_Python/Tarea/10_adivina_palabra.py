import random

palabras = ["gato", "conejo", "perro", "pez", "leon", "elefante"]
palabra_elegida = random.choice(palabras)
letras_adivinadas = ["_"] * len(palabra_elegida)


def mostrar_palabra():
    print(" ".join(letras_adivinadas))


intentos = 0
max_intentos = 10

print("Bienvenido al Juego, Adivina el nombre de un Animal")
mostrar_palabra()

while "_" in letras_adivinadas and intentos < max_intentos:
    letra = input("\n Ingresa una letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Por favor ingrese solo una letra")

    if letra in letras_adivinadas:
        print("Ya has adivinado esa letra")
        continue

    if letra in palabra_elegida:
        for i in range(len(palabra_elegida)):
            if palabra_elegida[i] == letra:
                letras_adivinadas[i] = letra
        mostrar_palabra()
    else:
        intentos += 1
        print("Letra incorrecta, Intentos restantes:", max_intentos - intentos)

if "_" not in letras_adivinadas:
    print("Felicidades has adivinado la palabra")
else:
    print("Perdiste, la palabra era:", palabra_elegida)
