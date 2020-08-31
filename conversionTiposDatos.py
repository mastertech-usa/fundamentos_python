"""
Programa para explicar conversiones entre tipos de datos en python.
Nota: El código aquí presentado presenta errores!!, el proposito de este script es totalmente pedagógico. 

La conversión entre tipos de datos en python ocurre de dor formas:
1. Conversión implicita. (La realiza Python en tiempo de ejecución)
2. Conversión explicita. (El programador la definio)

"""

#1. Conversión implicita
num_int = 4
num_float = 1.5
# Que tipo de dato sera asignado a la varaible que recibe la suma de num_int y num_float?
sum_nums = num_int + num_float
print(sum_nums)
print(type(sum_nums)) #El resultante es un Float. 
#Promoción de tipos en los lenguajes de programación para evitar la perdida de inf.

#2. Conversión explicita (Type Casting)
#2.1.Conversión en tipos de datos primitivos: Integers, Float, Strings, Boolean

a_int = 4
b_int = 6
c_sum = a_int + b_int
print("Valor de c_sum:",c_sum," Tipo de dato c_sum:", type(c_sum)) #Algo nuevo: Multiples valores de impresión!!!

c_float_sum = float(a_int + b_int) #Funcion float.
print("Valor de c_float_sum:",c_float_sum," Tipo de dato c_float_sum:", type(c_float_sum)) 
#int->float no hay perdida de inf.

a_float = 4.3
b_float = 6.0
c_sum = a_float +b_float
print("Valor de c_sum:",c_sum," Tipo de dato c_sum:", type(c_sum)) 

c_int_sum = int(a_float + b_float)
print("Valor de c_int_sum:",c_int_sum," Tipo de dato c_int_sum:", type(c_int_sum)) 

#Para conversiones a partir de strings si contienen valores compatibles.
a_str = "23"
b_str = "3.1"
c_sum = a_str + b_str
print("Valor de c_sum:",c_sum," Tipo de dato c_sum:", type(c_sum)) 

c_str_float_sum = float(a_str) + float(b_str)
print("Valor de c_str_float_sum:",c_str_float_sum," Tipo de dato c_str_float_sum:", type(c_str_float_sum)) 

#Valores no compatibles
int(b_str)
int("10,2")
float("10,2")
float("sss")

#2.2.Conversión en tipos de datos no primitivos. Colleciónes: Dict, Tuple, List, Set

#Conversión de listas a tuplas (transformación natural)

a_tuple = (1,1,1,1,2,3,4,5,6,7,8,9,10)
b_list = [1,2,4,5,12,2,3,4,5]

print(tuple(b_list)) #Funcion tuple
print(list(a_tuple)) #Funcion list

#Conversión de string a lista o tupla
miString = "Este es el curso de Intro a Python"
print(tuple(miString))
print(list(miString))

#Conversión de listas y tuplas a set (aplica en sentido inverso)
print(set(a_tuple))
print(set(b_list))

#Conversión a diccionario (solo colecciones de pares de elementos)
ejem1 = [[1,2],[3,4]] #Esto es una lista de listas (lista anidada). La listas anidadas contienen dos elementos.
ejem2 = [(1,2),(3,4)] #Esto es una lista de tuplas. Las tuplas contienen dos elementos.

#Como acceder a una lista anidada
print(ejem1)
print(ejem1[0])
print(ejem1[0][0])

print(ejem2[0][1])
#Como convertirla a un diccionario
print(dict(ejem1))
print(dict(ejem2))






