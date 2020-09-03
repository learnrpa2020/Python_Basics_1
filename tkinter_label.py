from tkinter import *
from tkinter import ttk
root=Tk()
label=ttk.Label(root,text="Hello, Tkinter")
label.pack()
label.config(text='This is the very useful program to learn about tkinter.Using this we can create desktop applications')
label.config(wraplength=150)
label.config(justify=CENTER)
label.config(foreground="blue",background="yellow")
label.config(font=('courier',18,'bold'))
label.config(text="Hello,Tkinter")
