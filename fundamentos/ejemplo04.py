import cv2 as cv

img1 = cv.imread('zurbaran/vasijas.jpg')
assert img1 is not None, "file could not be read, check with os.path.exists()"
# Número de ciclo transcurrido antes de comenzar
e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
# Número de ciclos trancurridos al finalizar
e2 = cv.getTickCount()
# El tiempo transcurrido se halla dividiendo por la frecuencia de la máquina
t = (e2 - e1)/cv.getTickFrequency()
print( t )

print(cv.useOptimized())
e1 = cv.getTickCount()
res = cv.medianBlur(img1,49)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )

cv.setUseOptimized(False)
e1 = cv.getTickCount()
res = cv.medianBlur(img1,49)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )