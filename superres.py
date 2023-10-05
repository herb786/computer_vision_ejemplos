import cv2
from cv2 import dnn_superres

# Inicializar superres
sr = dnn_superres.DnnSuperResImpl_create()
# Cargar imagen
image = cv2.imread('./arte/dolmen.jpg')

# Descargar el modelo requerido
# https://github.com/opencv/opencv_contrib/tree/4.x/modules/dnn_superres
sr.readModel("EDSR_x4.pb")

# Ajustar la escala
sr.setModel("edsr", 4)

e1 = cv2.getTickCount()
# Ampliar imagen
result = sr.upsample(image)

e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print( t )

cv2.imwrite("./upscaled.png", result)