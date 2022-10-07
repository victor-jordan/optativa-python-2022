#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
5. Definir una función que invierta una cadena dada.
"""
def inversor(frase):
    longitud = len(frase)
    invertida = ""
    indice = -1
    while longitud >= 1:
        invertida += frase[indice]
        indice += -1
        longitud -= 1

    return invertida

frase = "el veloz murcielago, vuela alto en la montaña"
cadena = "Una cadena"

print("frase: " + inversor(frase))
# print("cadena: " + str(contador_vocales(cadena)))
