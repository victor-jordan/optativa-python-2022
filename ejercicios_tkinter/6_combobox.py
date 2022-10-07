#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
6. Mostrar como generar un combobox
"""

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name


root = tk.Tk()

root.geometry('500x300')
root.resizable(False, False)
root.title('Ejemplo Combobox')

label = ttk.Label(text='Selecciona un mes: ')
label.pack(fill=tk.X, padx=5, pady=5)

mes_seleccionado = tk.StringVar()
combobox = ttk.Combobox(root, textvariable=mes_seleccionado)

# utilizamos slice de python para obtener solo las 3 primeras letras
combobox['values'] = [month_name[m][0:3] for m in range(1, 13)]

combobox['state'] = 'readonly'
combobox.pack(fill=tk.X, padx=5, pady=5)


def cambia_opcion(evento):
    showinfo(
        title='Resultado',
        message=f'Seleccionaste {mes_seleccionado.get()}'
    )


combobox.bind('<<ComboboxSelected>>', cambia_opcion)

root.mainloop()
