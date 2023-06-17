import math

def sumar(x:float,y:float)->float:
    try:
        resultado = x+y
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def restar(x:float,y:float)->float:
    try:
        resultado = x-y
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"


def producto(x:float,y:float)->float:
    try:
        resultado = x*y
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def division(x:float,y:float)->float:
    try:
        if y!=0:
         resultado = x/y
         return resultado
        else:
         return "Error: No es posible dividir entre cero"
    except ValueError:
        return "Error: Tipo de dato no válido"



