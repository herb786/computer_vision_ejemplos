import numpy as np
import cv2 as cv

img = cv.imread('digits.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Seccionar la imagen compuestas de 5000 dígitos
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]

# Crear unaa matriz con los dígitos (50,100,20,20)
x = np.array(cells)

# Separemos los datos de partida y los datos de ensayo
train = x[:,:50].reshape(-1,400).astype(np.float32) # Size = (2500,400)
test = x[:,50:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)

# Etiquetemos los datos de partida y los datos de ensayo
k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis]
test_labels = train_labels.copy()

# Inciamos el adiestrador kNN, con k=5
knn = cv.ml.KNearest_create()
knn.train(train, cv.ml.ROW_SAMPLE, train_labels)
ret,result,neighbours,dist = knn.findNearest(test,k=5)

# Verificamos la precisión de la clasificación
matches = result==test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print( accuracy )