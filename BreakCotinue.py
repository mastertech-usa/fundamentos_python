"""
    Script que explica Break and While.
    Nota: Este script puede contener errores y es netamente pedagógico. 

"""


#1. Ejemplo encontrar el primer número que es multiplo de n y m en el rango [1,100]
n = 3
m = 13
for val in range(1,101):
    print(val,end="-")
    if val % n == 0 and val % m == 0:
        print("Encontre el número que es multiplo de {} y {}: {}".format(n,m,val))
        break

#  2. La sentencia continue
#  La instrucción continue se usa para omitir el resto del código dentro de un bucle
#  para la iteración actual. El bucle no termina pero continúa con la siguiente iteración.

# Ejemplo contar cuantas vocales hay en un string
print("Ejercicio")
mistring = "Quiero contar las vocales de este string"
vocales = ["a","e","i","o","u"]
numvoca = 0
for caracter in mistring:
    if caracter not in vocales:
        continue
    numvoca += 1
print("El número de vocales en el string es: {}".format(numvoca))

# Imprimir todos los caracteres de un string menos las vocales "o" y "i"

print("Otro Ejercicio")
mistring = "Quiero quitarle las vocales a este string, se podrá leer?"
vocales = ["i","o"]
for caracter in mistring:
    if caracter in vocales:
        continue
    print(caracter,end="")
print("Termino")