#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
12. Escribir una función que reciba otra función y una lista. Debe devolver otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista enviada.
"""
def elevar_cuadrado(numero):
    return numero * numero

def aplicar_funcion_lista(funcion, lista):
    otra_lista = []
    for elemento in lista:
        otra_lista.append(funcion(elemento))
    return otra_lista

lista_numeros = [1,2,3,4,5,6,7,8]
print(aplicar_funcion_lista(elevar_cuadrado, lista_numeros))