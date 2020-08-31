"""
PROBLEMA 2:

ENUNCIADO: Dado dos números obtener el cociente y el residuo.

ANÁLISIS: Para la solución de este problema, se requiere que el usuario ingrese dos números enteros 
 (Dividendo y Divisor) y el sistema debe realizar el cálculo respectivo para hallar el cociente y el residuo. 
 Para esto se debe usar la siguiente expresión:

Cociente = Dividendo / divisor.
Residuo = dividendo % divisor

"""

# Capturar las entradas
dividendo = input("Por favor ingrese el dividendo: ")
divisor = input("Por favor ingrese el divisor: ")

dividendo = int(dividendo)
divisor = int(divisor)
# Calcular cociente y residuo

cociente = dividendo // divisor
residuo = dividendo % divisor

print("El conciente de la division es {}, y el residuo es {}".format(cociente,residuo))

