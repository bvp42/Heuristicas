import time
import numpy as np
import math
import solucion_inicial as solI
import funcion_objetivo as fO
import solucion_vecina as solV
import genera_mutante as gM
import hijo_mutante as hM
from solucion_vecina import EPSILON
from genera_mutante import F
from hijo_mutante import CR
import random as rnd
import csv
import math

# Se asigna una semilla para replicar los resultados comentar si no se requiere
#semilla = rnd.seed(100000)

# Aqui se debe modificar el parametro epsilon que es el centro
solV.EPSILON = 1

#Se declara el factor de mutacioin y la taza de Cruza
gM.F = 0.6
hM.CR = 0.4


costo_hijo = None

#Arreglo resultados
resultados = [[],[]]

#Se generan las 30 corridas
for i in range(30):
    # Generar una poblacion aleatoria
    p = np.zeros((13, 2))
    for i in range(13):
        aux = solI.Solucion_Inicial()
        p[i][0] = aux[0]
        p[i][1] = aux[1]

    #Generamos sus costos
    costo = np.zeros(13)
    for i in range(13):
        costo[i] = fO.Funcion_objetivo([p[i][0],p[i][1]])

    # Se inicia el conteo del tiempo de ejecución
    Inicia_ejecucion = time.time()

    for n in range(500):
        for m in range(13):

        #Generar 3 aleatorios
            num_posibles = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
            num_posibles = num_posibles[num_posibles !=m]
            
            num_rnd = np.array([-1,-1,-1])
            for k in range(3):
                num_rnd[k] = rnd.choice(num_posibles)
                num_posibles = num_posibles[num_posibles != num_rnd[k]]
            
            mutante = gM.GeneraMutante(p[num_rnd[0]],p[num_rnd[1]],p[num_rnd[2]])
            hijo = hM.GeneraHijo(p[m],mutante)
            costo_hijo = fO.Funcion_objetivo(hijo)
            if(costo_hijo<=costo[m]):
                p[m][0] = hijo[0]
                p[m][1] = hijo[1]
                costo[m] = costo_hijo
    mejor_costo = costo[0]
    posicion = 0
    for j in range(1,13):
        if(costo[j]<mejor_costo):
            mejor_costo = costo[j]
            posicion = j
    
    # Se calcula el tiempo empleado
    tiempo = time.time() - Inicia_ejecucion
    print("\n\nMejor costo encontrado = ", mejor_costo)
    #Minimo global 𝑥∗= (420.9687, 420.9687)
    print("Mejor solución encontrada = ",p[posicion])
    print("El tiempo de ejcución fue de ",tiempo, " segundos.")
    resultados[0].append(mejor_costo)
    resultados[1].append(tiempo)

#Crea un archivo csv para el analisis
variante = "evol_dif.csv"
with open(variante, 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Costo', 'Tiempo'])
    for i in range(30):
      filewriter.writerow([ str(resultados[0][i]), str(resultados[1][i])] )





