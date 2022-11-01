from tkinter import *
import tkinter as tk
from tkinter import ttk

root = Tk(className= 'Fun Button Counter')
root.geometry("500x200")
#create style object

#variable is stored in the root object
root.counter = 0

def clicked():
    root.counter += 1
    L['text'] = 'Button clicked: ' + str(root.counter)
        
b = Button(root, fg='white', bg='green', text="Click Me", command=clicked)
b.pack()
e = Button(root, fg='black', bg='red', text="FINISH", command = root.destroy)
e.pack()

L = Label(root, text="No clicks yet.")
L.pack()

root.mainloop()