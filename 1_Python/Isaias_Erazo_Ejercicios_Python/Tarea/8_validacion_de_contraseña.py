contraseña = input(
    "Ingresa una contraseña con almenos 8 caracteres y almenos una letra y un numero:\n"
)

if len(contraseña) >= 8:  # Los 8 caracteres de la contraseña
    letra = False
    numero = False

    for caracter in contraseña:  # Letra y Numero de la contraseña
        if caracter.isalpha():
            letra = True
        elif caracter.isdigit():
            numero = True

    if letra and numero:  # Resultado
        print("Contraseña valida")
    else:
        print("Contraseña invalida: Debe contener un numero y una letra")
else:
    print("Contraseña invalida: Debe tener 8 caracteres")
