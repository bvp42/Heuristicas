import random as rnd
import numpy as np
def Solucion_Inicial():
    return np.array([rnd.uniform(-500, 500) for i in range(2)])
