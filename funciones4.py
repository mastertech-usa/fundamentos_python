"""
    Script4 para explicar funciones en Python.
    Variable globales y locales

"""

# 1. Como accesso variables globales? en funciones cuyo alcance es meramente local

x = "global" #Variable global
print(x)
def foo():
    global x # Indico que quiero manipular la variable global x definida anteriormente
    y = "local" #Y es una varaible local
    x = "Modifico una variable  global en un alcance local"
    print(x)
    print(y)
    
foo()
print(x)