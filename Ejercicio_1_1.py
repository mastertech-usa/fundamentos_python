"""
PROBLEMA 1: 

ENUNCIADO: Dados dos números enteros, hallar la suma.

ANÁLISIS: Para la solución de este problema, se requiere que el usuario ingrese dos números enteros y el sistema realice el cálculo respectivo para hallar la suma, para esto se debe usar la siguiente expresión.
Expresión Matemática: suma = numero 1 + numero 2

Entrada: Dos números enteros (números 1 y número 2).

"""

# Capturar los números de entrada por parte del usuario
num_1 = input("Ingrese el primer numero:")
num_2 = input("Ingrese el segundo numero:")

#Suma y realizar type casting
suma = int(num_1) + int(num_2)
print("El resultado de la suma es {}".format(suma))
