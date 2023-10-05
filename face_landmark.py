import cv2 as cv

#-- Cargar el clasificador
face_cascade = cv.CascadeClassifier()
face_cascade.load('modelos/lbpcascade_frontalface_improved.xml')

#-- Cargar la imagen
frame = cv.imread('arte/howler.jpg')

#-- Cargar el detector de fronteras
facemark = cv.face.createFacemarkKazemi() 
#-- Ruta: opencv/build/share/opencv4/testdata/cv/face/
facemark.loadModel('face_landmark_model.dat')

frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
frame_gray = cv.equalizeHist(frame_gray)
#-- Detectar rostros
faces = face_cascade.detectMultiScale(frame_gray)

#-- Encontrar fronteras
result, landmarks = facemark.fit(frame, faces)

for (x,y,w,h) in faces:
    center = (x + w//2, y + h//2)
    frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
for (x, y) in landmarks[0][0]:
    frame = cv.circle(frame, (int(round(x)), int(round(y))), 4, (0, 0, 255), -1)

cv.imshow('Busqueda Facial', frame)
cv.waitKey()
#-- python3 face_landmark.py