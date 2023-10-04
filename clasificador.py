from __future__ import print_function
import cv2 as cv
import argparse

# Cada imagen pasa por un ciclo de clasificación (Cascade classifier)
# Cada clasificador examina una singularidad o rasgo de la imagen y responde a la pregunta
# mi imagen posee este singularidad?
# Al terminar el ciclo se podrá responder la pregunta
# mi imagen posee todas las singularidades para ser considerada un martillo?

# Usar muestras preparadas y adiestrar modelo
# opencv_createsamples -vec positivos.vec -info anotaciones.txt -bg bg.txt -num 18 -w 80 -h 80
# opencv_traincascade -data martillos/cascada -vec positivos.vec -bg bg.txt -numPos 18 -numNeg 15 -numStages 20 -precalcValBufSize 512 -precalcIdxBufSize 512 -w 80 -h 80

# Crear muestras y adiestrar modelo
# opencv_createsamples -vec positivos.vec -img martillos/img.png -bg bg.txt -num 200
# opencv_traincascade -data martillos/cascada -vec positivos.vec -bg bg.txt -numPos 200 -numNeg 15

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detectar martilols
    martillos = martillo_cascade.detectMultiScale(frame_gray, 1.005, 10)
    for (x,y,w,h) in martillos:
        frame = cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 4)
    cv.imshow('Capture - Hammer detection', frame)


martillo_cascade = cv.CascadeClassifier()

# Cargar el clasificador adiestrados
martillo_cascade.load('martillos/cascada/cascade.xml')

frame = cv.imread('martillos/test.png')
detectAndDisplay(frame)
cv.waitKey()

#python3 clasificador.py