from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Carrusel')
root.geometry('850x650')

img1 = ImageTk.PhotoImage(Image.open('gato1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('gato2.webp'))
img3 = ImageTk.PhotoImage(Image.open('gato3.jpg'))


lista = [img1, img2, img3]

l = Label(root, image=img1)
l.grid(row=0, column=0, columnspan=3, pady=10)

def adelante(img_num):
    global l
    global btn_atras
    global btn_adelante

    l.grid_forget()
    l = Label(root, image=lista[img_num])
    btn_atras = Button(root, text='<-', command=lambda: atras(img_num - 1))
    btn_adelante = Button(root, text='->', command=lambda: adelante(img_num + 1))

    if img_num == 2:
        btn_adelante = Button(root, text='N/A', state=DISABLED)

    l.grid(row=0, column=0, columnspan=3, pady=10)
    btn_atras.grid(row=1, column=0, pady=10)
    btn_adelante.grid(row=1, column=2, pady=10)

def atras(img_num):
    global l
    global btn_atras
    global btn_adelante

    l.grid_forget()
    l = Label(root, image=lista[img_num])
    btn_atras = Button(root, text='<-', command=lambda: atras(img_num - 1))
    btn_adelante = Button(root, text='->', command=lambda: adelante(img_num + 1))

    if img_num == 0:
        btn_atras = Button(root, text='N/A', state=DISABLED)

    l.grid(row=0, column=0, columnspan=3, pady=10)
    btn_atras.grid(row=1, column=0, pady=10)
    btn_adelante.grid(row=1, column=2, pady=10)



btn_atras = Button(root, text='N/A', state=DISABLED)
btn_adelante= Button(root, text='->', command=lambda: adelante(1))

btn_atras.grid(row=1, column=0, pady=10)
btn_adelante.grid(row=1, column=2, pady=10)

root.mainloop()