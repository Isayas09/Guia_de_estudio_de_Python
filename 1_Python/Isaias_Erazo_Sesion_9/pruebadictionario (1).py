num_estudiantes = int(input("Ingrese el número de estudiantes: "))

datos_estudiantes = {}

for it in range(1, num_estudiantes + 1):
    nombre = input(f"Ingrese el nombre del estudiante {it}: ")
    edad = int(input(f"Ingrese la edad del estudiante {it}: "))
    datos_estudiantes[nombre] = edad

    estudio = input(f"Ingrese el nivel del estudiantes {it}: ")
    grado = input(f"Ingrese el grado del estudiante {it}: ")

    datos_estudiantes[estudio] = grado


print("\nDatos de los estudiantes:")
for nombre, edad , estudio, grado in datos_estudiantes.items():
    print(
        f"Nombre: {nombre}, Edad: {edad}, Estudio: {estudio}, Grado: {grado} ")
