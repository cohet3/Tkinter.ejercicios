from tkinter import *

root =Tk()
root.title('hola mundo')
root.geometry('200x400')

#label = Label(root, text='holamundo mi primera etiqueta amorcitoo')
l1 = Label(root, text='holamundo mi primera etiqueta amorcitoo')
l2 = Label(root, text='holamundo mi primera etiqueta amoroo')
l3 = Label(root, text='holamundo mi primera etiqueta amorco')

l3.grid(row=2, column=3)

l1.grid(row=0, column=0)

l2.grid(row=10, column=8)

root.mainloop()