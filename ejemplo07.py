import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Imagen bajo estudio
img1 = cv.imread('zurbaran/pieza2.jpg',cv.IMREAD_GRAYSCALE)
# Imagen para ensayo
img2 = cv.imread('zurbaran/vasijas.jpg',cv.IMREAD_GRAYSCALE)

# Iniciar SIFT
sift = cv.SIFT_create()

# Ubicar las singularidades y sus descriptores con SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# Congruencia de singularidades usando fuerza bruta
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)
# Usar la desigualdad de Lowe, para discriminar según la distancia
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3),plt.show()