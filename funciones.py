"""
    Script para explicar funciones en Python.

"""


#1. Definición básica.

def buenosdias(nombre):
    """Esta función  le desea buenos días a una persona.
        
        Parameters:
        nombre : String con nombre de persona

        Return:
        None
    """
    print("Buenos días!, ",  nombre )


#2. Llamado

minombre = "Superman López"
buenosdias(minombre) #Agumentos


#3. Return

# La declaración return se usa para salir de una función y volver al lugar desde donde se llamó.
# Esta declaración puede contener expresiones que se evalúan y devuelven un valor. 
# Si no hay expresión en la declaración o la declaración de retorno en sí no está presente dentro de una función,
# entonces la función devolverá el objeto None.

# Python Doc: The None keyword is used to define a null.

minombre = "Rigoberto"
print(buenosdias(minombre))


def buenasnoches(nombre):
    """Esta función  le desea buenos días a una persona.
        
        Parameters:
        nombre : String con nombre de persona

        Return:
         String -Es hora de descansar-
    """
    print("Buenas noches!, ",  nombre )

    return "Es hora de descansar"

minombre = "Rigoberto"
print(buenasnoches(minombre))




def valor_absoluto(num):
    """Esta función retorna el valor absoluto
    de un número real.

        Parameters:
        num : Float

        Return:
         num : Float con valor absoluto 
    
    """
    if num >= 0:
        return num
    else:
        return -num

print(valor_absoluto(-120.03))

#4. Alcance y yiempo de vida de las variables

# El alcance de una variable es la parte de un programa donde se reconoce la variable. 
# Los parámetros y variables definidos dentro de una función no son visibles desde el exterior. 
# Por lo tanto, tienen un alcance local.

# El tiempo de vida de una variable es el período durante el cual la variable esta referenciada en memoria. 
# El tiempo de vida de una variable dentro de una función es tan larga como la ejecución de la función.


def funcion_prueba():
    """Esta función sirve para explicar el alcance y tiempo de vida de una variable
        en una función.
    """
    variable = 1230
    print("Valor dentro de la función:",variable)

variable = 3450
funcion_prueba()
print("Valor fuera de la función:",variable)

## Revisar en http://www.pythontutor.com/visualize.html#mode=edit