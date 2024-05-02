from tkinter import *

root = Tk()
root.title('sliders')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()


def enviar():
    hor = horizontal.get()
    ver = vertical.get()
    print(str(hor) + '' + str(ver))

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()