#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
2. Definir una función que tome tres numeros, debe devolver el mayor y el menor de ellos.
"""
def mayor_menor_de_tres(n1,n2,n3):
    if n1 > n2 and n1 >n3:
        print("el mayor es " + str(n1))
    elif n2 > n1 and n2 > n3:
        print("el mayor es " + str(n2))
    elif n3 > n1 and n3 > n2:
        print("el mayor es " + str(n3))
    else:
        print("Son iguales")


mayor_menor_de_tres(18, 12, 10)
mayor_menor_de_tres(4, 999, 55)
mayor_menor_de_tres(11, 11, 27)
mayor_menor_de_tres(11, 11, 11)
