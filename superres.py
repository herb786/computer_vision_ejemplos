import cv2
from cv2 import dnn_superres

# Inicializar superres
sr = dnn_superres.DnnSuperResImpl_create()
# Cargar imagen
image = cv2.imread('./dolmen.jpg')

# Descargar el modelo requerido
# https://github.com/opencv/opencv_contrib/tree/4.x/modules/dnn_superres
sr.readModel("EDSR_x4.pb")

# Ajustar la escala
sr.setModel("edsr", 4)
# Ampliar imagen
result = sr.upsample(image)

cv2.imwrite("./upscaled.png", result)