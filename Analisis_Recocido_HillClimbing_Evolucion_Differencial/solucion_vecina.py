import random as rnd
import numpy as np

EPSILON = 1

def Solucion_vecina(solucion:np):
    solucion_vecina = np.zeros(2)
    solucion_vecina[0] = solucion[0] + EPSILON * rnd.uniform(-1,1)

    if (solucion_vecina[0]>500):
        solucion_vecina[0] = 500.0
    elif (solucion_vecina[0]<-500):
        solucion_vecina[0] = -500

    solucion_vecina[1] = solucion[1] + EPSILON * rnd.uniform(-1,1)
    if (solucion_vecina[1]>500):
        solucion_vecina[1] = 500
    elif (solucion_vecina[1]<-500):
        solucion_vecina[1] = -500
    
    return solucion_vecina
