#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
7. Definir una función que tome una cadena y un entero como parámetros,
Devuelve las palabras que tengan n caracteres, tomados del entero
"""
def procedimiento(frase, tamanio):
    lista_palabras = frase.split()
    for palabra in lista_palabras:
        if len(palabra) == tamanio:
            print(palabra)


procedimiento("Python es usado en todo el mundo", 5)
