import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Tamizado de imágenes por promedios deslocalizados
img = cv.imread('zurbaran/taza.jpg')
dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()