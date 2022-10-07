#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"
from math import sin,cos,tan,exp,log

"""
9. Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros desde el 1 al valor introducido y el resultado de aplicar la función a esos enteros.
"""

def apply_math_function(mfunction, number):
	"""
	Función que aplica una función a los enteros desde 1 hasta n.
    Parámetros:
        mfunction: Es una función que recibe un número real y devuelve otro.
        number: Es un número entero positivo.
    Devuelve:
        Un diccionario con los pares i:mfunction(i) para cada valor entero i de 1 a n.
	"""
	functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
	result = {}

	for i in range(1, number+1):
		result[i] = functions[mfunction](i)

	return result


def calculator():
	"""
	Función que aplica una función seleccionada por el usuario (seno, coseno, tangente, exponencial o logarítmo) a la lista de enteros desde 1 hasta n. 
    Imprime por pantalla una tabla con la secuencia de enteros y el resultado de aplicarles la función introducida.
	"""
	capture_function = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')
	capture_number = int(input('Introduce un entero positivo: '))

	for i, j in apply_math_function(capture_function, capture_number).items():
		print(str(i) + ".-", '\t', j)
	return

calculator()