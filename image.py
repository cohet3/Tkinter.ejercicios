from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola mundo')

# imagen = Image.open('coliseo.jpeg')
# imagen.show()

img = ImageTk.PhotoImage(Image.open('gato3.jpg'))
l = Label(image=img)
l.pack()

root.mainloop()