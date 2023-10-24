import os
import pyjokes
import pyttsx3
import datetime
import wikipedia
import webbrowser
from tkinter import *
import speech_recognition as sr

root = Tk()
root.geometry('400x600')
root.title('')
root.resizable(0, 0)
root.configure(background='black')

name = "JARVIS"


def speak(text):
    global engine
    engine = pyttsx3.init("sapi5")
    engine.setProperty('rate', 170)

    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="en-IN")
        except Exception as e:
            print(str(e))

        return said

def respond(query):
    if "hello"  in query:
        el_response['text'] = 'Hi. How can I help you?'
        el_response.update()
        speak('Hi, How can I help you?')
    elif " you ready" in query:
        el_response['text'] = 'Ready always for you,sir'
        el_response.update()
        speak('Ready always for you,sir') 
    elif "what's your name" in query:
        el_response['text'] = f"oh you forgot me. I'm {name}"
        el_response.update()
        speak(f"oh you forgot me. I'm {name}")

    elif 'date and time' in query:
        el_response['text'] = datetime.datetime.now()
        el_response.update()
        speak(f"It's {datetime.datetime.ctime()}\tand today is {datetime.date.today()}")
    elif 'joke' in query:
        joke = pyjokes.get_joke('en', 'neutral')
        joke = joke[:30] + "\n" + joke[30:]
        el_response['text'] = joke
        el_response.update()
        print('helllo')
        speak(joke)
    elif 'open' in query:
        query = query.replace('open ', '')
        webbrowser.open(f"{query}.com")
    elif 'search' in query:
        speak("what do you want to search?")
        search = get_audio()
        url = "https://google.com/search?q=" + search
        el_response['text'] = f"Here is what i have found for {search}"
        webbrowser.get().open(url)
    elif 'location' in query:
        speak("which location do you want to search for?")
        location = get_audio()
        url = "https://google.nl/maps/place/" + location
        el_response['text'] = f"Here is what i have found for {location}"
        webbrowser.get().open(url)
    elif "activate eclipse" in query:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        name = 'ECLIPSE'
        speak('hello sir, how may i help you')
    elif "activate jarvis" in query:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        name = 'JARVIS'
        speak('hello sir, how may i help you')
    elif 'stop this' in query:
        speak("thank you sir")
        exit()
    elif query != '':
        try:
            result = wikipedia.summary(query, sentences=1)
            blit = ''
            words = result.split()
            try:
                for i in range(len(words) // 5 + 1):
                    for j in range(5):
                        blit += words[j] + ' '
                    del words[:5]
                    blit += '\n'
            except IndexError:
                pass

            el_response['text'] = blit
            el_response.update()

            speak(result)
        except Exception:
            speak('I can search that for you.')
            url = "https://google.com/search?q=" + query
            webbrowser.get().open(url)
    else:
        speak("Sorry,,I don't get you.")


def send():
    global entry
    query = entry.get()
    entry.delete(0,END)
    respond(query.lower())


def listen():
    global state, el_response, qns, engine, name
    state.configure(text='Listening...')
    state.update()
    query = get_audio().lower()
    qns['text'] = query.upper()
    qns.update_idletasks()
    state.configure(text='')
    state.update()
    respond(query)

txt_input = Frame(root, bg="black")
txt_input.place(relx=0.1, rely=0.86)
entry = Entry(txt_input, width=45)
entry.grid(row=0, column=0, ipady=2)

send = Button(txt_input, text="s", command = send, bg='#B4D5FF', padx=3.2)
send.grid(row=0, column=1)

el_response = Label(root, text=f"Hi, I'm {name}", bg='black', fg='#3399FF', font=('', 12, 'normal'))
el_response.pack()

state = Label(root, text='', bg='black', fg='#3399FF', font=('', 12, 'normal'))
state.place(relx=0.15, rely=0.93, anchor=CENTER)

qns = Label(root, text='', bg='black', fg='#3399FF', font=('', 12, 'normal'))
qns.place(relx=0.3, rely=0.76, anchor=CENTER)

mic_img = PhotoImage(file="bluemic.png")
mic = Button(root, image=mic_img, borderwidth=0, command=listen, bg='black', activebackground='#B4D5FF')
mic.place(relx=0.9, rely=0.88, anchor=CENTER)

line_img = PhotoImage(file='line.png')
line = Label(root, image=line_img, borderwidth=0, bg='black')
line.place(relx=0.5, rely=0.83, anchor=CENTER)
root.update()


root.mainloop()
