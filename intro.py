from tkinter import *

root =Tk()
root.title('GRID')
root.geometry('200x400')

#label = Label(root, text='holamundo mi primera etiqueta ')
l1 = Label(root, text='holamundo mi primera etiqueta ')
l2 = Label(root, text='holamundo mi primera etiqueta ')
l3 = Label(root, text='holamundo mi primera etiqueta ')

l3.grid(row=2, column=3)

l1.grid(row=0, column=0)

l2.grid(row=10, column=8)

root.mainloop()