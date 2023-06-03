import math
import numpy as np

def Funcion_objetivo(solucion:np):
    #Funcion de Schwefel para dos variables
    f = lambda x,y : 418.9829 * 2 - x * math.sin(math.sqrt(abs(x))) -y * math.sin(math.sqrt(abs(y)))
    return f(solucion[0],solucion[1])