#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
2. Manipular las caracteristicas de la ventana
"""
import tkinter as tk

root = tk.Tk()

# Agregamos un titulo a la ventana
root.title("Ventana TK")

# Modificamos la geometria
root.geometry('600x400+50+50')

# Deshabilitar redimension
root.resizable(False, False)

# Cambiar icono
# root.iconbitmap('ruta del icono')

# Colocar un mensaje dentro de la ventan, con un label
mensaje = tk.Label(root, text="Hola mundo desde TK")
mensaje.pack()

root.mainloop()