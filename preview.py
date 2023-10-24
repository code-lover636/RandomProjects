import turtle

tur = turtle.Turtle()
screen = turtle.getscreen()
screen.bgcolor("black")
turtle.screensize(400,400)
screen.bgpic("assets/kathak.png")
def position(event):
    a, b = event.x, event.y
    print('tur.goto({}, {})'.format(a, b))

ws = turtle.getcanvas()
ws.bind('<Button-1>', position)
turtle.done()
