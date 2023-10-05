import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('gustafsson.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Método para hallar singularidades invariantes tras escalamiento
def sift_method():
    sift = cv.SIFT_create()
    kp = sift.detect(gray,None)
    img = cv.drawKeypoints(gray,kp,img)
    cv.imwrite('sift_keypoints.jpg',img)

# Usar el método de Shi-Tomasi para encontrar 30 esquinas sobresalientes 
# con calidad 0.01 
# y una distancia mínima de 10 entre las esquinas
def shi_method():
    corners = cv.goodFeaturesToTrack(gray, 30, 0.01, 50)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv.circle(img,(x,y),10,255,-1)

    plt.imshow(img),plt.show()

# Usar método ORB para hallar singularidades
def orb_method():
    img = cv.imread('gustafsson.jpg', cv.IMREAD_GRAYSCALE)
    orb = cv.ORB_create()
    # Encontrar singularidades
    kp = orb.detect(img,None)
    # Calcular los descriptores
    kp, des = orb.compute(img, kp)
    # Anotar la posición  de las singularidades ignorando el tamaño y la orientación
    img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
    plt.imshow(img2), plt.show()

orb_method()