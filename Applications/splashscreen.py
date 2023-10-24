from tkinter import*
from PIL import Image, ImageTk
import turtle
import time

WIDTH, HEIGHT = 700, 400

root = Tk()
x = root.winfo_screenwidth()/2 - WIDTH/2
y = root.winfo_screenheight()/2 -HEIGHT/2
root.geometry(f"{WIDTH}x{HEIGHT}+%d+%d" % (x, y))
root.config(highlightthickness=0)
root.overrideredirect(True)

# Turtle
canvas = Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness=0)
canvas.pack(expand=1, fill=BOTH, anchor='sw')
screen = turtle.TurtleScreen(canvas)
screen.bgpic("assets/clock.png")
screen.bgcolor("black")

splash = turtle.RawTurtle(screen,"square")
splash.speed(0)
splash.shapesize(0.7)
splash.color("blue")
splash.hideturtle()
splash.penup()
splash.left(180)
splash.fd(230)
splash.right(90)
splash.pendown()
splash.write("DATE & TIME APP", font=("ROG FONTS", 30, "bold"))

def load():
    global splash, root
    splash.fd(WIDTH/2)
    time.sleep(3)
    splash.fd(WIDTH/3)
    time.sleep(5)
    splash.fd(WIDTH/6)

splash.showturtle()
splash.penup()
splash.pensize(15)
splash.goto(-WIDTH/2,-HEIGHT/2)
splash.speed(1)
splash.right(90)
splash.pendown()
load()
root.destroy()
root.mainloop()
