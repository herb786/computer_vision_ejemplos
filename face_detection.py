from __future__ import print_function
import cv2 as cv
import argparse

# Cada imagen pasa por un ciclo de clasificación (Cascade classifier)
# Cada clasificador examina una singularidad o rasgo de la imagen y responde a la pregunta
# mi imagen posee este singularidad?
# Al terminar el ciclo se podrá responder la pregunta
# mi imagen posee todas las singularidades para ser considerada aquel objeto?

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detectar rostros
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- Localizar ojos en el rostro
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Face detection', frame)


face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()

# Cargar los clasificadores adiestrados
face_cascade.load('haarcascade_frontalface_alt.xml')
eyes_cascade.load('haarcascade_eye_tree_eyeglasses.xml')

frame = cv.imread('carlomagno.jpg')
detectAndDisplay(frame)
cv.waitKey()