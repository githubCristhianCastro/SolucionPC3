#PROBLEMA 1

def solicitar_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            x, y = fraccion.split('/')
            x = int(x)
            y = int(y)
            if x >= y and y!= 0:
                raise ValueError
            return x, y
        except ValueError:
            print("Error: X e Y deben ser números enteros, X debe ser mayor o igual a Y, y Y no puede ser cero.")

def calcular_porcentaje(x, y):
    percentage = (x / y) * 100

    if percentage < 1:
        return 'E'
    elif percentage > 99:
        return 'F'
    else:
        return str(round(percentage)) + '%'

while True:
    try:
        x, y = solicitar_fraccion()
        porcentaje = calcular_porcentaje(x, y)
        print("Cantidad de combustible en el tanque:", porcentaje)
        break
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero. .")


#PROBLEMA 2

def ingreso_calificaciones():
    calificaciones_validas = False
    
    while not calificaciones_validas:
        calificaciones = input("Ingrese una lista de calificaciones separadas por comas: ")
        
        try:
            calificaciones_lista = calificaciones.split(',')
            
            calificaciones_enteros = [int(calificacion) for calificacion in calificaciones_lista]
            
            calificaciones_validas = True
        except ValueError:
            print("Error: Asegúrese de ingresar solo valores numéricos separados por comas.")
    
    return calificaciones_enteros

calificaciones = ingreso_calificaciones()
print("Calificaciones ingresadas:", calificaciones)

#PROBLEMA 3

from math import factorial

def Triangulo_Pascal(msg='Ingrese el número de filas del Triángulo de Pascal: '):
    try:
        n=int(input(msg))
        if n>0:
         return n
        else:
         print ('Ingrese un número entero postivo, vuelva a intentar....')
         return Triangulo_Pascal(msg)
    except:
        print('No es un número entero, vuelva a intentar....')
        return Triangulo_Pascal(msg)

n=Triangulo_Pascal()
print(n)

for i in range(n):
            for j in range(n - i + 1):
                print(end =' ')
            for r in range(i + 1):
                numero =  factorial(i) / (factorial(i-r)*factorial(r))
                print(int(numero), end=' ')

            print()  

#PROBLEMA 4

def longitud_ultima_palabra(string):
    try:
        string = string.strip()
        
        palabras = string.split()
        
        ultima_palabra = palabras[-1]
        return len(ultima_palabra)
        return palabras[-1]
    except IndexError:
        return 0

texto = input('Ingrese una frase: ')
longitud = longitud_ultima_palabra(texto)
print("La longitud de la última palabra es: ", longitud)

