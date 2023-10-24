from tkinter import*
import turtle
from time import strftime
from tkcalendar import Calendar
import splashscreen

# Setting window
root = Tk()
root.config(bg="black")
root.title("My Clock")
root.iconbitmap("assets\icon.ico")

def time_now(hands):
    Time = strftime("%I %M %S")
    Time = Time.split()
    hands[2].right(6*int(Time[2]) + 6)
    hands[1].right(6*int(Time[1]))
    hands[0].right(0.5*( 60*int(Time[0]) + int(Time[1]) ))


def setup_hands( length:tuple, width:tuple, shape="arrow", colour=("white", "blue", "red")):
    try:
        hands = []
        for x in range(3):
            hands.append(turtle.RawTurtle(screen,shape))
            hands[x].hideturtle()
            hands[x].left(90)
            hands[x].color(colour[x])
            hands[x].shapesize(stretch_len=length[x], stretch_wid=width[x])
            hands[x].showturtle()
        time_now(hands)
        center.stamp()
        return hands
    except Exception:
        print("error0")


def tick():
    try:
        center.stamp()
        hands[2].right(6)
        hands[1].right(1/10)
        hands[0].right(1/120)
        center.stamp()
        analog_canvas.after(1000,tick)
    except Exception:
        print("error1")


def show_time():
    try:
        Time = strftime("%I:%M:%S %p")
        Date = strftime("%d %h %Y")
        digital_time.config(text=Time)
        digital_date.config(text=Date)
        digital_time.after(1000,show_time)
        digital_date.after(86400000, show_time)
    except Exception:
        print("error2")

def cal():
    cal_win = Toplevel(root, bg="black", cursor="dotbox")
    cal_win.title("My Calendar")
    calendar = Calendar(cal_win, selectmode='day', year=int(strftime("%Y")), month=int(strftime("%m")) , day=int(strftime("%d")),\
                        bg='black', fg='white')
    calendar.pack()

# Widgets
analog_canvas = Canvas(root, width=400, height=350, bg="black")
digital_time  = Label(root, bg="black", fg="blue", font=("ROG FONTS",30,"normal"), width=10, justify="center")
digital_date  = Label(root, bg="black", fg="red", font=("Algerian",30,"normal"), width=10, justify="left")
calendar_but = Button(root, bg="black",activebackground="black", fg="grey", text="📆", font=("consolas",20,"normal"), bd=0,  justify="left", command=cal)

analog_canvas.grid(row=0, column=0, columnspan=2)
digital_time.grid(row=1, column=0, columnspan=2)
digital_date.grid(row=2, column=1, sticky="nw")
calendar_but.grid(row=2, column=0)
# Turtle screen
screen = turtle.TurtleScreen(analog_canvas)
screen.bgpic("assets\clock.png")
screen.bgcolor("black")
center = turtle.RawTurtle(screen,"circle")
center.color("white")
center.shapesize(0.5)
hands = setup_hands(length=(5,10,14), width=(0.2,0.3,0.3))


try:
    show_time()
    tick()
except Exception:
    print('error3')
root.mainloop()
