import math
import os
import sys

from MATHSS import operaciones

MENSAJE_PRINCIPAL ='Bienvenido al menú interactivo'
MENU_OPCIONES="""
¿Qué quieres hacer? Escribe una opción
    1) Calcular la suma de 2 números
    2) Calcular la resta de 2 números
    3) Calcular el producto de 2 números
    4) Calcular la división de 2 números
    5) Salir
"""
def validar_ingreso_numero_decimal(msg='Ingrese un número entero: ')->float:
   try:
      n=float(input(msg))
      return n
   except:
      print('No es un número, vuelva a intentar....')
      return validar_ingreso_numero_decimal(msg)

print(MENSAJE_PRINCIPAL)
while True:
    opcion = input(MENU_OPCIONES)
    if opcion == '1':
        n1 = validar_ingreso_numero_decimal('Introduce el primer número: ')
        n2 = validar_ingreso_numero_decimal('Introduce el segundo número: ')
        resultado_suma= operaciones.suma(n1, n2)
        print(f"{n1} + {n2} = {resultado_suma}") 

    elif opcion == '2':
        n1 = validar_ingreso_numero_decimal('Introduce el primer número: ')
        n2 = validar_ingreso_numero_decimal('Introduce el segundo número: ')
        resultado_resta=operaciones.resta(n1,n2)
        print(f'{n1} - {n2} = {resultado_resta}')

    elif opcion =='3':
        n1 = validar_ingreso_numero_decimal('Introduce el primer número: ')
        n2 = validar_ingreso_numero_decimal('Introduce el segundo número: ')
        resultado_producto=operaciones.producto(n1,n2)
        print(f'{n1} * {n2} = {resultado_producto}')

    elif opcion =='4':
        n1 = validar_ingreso_numero_decimal('Introduce el primer número: ')
        n2 = validar_ingreso_numero_decimal('Introduce el segundo número: ')
        resultado_division=operaciones.division(n1,n2) 
        print(f'{n1} / {n2} = {resultado_division}')

    elif opcion =='5':
        print('¡Hasta luego! Ha sido un placer ayudarte')
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
      