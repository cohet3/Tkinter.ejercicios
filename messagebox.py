from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('popUp')

#def click():
    #messagebox.showwarning('Popup', 'Hola Mundo!')

# def click():
#     messagebox.showinfo('Popup', 'Hola Mundo!')

# def click():
#     messagebox.showerror('Popup', 'Hola Mundo! :(')

# def click():
#     respuesta = messagebox.askquestion('Popup', 'Hola Mundo!') *devuelve un boolean
#     if respuesta == 'yes':
#         messagebox.showinfo('Respuesta', ':) la respuesta fue' + respuesta)
#     else:
#         messagebox.showinfo('Respuesta', ':( la respuesta fue ' + respuesta)


# def click():
    
#     respuesta =messagebox.askokcancel('Hola Mundo', 'desea realizar la accion?') *devuleve un string
#     if respuesta:
#         messagebox.showinfo('Hola mundo', 'La respuesta fue ok')
#     else:
#         messagebox.showinfo('hola mundo', ' la respuesta fue cancelar')

def click():
    
    respuesta = messagebox.askyesno('popUp', 'desea realizar la accion?')
    print(respuesta)
    if respuesta:
        messagebox.showinfo('Hola mundo', 'La respuesta fue ok')
    else:
        messagebox.showinfo('hola mundo', ' la respuesta fue cancelar')


btn = Button(root, text='Presioname', command=click)
btn.pack()

root.mainloop()