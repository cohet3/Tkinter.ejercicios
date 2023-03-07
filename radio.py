from cProfile import label
from tkinter import *

root = Tk()
root.title('Hola Mundo')

r = IntVar()
r.set('2')

CHANCHITOS = [
    ('Feliz', 'Feliz'),
    ('triste', 'triste'),
    ('Amargado', 'Amargado'),
    ('wolfgang', 'Wolfgang')
]

chanchito = StringVar()
chanchito.set('lala')

for text, chancho in CHANCHITOS:
    Radiobutton(root, text=text, variable=chanchito, value=chancho).pack()


l = Label(root, textvariable=chanchito)
l.pack()

root.mainloop()
