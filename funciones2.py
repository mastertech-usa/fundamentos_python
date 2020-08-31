"""
    Script2 para explicar funciones en Python.
    Argumentos

"""

# 1. Considere la siguiente función

def suma_lista(lista):
    """Esta función  suma los números de una lista
        
        Parameters:
        lista : Lista con números

        Return:
        suma: suma de los elementos de la lista
    """
    suma = 0
    for elem in lista:
        suma += elem
    return suma

milista = [12.5,10,13.4,13.22,7,2.34]
print(suma_lista(milista)) # En este llamado el argumento es milista y es OBLIGATORIO 

# Que pasa si no envio el argumento
# suma_lista()

# 2. Valores por defecto

def suma_lista2(lista = [1,2,3]):
    """Esta función  suma los números de una lista
    La diferencia con la anterior función es que en esta el parametro lista
    tiene un valor por defecto, por lo tanto cuando llamemos a esta función
    los argumentos son opcionales.
        
        Parameters:
        lista : Lista con números

        Return:
        suma: suma de los elementos de la lista
    """
    suma = 0
    for elem in lista:
        suma += elem
    return suma

milista = [12.5,10,13.4,13.22,7,2.34]
print(suma_lista2(milista)) # Con argumento
print(suma_lista2()) #Sin argumento, ahora si se puede pq hay un valor por defecto en la definición del parametro.


# 3. Funciones definidas con multiples parametros/LLamados con multiples argumentos

def elimina_caracteres(texto,eliminar = ["a","e","i","o","u"]):
    """Esta función elimina de un texto un conjunto de caracteres.
        
        Parameters:
        texto : String con texto del cual se quiere eliminar caracteres
        eliminar: Lista con los caracteres que quiero eliminar.

        Return:
        textopro: Texto sin los caracteres que se especificaron.
    """
    textopro = ""
    for caracter in texto:
        if caracter not in eliminar:
            textopro = textopro + caracter
    return textopro

mi_texto = "Colombia"

print(elimina_caracteres(mi_texto)) # Un solo argumento

print(elimina_caracteres(mi_texto,["l"])) # Multiples argumentos asignados por posición!!!


#4. Python definición de argumentos por palabra clave

result1 = elimina_caracteres(texto=mi_texto, eliminar=["l"]) # Todos los argumentos deben ir definidos por palabra clave
result2 = elimina_caracteres(eliminar=["l"],texto=mi_texto) # Diferente orden

print(result1, " ", result2)

# elimina_caracteres(texto=mi_texto, ["l"]) # Error