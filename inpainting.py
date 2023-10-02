import numpy as np
import cv2 as cv

# Remiendo de imágenes con colores circundando los defectos
img = cv.imread('alcira01.jpeg')
mask = cv.imread('mascara.jpg', cv.IMREAD_GRAYSCALE)
# Método basado en la ecuación de la eikonal
#dst = cv.inpaint(img,mask,3,cv.INPAINT_TELEA)
# Método basado en la ecuación de continuidad de Navier-Stokes
dst = cv.inpaint(img,mask,3,cv.INPAINT_NS)

cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()