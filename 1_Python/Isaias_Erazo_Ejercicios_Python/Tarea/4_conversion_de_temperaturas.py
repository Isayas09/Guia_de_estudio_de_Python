Grados = []
Grados2 = []

print("Bienvenido al converson de Grados Celcius a fahrenheit \n")

while True:
    Celcius = float(input("Ingresa una temperatura en grados Celcius: "))
    Grados.append(Celcius)

    for g in Grados:
        Fahrenheit = g * 1.8 + 32
        Grados2.append(Fahrenheit)

    otra_Conversion = input("Deseas relizar otra conversion? si / no?: ")
    if otra_Conversion.lower() != "si":
        break

print(f"{Grados}°C = {Grados2}°F\n")
