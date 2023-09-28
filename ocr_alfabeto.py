import cv2 as cv
import numpy as np

# http://archive.ics.uci.edu/dataset/59/letter+recognition
# Cargar datos y mapear las letras con números
data= np.loadtxt('letter-recognition.data', dtype= 'float32', delimiter = ',', converters= {0: lambda ch: ord(ch)-ord('A')})

# Crear 1000 datos de partida y 1000 de ensayo
train, test = np.vsplit(data,2)

# Separar las singularidades de las respuestas
responses, trainData = np.hsplit(train,[1])
labels, testData = np.hsplit(test,[1])

# Iniciar el adiestrador
knn = cv.ml.KNearest_create()
knn.train(trainData, cv.ml.ROW_SAMPLE, responses)
ret, result, neighbours, dist = knn.findNearest(testData, k=5)
correct = np.count_nonzero(result == labels)
accuracy = correct*100.0/10000
print( accuracy )