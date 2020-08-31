"""

Obtener el valor de salida de la siguiente función matemática:

Entradas:
    x: float
    y: float
    a: float
    b: float
    c: float
Salidas:
    salida: valor resultante de la función

"""

# Capturar las entradas

x = input("Ingrese el valor de x: ")
y = input("Ingrese el valor de y: ")
a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")
c = input("Ingrese el valor de c: ")

x = float(x)
y = float(y)
a = float(a)
b = float(b)
c = float(c)

# Construir la función

salida = ((3+4*x)/5) - ((10*(y-5)*(a+b+c))/x) +  9*(4/x + (9 + x)/y)

print("El valor de la función es {}: ".format(salida))
