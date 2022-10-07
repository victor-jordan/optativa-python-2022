#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
3. Definir una función que calcule la longitud de una cadena dada.
"""
# cadena = "Una cadena"
# print(len(cadena))

def largo_cadena(cadena):
    contador = 0
    for letra in cadena:
        contador +=1

    return contador

frase = "el veloz murcielago, vuela alto en la montaña"

print("con funcion: " + str(largo_cadena(frase)))
print("con len: " + str(len(frase)))
