"""

    La princesa Dido tuvo que huir de Roma, perseguida por su propio hermano, y terminó por refugiarse en la 
    costa norte de África, donde le pidió a un rey local que le cediera un terreno en el cual ella pudiera vivir. 
    El rey, con la oportunidad de humillar a una princesa extranjera, accedió a entregarle el terreno que ella deseara, 
    siempre y cuando no fuera mayor a lo abarcado por la piel de un buey. La princesa accedió a la extraña propuesta,
    y el rey le hizo entregar la piel de buey, ofreciéndose acompañarla para oficializar la entrega del terreno.

    Cuál sería su sorpresa cuando la princesa tomó la piel y la cortó en trozos de un milímetro de ancho,
    formando una larga cuerda con la que trazó un círculo gigantesco. Después del curioso trato,
    el rey no tuvo otra opción más que entregarle el terreno, y así fundó la ciudad de Cartago.

Descripción de la Entrada: 
    Su programa debe capturar las dimensiones (largo y ancho, en metros) 
    de la piel de buey –que vamos a asumir cuadrada. Tenga en cuenta que los números de entrada pueden tener 
    decimales, en cuyo caso el separador de decimales será el punto (“.”). 

Descripción De La Salida: 
    La salida en consola será el área total, en kilómetros cuadrados que puede abarcar Dido con la piel de buey ingresada,
    asumiendo que la divide en tiras de un milímetro de grosor para formar una cuerda, y que con esa cuerda forma un círculo perfecto.
    Sólo es necesario un número, no es necesario que especifique que se trata de kilómetros cuadrados.
       
     ______________
  A |              |  
  l |              |
  t |              |
  o |______________|
        Ancho
    
    n = alto (mts)
    m = ancho (mts)
    1 m = 1000 milimetros
    numero de tiras que se pueden cortar = m*1000
    cada tira tiene una longitud de = n
    longitud de la cuerda = n*m*1000 

    El perímetro de un círculo perfecto (longitud de la circunferencia) es 2*Pi*r

    n*m*1000 = 2*Pi*radio

    Necesitamos el radio para calcular el área:
    radio=n*m*1000/2*Pi 

    Con el radio podemos calcular el área del circulo:
    area = Pi * radio^2

    Esta en metros cuadrados, lo debemos pasar a kilometros cuadrados
    1km^2 = 1e6 m^2

    area_km_2 = area / 1e6 
"""
import math

# Capturar las entradas

alto = input("Ingrese el alto de la piel del buey (mts): ")
ancho = input("Ingrese el ancho de la piel del buey (mts): ")

alto = float(alto)
ancho = float(ancho)

# Calcular la longitud de la cuerda

longitud = alto*ancho*1000

# Calcular el radio del circulo con longitud de circuferencia = longi

radio = longitud /(2*math.pi)

# Calcular el area en mts

area = math.pi*radio**2

# Calcular el area en kmts
area_km_2 = area / 1e6

print("El área total, en kilómetros cuadrados que puede abarcar Dido con la piel de buey  es {}: ".format(area_km_2))


