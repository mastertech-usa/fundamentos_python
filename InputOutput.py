"""
Programa para explicar los operadores básicos de entrada/salida en python I/O y el import.  

1. input() Función para capturar datos del usuario (Entrada)
2. print() Función para imprimir datos en consola (Salida)

"""


#1. Función de salida print
print("Un string de salida a terminal")

a = 234
print("El valor de la variable a es:", a)

#Mejorando el formato de salida con str.format()
b = 554
print('El valor de a es {} y el de b es {}'.format(a,b)) # {} son marcadores de posición (placeholders)

#placeholder nombrados
print('Mi apellido es {lastname} y mi nombre es {firtsname}'.format(lastname = 'Manrique', firtsname = 'Ruben')) # {} son marcadores de posición (placeholders)

#2. Función de entrada input()

num = input('Ingrese un número por favor: ')
print(num)
print(type(num))
#Por defecto la información capturada es str.

#3. Import
# Cuando nuestro programa es grande es conveniente dividirlo en módulos. Cada módulo
# contendra funciones y definiciones que podremos utilizar despues.
# Cuando necesitemos utilizar funciones de un módulo lo debemos importar

import math
# https://docs.python.org/3/library/math.html
print(math.pi)
print(math.fabs(-12))
print(math.factorial(5))