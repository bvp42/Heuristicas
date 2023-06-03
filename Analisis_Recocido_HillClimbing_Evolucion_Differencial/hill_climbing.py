import time
import numpy as np
import math
import solucion_inicial as solI
import funcion_objetivo as fO
import solucion_vecina as solV
from solucion_vecina import EPSILON
import random as rnd
import csv

#Se asigna una semilla para replicar los resultados comentar si no se requiere
#semilla = rnd.seed(100000)

#Aqui se debe modificar el parametro epsilon que es el centro
solV.EPSILON = 1


#Arreglo resultados
resultados = [[],[]]

#Se generan las 30 corridas
for i in range(30):
  # Se inicia el conteo del tiempo de ejecución
  Inicia_ejecucion = time.time()

  # Se genera una solución de forma aleatoria
  Solucion_actual = solI.Solucion_Inicial()
  

  # Se calcula su costo
  Costo_actual = np.zeros(2)
  Costo_actual = fO.Funcion_objetivo(Solucion_actual)
  
  # Se realiza un ciclo while para ejecutar el algoritmo
  ciclos=0
  solucion_vecina = np.zeros(2)
  while(ciclos<1000):
    ciclos+=1
    solucion_vecina = solV.Solucion_vecina(Solucion_actual)
    costo_vecina = fO.Funcion_objetivo(solucion_vecina)
    if(costo_vecina<=Costo_actual):
      Costo_actual = costo_vecina
      Solucion_actual = np.copy(solucion_vecina)

  # Se calcula el tiempo de ejecución
  time_sec_V1 = time.time()

  # Se calcula el tiempo empleado
  Tiempo = time.time() - Inicia_ejecucion

  print("\n\nMejor costo encontrado = ", Costo_actual)
  resultados[0].append(Costo_actual)
  #Minimo global 𝑥∗= (420.9687, 420.9687)
  print("Mejor solución encontrada = ",Solucion_actual)
  print("\nEl tiempo de ejcución fue de ",Tiempo, " segundos.")
  resultados[1].append(Tiempo)

#Crea un archivo csv para el analisis
variante = 'variante2.csv'
if(solV.EPSILON==1):
  variante = 'hill_climbing.csv'
with open(variante, 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Costo', 'Tiempo'])
    for i in range(30):
      filewriter.writerow([ str(resultados[0][i]), str(resultados[1][i])] )

