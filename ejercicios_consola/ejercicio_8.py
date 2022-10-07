#!"C:\Users\Administrador\AppData\Local\Programs\Python\Python38\python.exe"

"""
8. Escribir una función que aplique un porcentaje de descuento a un precio y otra que aplique el IVA, escribir otra función que reciba un diccionario con los precios y porcentajes de una canasta de compras y una de las funciones anteriores, utilizar la función para el descuento o el IVA a los productos de la canasta y devolver el precio total final.
"""

def apply_discount(price, percentage):
    """
    Función que aplica un descuento a un precio.
    Parámetros:
      price: es el valor real al cual aplicamos el descuento.
      percentage: es el porcentaje a descontar del valor real.
    Devuelve:
      El precio final con descuento.
    """
    return int(price - (price * percentage) / 100)


# print(apply_discount(5000, 10))

def apply_task(price, percentage):
    """
    Función que aplica un IVA a una cantidad.
    Parámetros:
        price: Es un valor real con el precio al que aplicar el IVA.
        percentage: Es el porcentaje del IVA a aplicar.
    Devuelve:
        El precio final tras aplicar el IVA.
    """
    return int(price + (price * percentage) / 100)

# print(apply_task(5000, 10))

def final_buy(basket, function):
    """
    Función que calcula el precio de una canasta de la compra una vez aplicada una función a los precios iniciales.
    Parámetros:
        basket: Es un diccionario formado por pares precio:descuento.
        function: Es una función que toma dos valores reales y devuelve otro. Normalmente para aplicar descuentos o IVA.
    Devuelve:
        El precio final de la canasta de la compra una vez aplicada la función sobre los precios iniciales.
    """
    total = 0
    for price,discount in basket.items():
        total += function(price, discount)
    return total

canasta = {10000:20, 500:10, 20000:5, 8000:15}

print('Canasta con descuento: ', final_buy(canasta, apply_discount))
print('Canasta con IVA: ', final_buy(canasta, apply_task))
