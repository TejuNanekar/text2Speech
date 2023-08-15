import tkinter as tk
from tkinter import*
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import sys
import os

root=Tk()
root.title("Text to Speech")
root.geometry("900x450+200+200")
root.configure(bg="#305062")

engine=pyttsx3.init()

def speaknow():
    text= text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        elif(gender=='Female'):
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=="Normal"):
            engine.setProperty('rate',100)
        else:
            engine.setProperty('rate',60)
            setvoice()

Top_frame=Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

logo=PhotoImage(file="voice33.png")
Label(Top_frame,image=logo,bg="white").place(x=10,y=5)


text_area=Text(root,font="Robote 20",bg="White",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=780,y=160)

gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14 bold",state='r',width=10,)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Female')



speed_combobox=Combobox(root,values=['Fast','Slow','Normal'],font="arial 14 bold",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')


btn=Button(root,text="Speak",width=10,font="arial 14 bold",command=speaknow)
btn.place(x=550,y=280)
root.mainloop()