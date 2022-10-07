#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
4. Escribir una función cuente las vocales de una frase.
"""
def contador_vocales(frase):
    contador = 0
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letra in frase:
        if letra in vocales:
            contador +=1

    return contador

frase = "el veloz murcielago, vuela alto en la montaña"
cadena = "Una cadena"

print("frase: " + str(contador_vocales(frase)))
print("cadena: " + str(contador_vocales(cadena)))
