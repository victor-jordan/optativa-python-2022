#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
1. Crear una ventana que muestre el mensaje 'Hola mundo'
"""
import tkinter as tk

root = tk.Tk()

# Colocar un mensaje dentro de la ventan, con un label
mensaje = tk.Label(root, text="Hola mundo desde TK")
mensaje.pack()

root.mainloop()