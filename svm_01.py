import cv2 as cv
import numpy as np

def linear(xy):
    if (xy[1] < 500 - xy[0]):
        return 1
    else:
        return -1

# Crear datos de partida
#trainingData = np.matrix([[501, 10], [255, 10], [501, 255], [10, 501]], dtype=np.float32)
centers = np.random.randint(500,size=(100,2))
trainingData = centers.astype(np.float32)
print(trainingData)
labels = np.array(list(map(linear,trainingData)))

# Adiestrar el modelo con vectores auxiliares
svm = cv.ml.SVM_create()
svm.setType(cv.ml.SVM_C_SVC)
svm.setKernel(cv.ml.SVM_LINEAR)
svm.setTermCriteria((cv.TERM_CRITERIA_MAX_ITER, 100, 1e-6))
svm.train(trainingData, cv.ml.ROW_SAMPLE, labels)

# Gráfico
width = 512
height = 512
image = np.zeros((height, width, 3), dtype=np.uint8)

# Visualizar las regiones clasificadas
green = (0,255,0)
blue = (255,0,0)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        sampleMat = np.matrix([[j,i]], dtype=np.float32)
        response = svm.predict(sampleMat)[1]
        if response == 1:
            image[i,j] = green
        elif response == -1:
            image[i,j] = blue

# Visualizar los datos de partida
thickness = -1
centers = np.vstack((labels,np.transpose(centers)))
for x in np.transpose(centers):
    print(x)
    if (x[0] > 0):
        cv.circle(image, (x[1], x[2]), 4, (0, 0, 0), thickness)
    else:
        cv.circle(image, (x[1], x[2]), 4, (255, 255, 255), thickness)

# Mostrar los vectores auxiliares
thickness = 2
sv = svm.getUncompressedSupportVectors()
for i in range(sv.shape[0]):
    cv.circle(image, (int(sv[i,0]), int(sv[i,1])), 6, (0, 0, 255), thickness)
cv.imwrite('result.png', image) # save the image
cv.imshow('SVM Simple Example', image) # show it to the user
cv.waitKey()