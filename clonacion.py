import cv2 as cv
import numpy as np

#https://docs.opencv.org/4.x/d1/d0d/group__photo.html
#https://learnopencv.com/seamless-cloning-using-opencv-python-cpp/
#https://amroamroamro.github.io/mexopencv/opencv/cloning_demo.html

# imagen de partida
src = cv.imread('arte/src_otorongo.jpg')
# porción de intercambio
mask = cv.imread('arte/mascara_otorongo.jpg')
# imagen de destino
dst = cv.imread('arte/puma.jpg')

#mask = cv.threshold(src, 254, 255, cv.THRESH_BINARY_INV)

# Hallar la caja encerrando la máscara
gray = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
nonzero = cv.findNonZero(gray)
x, y, w, h = cv.boundingRect(nonzero)

# Editar la imagen de destino
p = x + w//2, y + h//2
result = cv.seamlessClone(src, dst, mask, p, cv.NORMAL_CLONE)
cv.imshow('Seamless', result)
cv.waitKey()

#-- python3 clonacion.py