import numpy as np
F = 0.6
def GeneraMutante(p,k,g):
    mutante = np.zeros(2)
    mutante[0] = p[0] + F*(k[0] -g[0])
    mutante[1] = p[1] + F*(k[1] -g[1])
    if mutante[0]>500 :
        mutante[0] = 500
    elif mutante[0]<-500:
        mutante[0] = -500
    
    if mutante[1]>500 :
        mutante[1] = 500
    elif mutante[1]<-500:
        mutante[1] = -500
    return mutante
