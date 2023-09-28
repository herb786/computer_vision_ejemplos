import numpy as np
import cv2 as cv

img = cv.imread('bortnyik04.jpeg')
Z = img.reshape((-1,3))
Z = np.float32(Z)

# Cuantificar colores en 8 aglomeraciones
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret,label,center=cv.kmeans(Z, K, None,criteria,10, cv.KMEANS_RANDOM_CENTERS)

# Recrear la imagen después de colapsar los colores
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv.imshow('res2',res2)
cv.waitKey(0)
cv.destroyAllWindows()