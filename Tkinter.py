'''
# Project 1
from tkinter import *

window=Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300')

def insert_text():
    value=entry.get()
    textbox.insert(END, value+"\n")
    entry.delete(0,END)

greeting=Label(window,text="Hi Everyone",fg="black",bg='white')
button=Button(window,text="Click me",bg='black',fg='black',command=insert_text)
entry=Entry(window,fg='Yellow',bg='blue',width=50)
greeting.pack()
button.pack()
entry.pack()

frame=Frame(master=window,relief=RAISED,borderwidth=5)
frame.pack()
label=Label(master=frame,text='Sample Form')
label.pack()

textbox=Text(fg='Green',bg="Yellow")
textbox.pack()

window.mainloop()
'''

import tkinter as tk
window=tk.Tk()

for i in range(3):
    for j in range(3):
        frame=tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i,column=j, padx=5, pady=5)
        label=tk.Label(master=frame,text=f"Row {i}\nColumn {j}")
        label.pack()
window.mainloop()