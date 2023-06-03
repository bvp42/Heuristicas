import numpy as np
import random
CR = 0.4
def GeneraHijo(p,mutante):
    hijo = np.zeros(2)
    i= random.randint(0,1)
    for j in range(2):
        if random.uniform(0,1)<CR:
            hijo[j]=mutante[j]
        else:
            hijo[j]= p[j]
    hijo[i]=mutante[i]
    return hijo