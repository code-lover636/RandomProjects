from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import ttk
from utils import *
import pygame

root = Tk()
pygame.mixer.init()
root.geometry("550x550")
root.iconbitmap("./assets/VB.ico")
root.title("voicebook")
root.resizable(False,False)

# Variables
Mode = "Paused"
Line = 0
sound = SoundUtils()

# Background
bg_container = Canvas(root, width=550, height=550, bg="white")
bg_container.pack()
bgimg = ImageTk.PhotoImage(Image.open("./assets/background.png"))
bg_container.create_image(0, 0, image=bgimg, anchor=NW)

# File Picker
def pick_file():
    global pdf, audio
    filename = filedialog.askopenfilename(
                title="PDF Selector", 
                initialdir=r"C:\Users\aravi\OneDrive\Documents\My Documents\Amritha", 
                filetypes=(("pdf files", "*.pdf"), ("all files", "*.*"))
                )
    print(filename)
    if filename != "": 
        filenm.config(text=filename.split("/")[-1][:-4][:20]+"...")
        
        pdf = PDFUtils(filename)
        speedbtn.config(state=DISABLED)
        tonebtn.config(state=DISABLED)
        statebtn.config(command=play)
        content = pdf.get_page(pdf.currentPage)
        insertPage(content)
        
        name = sound.save_audio(content, filenm["text"].replace(".",""))
        audio = pygame.mixer.Sound(name)
        audio.play()
        pygame.mixer.pause()
        return filename

fileimg = ImageTk.PhotoImage(Image.open("./assets/pdf-icon.png"))
filebtn = Button(bg_container, cursor="hand2", borderwidth=0, image=fileimg, padx=0, pady=0, command=pick_file)
filebtn.place(x=499, y=14)

filenm = Label(bg_container, text="No file selected", font=("Candara", 10), fg="black", bg="white", anchor=E)
filenm.place(x=382, y=45)

# Text Box
def insertPage(content):
    display.config(state=NORMAL)
    display.insert("1.0", content)
    display.config(state=DISABLED)
    
display = Text(bg_container, width=54, height=18, font=("Arial", 11), fg="black", bg="#D9D9D9", borderwidth=0)
display.insert("1.0", "Please select a PDF file")
display.config(state=DISABLED)
display.place(x=57, y=103)

# Voice Tone
maleimg = ImageTk.PhotoImage(Image.open("./assets/male-icon.png"))
femaleimg = ImageTk.PhotoImage(Image.open("./assets/female-icon.png"))
tonebtn = Button(bg_container, command=lambda: sound.chngtone(tonelabel), bg="white", cursor="hand2", image=maleimg, borderwidth=0,highlightthickness=0, activebackground="white")
tonebtn.place(x=35, y=470)
tonelabel = Label(bg_container,text="Male Voice", bg="white", fg="black", borderwidth=0, anchor=CENTER)
tonelabel.place(x=31, y=515)

# Speed Rate
fastimg = ImageTk.PhotoImage(Image.open("./assets/fast-icon.png"))
speedbtn = Button(bg_container, bg="white", command=lambda: sound.chngrate(speedlabel), cursor="hand2", image=fastimg, borderwidth=0,highlightthickness=0, activebackground="white")
speedbtn.place(x=470, y=470)
speedlabel = Label(bg_container,text="1.0x", bg="white", fg="black", borderwidth=0, anchor=CENTER)
speedlabel.place(x=480, y=515)

# Backward & Forward Button
backimg = ImageTk.PhotoImage(Image.open("./assets/backward-icon.png"))
forthimg = ImageTk.PhotoImage(Image.open("./assets/forward-icon.png"))
backbtn = Button(bg_container, bg="#D9D9D9", cursor="hand2", image=backimg, borderwidth=0,highlightthickness=0, activebackground="#D9D9D9")
backbtn.place(x=211, y=479)
forthbtn = Button(bg_container, bg="#D9D9D9", cursor="hand2", image=forthimg, borderwidth=0,highlightthickness=0, activebackground="#D9D9D9")
forthbtn.place(x=313, y=479)

# Play & Pause Button
def play():
    global Mode, audio
    if Mode == "Playing":
        pygame.mixer.pause()
        Mode = "Paused" 
        statebtn.config(image=playimg)
    else:
        pygame.mixer.unpause()
        Mode = "Playing"
        statebtn.config(image=pauseimg)
   
playimg = ImageTk.PhotoImage(Image.open("./assets/play-icon.png"))
pauseimg = ImageTk.PhotoImage(Image.open("./assets/pause-icon.png"))
statebtn = Button(bg_container, bg="#D9D9D9", image=playimg, borderwidth=0,highlightthickness=0, cursor="hand2", activebackground="#D9D9D9")
statebtn.place(x=252, y=472)

root.mainloop()