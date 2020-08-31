"""

PROBLEMA 4:

ENUNCIADO: Crear un programa para encontrar el área de un círculo.

Entradas:
    radio: radio del circulo
Salidas:
    area: Area del circulo

Expresión Matemática:
    area = Pi*radio^2

"""

# Capturar las entradas
radio = input("Por favor ingrese el radio del circulo:")
radio = float(radio)

#Calcular el area
import math

area = math.pi*radio**2

print("El área del circulo con radio {}, es {}".format(radio,area))