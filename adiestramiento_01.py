# Adiestramiento computacional - Machine Learning
# Clasificación por proximidad a datos confinantes.
# Algoritmo de vecinos aledaños -  k-Nearest Neighbour (kNN).

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Recrear 50 puntos de partida con coordenadas entre 0 y 100
trainData = np.random.randint(0,100,(50,2)).astype(np.float32)

# Etiquetar cada par de coordenadas con 2 para rojo, 1 para los azul, 0 para verde
responses = np.random.randint(0,3,(50,1)).astype(np.float32)

# Graficar coordenadas rojas
red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'g','^')

# Graficar coordenadas azules
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

# Graficar coordenadas verdes
green = trainData[responses.ravel()==2]
plt.scatter(green[:,0],green[:,1],80,'r','*')

# Agregar un nuevo par de coordenadas
newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'k','o')

# Iniciar el adiestrador de modelos
knn = cv.ml.KNearest_create()
knn.train(trainData, cv.ml.ROW_SAMPLE, responses)

# Encontrar los 5 colindantes a la nueva coordenada
ret, results, neighbours ,dist = knn.findNearest(newcomer, 5)

# Graficar círculo encerrando las 5 coordenadas
distance = np.sqrt(dist[0][4])
an = np.linspace(0, 2 * np.pi, 100)
plt.plot(newcomer[0][0]+ distance * np.cos(an), newcomer[0][1]+ distance * np.sin(an), 'tab:orange')

print( "result:  {}\n".format(results) )
print( "neighbours:  {}\n".format(neighbours) )
print( "distance:  {}\n".format(dist) )
plt.show()