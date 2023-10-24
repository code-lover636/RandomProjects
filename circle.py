import turtle, math, random

scrn = turtle.Screen()
scrn.bgcolor("black")

tur = turtle.Turtle()
tur.penup()
tur.speed(20)
tur.color("red")
tur.hideturtle()

def spiral(rad):
    tur.pendown()
    for i in range(50):
        tur.begin_fill()
        tur.circle(75)
        tur.left(20)
        color = random.choice(["red","green","dark blue","light green","yellow"])
        tur.color(color)
        tur.fd(1)
        tur.end_fill()

spiral(100)

turtle.done()
