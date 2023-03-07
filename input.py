from cgitb import text
from tkinter import *

root = Tk ()
root.title('hola mundo')
root.geometry('500x500')

e = Entry(root, width=40)
e.pack()
e.insert(0, "Ingresa texto:")

def click():
    texto = e.get()
    textvarible.set(texto)
    valor=textvarible.get()
    print(valor)
    # l = Label(root, text=texto)
    # l.pack()
    e.delete(0, END)


btn = Button(root, text='click', command=click)
btn.pack() 

textvarible = StringVar() 

l = Label(root, textvariable=textvarible)
l.pack()

root.mainloop()