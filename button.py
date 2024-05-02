from re import L
from tkinter import *

root =Tk()
root.title('Button')

l = Label(root, text='hola mundo')
def click():
  
    l.pack()

btn = Button(root, text="clickeame", command=click, fg='red', bg='blue')
btn.pack()

root.mainloop()
