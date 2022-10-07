#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
Linea "shebang" o "hashbang"
#!/usr/bin/env python <- Para Linux
1. Definir una función que tome como argumento dos numeros y devuelva el mayor de ellos.
"""
def mayor(n1, n2):
    if n1 < n2:
        print(str(n2) + " es mayor")
    elif n2 < n1:
        print(str(n1) + " es mayor")
    else:
        print("Son iguales")


mayor(3,4)
mayor(6,5)
