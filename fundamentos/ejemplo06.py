import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# Imagen bajo estudio
img1 = cv.imread('zurbaran/pieza.jpg',cv.IMREAD_GRAYSCALE)
# Imagen para ensayo
img2 = cv.imread('zurbaran/vasijas.jpg',cv.IMREAD_GRAYSCALE)

# Hallar singularidades y sus descriptores
orb = cv.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# Congruencia de singularidades usando fuerza bruta

# Iniciar el buscador de coincidencias
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
# Concordar descriptores.
matches = bf.match(des1,des2)
# Ordenarlos por distancia.
matches = sorted(matches, key = lambda x:x.distance)
# Anotar las primeras 15 congruencias
img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:15],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3),plt.show()