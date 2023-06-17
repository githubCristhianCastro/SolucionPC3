import random

def generar_numeros_aleatorios():
    numeros_aleatorios = []
    for _ in range(20):
        numero = random.randint(0, 100)
        numeros_aleatorios.append(numero)
    return numeros_aleatorios

def mostrar_lista(lista):
    print("Lista de números aleatorios:")
    for numero in lista:
        print(numero)

def ordenar_lista(lista):
    lista.sort()
    print("Lista ordenada:")
    for numero in lista:
        print(numero)