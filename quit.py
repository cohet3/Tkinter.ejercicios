from tkinter import *

root = Tk()
root.title('Lógica para cerrar la ventana')

exit = Button(root, text='salir', command=root.quit)
exit.pack()

root.mainloop()