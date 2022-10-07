#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
11. Escribir una función que reciba una frase y devuelva un diccionario con las palabras y su longitud.
"""


def longitud_palabras(frase):
    palabras = frase.split()
    longitud = map(len, palabras)
    return dict(zip(palabras, longitud))


frase = "Hola mundo desde Python!"

print(longitud_palabras(frase))
