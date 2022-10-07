#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"
from math import sin,cos,tan,exp,log

"""
10. Escribir una función que reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.
"""

def grade(score):
    if score == 1:
        return 'Insuficiente'
    elif score == 2:
        return 'Aceptable'
    elif score == 3:
        return 'Bueno'
    elif score == 4:
        return 'Muy bueno'
    elif score == 5:
        return 'Excelente'
    else:
        return 'Nro invalido para calificar'

def apply_grade(scores):
    return list(map(grade, scores))

lista_calificaciones = [5, 4, 2, 3, 1, 8]

print(apply_grade(lista_calificaciones))