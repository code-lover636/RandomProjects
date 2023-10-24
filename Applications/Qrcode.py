import os
import qrcode
import random
from tkinter import*
import cv2

root = Tk()
root.geometry("500x200")
root.config(bg="black")
root.title("Qr Code generator")


def show(num):
    img = cv2.imread(f"assets/Qrcode{num}.jpg")
    cv2.imshow("QRCODE",img)


def generate_code(link):
    if link.strip() != "":
        link_entry.delete(0,"end")
        img = qrcode.make(link)
        save_file(img)


def save_file(img):
    num = random.randint(1000,9000)
    for file in os.listdir("./assets"):
        if str(num) in file:
            save_file(img)
            return
    else:
        img.save(f"assets\Qrcode{num}.jpg")
        show(num)

heading = Label(root, text="    QR CODE Generator", bg="black", fg="red", font=("Algerian", 30, "bold"))
prompt = Label(root, text="Enter link", bg="yellow", fg="red",font=("Consolas", 15, "bold"), pady=5, anchor="nw")
link_entry = Entry(root, width=50, bd=2)
enter_but = Button(root, text="UPLOAD", bg="blue", fg="white", pady=3, command=lambda: generate_code(link_entry.get()))

heading.grid(row=0, column=0, columnspan=2)
prompt.grid(row=1, column=0, columnspan=2 )
link_entry.grid(row=2, column=0, ipady=3)
enter_but.grid(row=2, column=1)

root.mainloop()

