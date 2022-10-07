#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
13. Escribir una función que pida un numero entero determinado por el usuario, a partir de ese rango guardar en un archivo de nombre 'tabla_numero.txt' la tabla de multiplicar de ese numero.
"""

numero = int(input('Introduce un numero mayor a cero: '))

nombre_archivo = 'tabla_del_' + str(numero) + '.txt'

archivo = open(nombre_archivo, 'w')

for indice in range(1, 13):
    registro = str(numero) + ' x ' + str(indice) + ' = ' + str(numero*indice) + '\n'
    archivo.write(registro)

archivo.close()