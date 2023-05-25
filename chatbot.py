#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pyttsx3')
get_ipython().system('pip install keyboard')
from tkinter import *
import pyttsx3

root = Tk() 
root.title("Chatbot")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160 )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def send():
    send = "\nYou-> "+e.get()
    txt.insert(END, send)
    user = e.get().lower()
    if(user== "hello"):
        speak("Hi")
        txt.insert(END, "\n" + "Bot -> Hi")
    elif(user == "hi" or user == "hii" or user == "hii"):
        speak("Hello")
        txt.insert(END, "\n" + "Bot -> Hello")
    elif(e.get()== "how are you"):
        speak("fine! and you")
        txt.insert(END, "\n" + "Bot-> fine! and you")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        speak("Great! how can I help you?")
        txt.insert(END, "\n" +"Bot-> Great! how can I help you?")
    else:
        speak("Sorry! I dind't got you")
        txt.insert(END, "\n"+ "Bot-> Sorry! I dind't got you")
    e.delete(0, END)

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e= Entry(root, width=100)
e.grid(row=1, column=0) 
send = Button(root, text="Send", command=send)
send.grid(row=1, column=1)
root.bind('<Return>', lambda e: send(e))
root.mainloop()


# In[ ]:




