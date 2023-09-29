import turtle
import random

# Configurar el lienzo
wn = turtle.Screen()
wn.bgcolor("white")

# Función para dibujar una flor
def dibujar_flor(x, y):
    # Configurar la tortuga para la flor
    rosa = turtle.Turtle()
    rosa.shape("turtle")
    rosa.speed(0)  # Configura la velocidad máxima
    rosa.penup()
    rosa.goto(x, y)
    rosa.pendown()

    # Función para dibujar un pétalo de rosa
    def dibujar_petalo():
        rosa.color("yellow")
        rosa.begin_fill()
        rosa.circle(100, 60)
        rosa.left(120)
        rosa.circle(100, 60)
        rosa.end_fill()

    # Dibuja los pétalos de la rosa
    for _ in range(6):
        dibujar_petalo()
        rosa.left(60)

    # Posiciona la tortuga para el tallo
    rosa.penup()
    rosa.goto(x, y - 100)  # Posición bajo la flor
    rosa.pendown()

    # Dibuja el tallo
    rosa.color("green")
    rosa.width(10)
    rosa.goto(x, y - 250)  # Longitud del tallo

    # Dibuja las hojas
    rosa.penup()
    rosa.goto(x - 30, y - 250)
    rosa.pendown()
    rosa.goto(x + 30, y - 250)
    rosa.goto(x, y - 200)
    rosa.goto(x - 30, y - 250)

    rosa.hideturtle()

# Dibuja múltiples flores en posiciones aleatorias
num_flores = 10  # Puedes ajustar la cantidad de flores
for _ in range(num_flores):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    dibujar_flor(x, y)

# Mantén la ventana abierta
wn.mainloop()



