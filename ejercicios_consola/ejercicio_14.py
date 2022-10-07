#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
14. Escribir una función que pida dos numeros numero y linea, debe leer el archivo 'tabla_del_numero.txt' y con el archivo abierto, nos muestr por pantalla la linea del archivo. Si no existe el archivo o la linea, debe mostrar un mensaje informando de ese error.
"""

numero = int(input('Introduce el numero de la tabla para visualizar: '))
linea = int(input('Introduce la linea a visualizar: '))

nombre_archivo = 'tabla_del_' + str(numero) + '.txt'

try:
    with open(nombre_archivo, 'r') as a:
        registros = a.readlines()
    print(registros[linea - 1])
    a.close()
except FileNotFoundError:
    print('No existe el archivo con la tabla del', numero)

