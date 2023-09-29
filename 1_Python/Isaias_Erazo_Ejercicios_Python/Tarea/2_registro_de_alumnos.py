alumnos = []

while True:
        nombre = input("Ingresa el nombre del alumno (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        
        edad = int(input("Ingresa la edad de {} : ".format(nombre)))

        alumnos.append({"nombre": nombre, "edad": edad})

print("\nAlumnos mayores de 18 años:")
for alumno in alumnos:
        if alumno["edad"] > 18:
            print(alumno["nombre"])