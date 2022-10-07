#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
3. Escribir una aplicación que tome un dato numerico expresado en Fahrenheit y convertirlo a Celsius.
"""
import tkinter as tk
from tkinter.messagebox import showerror


def convertir(f):
	"""
	Conviete el numero enviado (f) a Celsius (c)
	"""
	c = (f - 32) * 5 / 9
	return c


def comando_click_boton():
	"""
	Maneja el evento click del boton para convertir
	"""
	try:
		f = float(temperatura.get())
		c = convertir(f)
		resultado = f'{f} Fahrenheit = {c:.2f} Celsius'
		celsius_label.config(text=resultado)
	except ValueError as error:
		showerror(title='Error', message=error)


root = tk.Tk()

# Agregamos un titulo a la ventana
root.title("Convertidor de Temperaturas")

# Modificamos la geometria
root.geometry('500x80')

# Deshabilitar redimension
root.resizable(False, False)

# Generamos el contenedor
frame = tk.Frame(root)

# opciones para los elementos del formuluario
options = {'padx': 5, 'pady': 5}

# Etiqueta de temperatura a convertir
temp_label = tk.Label(frame, text='Grado en Fahrenheit: ')
temp_label.grid(column=0, row=0, sticky='W', **options)

# Campo de texto para ingresar el valor a convertir
temperatura = tk.StringVar()
temp_txtb = tk.Entry(frame, textvariable=temperatura)
temp_txtb.grid(column=1, row=0, **options)
temp_txtb.focus()

# Boton para realizar la conversión, deberá llamar a la función
temp_button = tk.Button(frame, text='Convertir a Celsius')
temp_button.grid(column=2, row=0, sticky='W', **options)
temp_button.configure(command=comando_click_boton)

# Label para mostrar el resultado
celsius_label = tk.Label(frame)
celsius_label.grid(row=1, columnspan=3, **options)

# Dar forma al contenedor
frame.grid(padx=10, pady=10)

# Iniciamos la app
root.mainloop()