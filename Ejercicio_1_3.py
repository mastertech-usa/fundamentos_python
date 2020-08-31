"""

PROBLEMA 3

ENUNCIADO: Dado el valor de venta de un producto, hallar el Ingreso General a las Ventas (19%) y el
             precio de Venta
ANÁLISIS: Para la solución de este problema, se requiere que el usuario ingrese el valor de la venta del producto 
            y el sistema realice el cálculo respectivo para hallar el Ingreso General a las Ventas y el precio 
            de venta.

Entradas:
    vv: Valor de Venta
Salidas:
    Igv: Ingreso General a las Ventas
    Pv: El precio de Venta

Expresión Matemática:
    Igv = vv * 0.19
    Pv = vv + igv

"""

# Capturar las entradas
vv = input("Defina el valor de venta:")
vv = float(vv)

#Calcular Igv y Pv
igv = vv * 0.19
pv = vv + igv

print("El ingreso general a las ventas es {}, y el precio de venta es {}".format(igv,pv))

