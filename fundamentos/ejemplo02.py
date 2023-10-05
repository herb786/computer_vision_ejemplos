import numpy as np
import cv2 as cv

# Mostrar todo los eventos disponibles
events = [i for i in dir(cv) if 'EVENT' in i]
print( events )

drawing = False # true si hace click izquierdo
mode = True # True para dibujar rectángulo. Aprieta 'm' para conmutar a curvas
ix,iy = -1,-1

# Función de trazado
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)


# Canvas con fondo negro
img = np.zeros((512,512,3), np.uint8)
# Ventana para el canvas
cv.namedWindow('image')
# Dibujar elipse en el canvas
cv.ellipse(img,(256,256),(100,50),0,0,270,255,-1)
# Dibujar polígono
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
# Agregar texto al canvas
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
#Evento del ratón compuesto con la función de trazado
cv.setMouseCallback('image',draw_circle)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        # Luego de pulsar ESCape
        break
cv.destroyAllWindows()