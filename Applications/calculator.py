from tkinter import *
from tkinter import messagebox
from math import sqrt

root = Tk()
root.title("Calculator")

# creating input box
e = Entry(root, width=41, readonly="green", borderwidth=3,justify=RIGHT, font=('arial', 15), bg='ivory', fg='blue', insertwidth=2)
e.grid(row=0, column=1, columnspan=4, padx=0, pady=5, ipady=5)

e.insert(0,'0')
br_list = [" ", "+", "-", "x", "÷", "^"]
expression_list = []
count = 0


# defining functions
def click(value):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(value))


def last_math(list_name):
    global count
    count += 1
    try:
        if len(list_name) > 0:
            e.delete(0, END)
            e.insert(0, expression_list[-count])
    except IndexError:
        count = 0


def bracket():
    global br_list, count
    current = e.get()
    if current.count("(") == current.count(")"):
        if current == '' or current[-1] in br_list:
            click('(')
        else:
            click(' x (')
    else:
        click(')')


def delete(character):
    if 's' in character:
        e.delete(0, END)
    else:
        try:
            if e.get()[-1] == ' ':
                entry = e.get()[:-3]
            else:
                entry = e.get()[:-1]
            e.delete(0, END)
            e.insert(0, entry)
        except IndexError:
            pass


def sqroot(expression):
    for i in range(expression.count('√')):
        start = expression.index('√')
        sq1 = expression[start:expression.find(')', start, len(expression)) + 1]
        sq2 = sqrt(eval(sq1[2:-1]))
        expression = expression.replace(sq1, str(sq2))
        # print(sq1, sq2, expression, expression.count('√'), sep='\n')
    return expression


def equalize():
    global expression_list, count
    try:
        expression = e.get().strip()
        expression_list.append(expression)
        expression = sqroot(expression)
        expression = expression.replace('x', "*")
        expression = expression.replace('÷', "/")
        expression = expression.replace('^', "**")
        expression = expression.replace('mod', "%")

        count = 0
        if expression[0] == "0": expression = expression[1:]
        expression = eval(expression)
        e.delete(0, END)
        e.insert(0, expression)
    except ZeroDivisionError:
        messagebox.showerror('check again', 'Cannot divide by zero')
    except SyntaxError:
        messagebox.showerror('check again', 'Something went wrong.\n Leading zeros in decimal integer literals are not permitted\n Use an 0o prefix for octal integers')
    except NameError:
        e.delete(0, END)
        messagebox.showerror('check again', 'Something went wrong. Please check again!')
    return expression_list


B_X, B_Y = 30, 15
frames = Frame(root)
frames.grid(row=1, column=1)

# Number buttons
button1 = Button(frames, text="  1  ", command=lambda: click(1), padx=B_X, pady=B_Y, fg='white', bg='black', borderwidth=3, font=("consolas",15,'normal'))
button2 = Button(frames, text="  2  ", command=lambda: click(2), padx=B_X, pady=B_Y, fg='white', bg='black', borderwidth=3, font=("consolas",15,'normal'))
button3 = Button(frames, text="  3  ", command=lambda: click(3), padx=B_X, pady=B_Y, fg='white', bg='black', borderwidth=3, font=("consolas",15,'normal'))
button4 = Button(frames, text="  4  ", command=lambda: click(4), padx=B_X, pady=B_Y, fg='white', bg='black', borderwidth=3, font=("consolas",15,'normal'))
button5 = Button(frames, text="  5  ", command=lambda: click(5), padx=B_X, pady=B_Y, fg='white', bg='black', borderwidth=3, font=("consolas",15,'normal'))
button6 = Button(frames, text="  6  ", command=lambda: click(6), padx=B_X, pady=B_Y, fg='white', bg='black', borderwidth=3, font=("consolas",15,'normal'))
button7 = Button(frames, text="  7  ", command=lambda: click(7), padx=B_X, pady=B_Y, fg='white', bg='black', borderwidth=3, font=("consolas",15,'normal'))
button8 = Button(frames, text="  8  ", command=lambda: click(8), padx=B_X, pady=B_Y, fg='white', bg='black', borderwidth=3, font=("consolas",15,'normal'))
button9 = Button(frames, text="  9  ", command=lambda: click(9), padx=B_X, pady=B_Y, fg='white', bg='black', borderwidth=3, font=("consolas",15,'normal'))
button0 = Button(frames, text="  0  ", command=lambda: click(0), padx=B_X, pady=B_Y, fg='white', bg='black', borderwidth=3, font=("consolas",15,'normal'))
fg = 'white'
bg = 'magenta'
# Special operators
padx, pady = 30, 5
power10 = Button(frames, text=' 10^ ', command=lambda: click(' x 10^('),  font=("consolas",15,'normal'), padx=padx, pady=pady, fg=fg, bg=bg, borderwidth=3)
b_mod =   Button(frames, text=' mod ', command=lambda: click(' mod '),  font=("consolas",15,'normal'), padx=padx, pady=pady, fg=fg, bg=bg, borderwidth=3)
history = Button(frames, text='  ⟳  ', command=lambda: last_math(expression_list),  font=("consolas",15,'normal'), padx=padx-4, pady=pady, fg=fg, bg=bg, borderwidth=3)
bracket_but = Button(frames, text=' ( ) ', command=bracket, font=("consolas",15,'normal'), padx=padx, pady=pady, fg=fg, bg=bg, borderwidth=3)
power = Button(frames, text='  ^  ', command=lambda: click(' ^ '), font=("consolas",15,'normal'), padx=padx, pady=pady, fg=fg, bg=bg, borderwidth=3)
root_ = Button(frames, text='  √  ', command=lambda: click('√('), font=("consolas",15,'normal'), padx=padx, pady=pady, fg=fg, bg=bg, borderwidth=3)
button_dot = Button(frames, text="  .  ", command=lambda: click('.'),font=("consolas",15,'normal'), padx=padx, pady=B_Y, fg=fg, bg=bg, borderwidth=3)
clear = Button(frames, text='clear', fg=fg, bg=bg, command=lambda: delete("chars"), font=("consolas",15,'normal'), padx=padx, pady=B_Y, borderwidth=3)

frame = Frame(root)
frame.grid(row=1, column=4)

by = 14
b_off     = Button(frame, text='OFF', command=root.destroy, padx=20, pady=by+2, fg='white', bg='red', borderwidth=3, font=("consolas",10,'normal'))
backspace = Button(frame, text=" ⌫ ", command=lambda: delete("char"), padx=16, pady=by, fg='white', bg='purple', font=("consolas",10,'normal'))
equal     = Button(frame, text=" = ", command=equalize, padx=20, pady=by+1, fg='white', bg='red', borderwidth=3, font=("consolas",10,'normal'))
# Operation buttons
plus     = Button(frame, text=" + ", command=lambda: click(" + "), padx=21, pady=by, fg='red', bg='yellow', font=("consolas",10,'normal'))
minus    = Button(frame, text=' − ', command=lambda: click(" - "), fg='red', bg='yellow', padx=20, pady=by, borderwidth=3, font=("consolas",10,'normal'))
multiply = Button(frame, text=' x ', command=lambda: click(" x "), fg='red', bg='yellow', padx=20, pady=by, borderwidth=3, font=("consolas",10,'normal'))
division = Button(frame, text=' ÷ ', command=lambda: click(" ÷ "), fg='red', bg='yellow', padx=20, pady=by, borderwidth=3, font=("consolas",10,'normal'))

# griding
button7.grid(row=2, column=1)
button8.grid(row=2, column=2)
button9.grid(row=2, column=3)
button4.grid(row=3, column=1)
button5.grid(row=3, column=2)
button6.grid(row=3, column=3)
button1.grid(row=4, column=1)
button2.grid(row=4, column=2)
button3.grid(row=4, column=3)
button0.grid(row=5, column=2)
clear.grid(row=5, column=1)

b_off.grid(row=0, column=0)
backspace.grid(row=1, column=0)
plus.grid(row=2, column=0)
minus.grid(row=3, column=0)
multiply.grid(row=5, column=0)
division.grid(row=4, column=0)
equal.grid(row=6, column=0)

power10.grid(row=0, column=2)
b_mod.grid(row=0, column=1)
history.grid(row=0, column=3)

root_.grid(row=1, column=1)
power.grid(row=1, column=2)
bracket_but.grid(row=1, column=3)
button_dot.grid(row=5, column=3)

root.mainloop()
