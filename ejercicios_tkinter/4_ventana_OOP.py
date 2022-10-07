#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
4. Aplicar enfoque POO con Tkinter para tener un codigo más organizado
"""
import tkinter as tk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    """
    Aplicacion TK con enfoque POO
    """
    def __init__(self):
        super().__init__()

        # Ventana raiz
        self.title('Ventana con enfoque OOP')
        self.geometry('500x80')

        # Labels
        self.label= tk.Label(self, text='Hola Tkinter')
        self.label.pack()

        # Butons
        self.button = tk.Button(self, text='Click')
        self.button['command'] = self.click_boton
        self.button.pack()

    def click_boton(self):
        showinfo(title='Informacion', message='Hola mundo')


if __name__ == "__main__":
    aplicacion = App()
    aplicacion.mainloop()