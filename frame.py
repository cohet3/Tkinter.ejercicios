from tkinter import *

root = Tk()
root.title('frame')

#frame = LabelFrame(root, text='login', padx=10, pady=10, borderwidth=10)
frame = LabelFrame(root, padx=10, pady=10, borderwidth=10)
frame.pack(padx=50, pady=50)

l = Label(frame, text='Estod dentro de un frame')
btn = Button(frame, text='Salir', command=root.quit)
l.pack()
btn.pack()

root.mainloop()