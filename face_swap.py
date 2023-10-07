import cv2 as cv
import numpy as np

def inRect(box, point):
    x, y, w, h = box
    px, py = point
    if (px >= x) and (px <= x+ w) and (py >= y) and (py <= y + h):
        return True
    return False

#-- Cargar el clasificador
face_cascade = cv.CascadeClassifier()
face_cascade.load('modelos/lbpcascade_frontalface_improved.xml')

#-- Cargar las imágenes
rostro1 = cv.imread('arte/travolta.jpg')
rostro2 = cv.imread('arte/cage.jpg')

#-- Cargar el detector de fronteras
facemark = cv.face.createFacemarkKazemi() 
facemark.loadModel('face_landmark_model.dat')

gris1 = cv.cvtColor(rostro1, cv.COLOR_BGR2GRAY)
gris1 = cv.equalizeHist(gris1)
faces1 = face_cascade.detectMultiScale(gris1)
result, landmarks1 = facemark.fit(rostro1, faces1)

gris2 = cv.cvtColor(rostro2, cv.COLOR_BGR2GRAY)
gris2 = cv.equalizeHist(gris2)
faces2 = face_cascade.detectMultiScale(gris2)
result, landmarks2 = facemark.fit(rostro2, faces2)

# Crear red convexa
hull = cv.convexHull(landmarks2[0][0], returnPoints=False)
frontera1 = [landmarks1[0][0][z][0] for z in hull]
frontera2 = [landmarks2[0][0][z][0] for z in hull]

#cv.imshow('Busqueda-facial1', cv.face.drawFacemarks(rostro1, landmarks1[0], (255, 0, 0) ))
#cv.imshow('Busqueda-facial2', cv.face.drawFacemarks(rostro2, landmarks2[0], (255, 0, 0) ))
#cv.waitKey()

# Generar parches triangulares
rect2 = 0, 0, len(rostro2[0]), len(rostro2)
subdiv = cv.Subdiv2D(rect2)
for lm in frontera2:
    subdiv.insert(lm)
triangleList = subdiv.getTriangleList()
triangles = []
for x in triangleList:
    pts = [(x[0], x[1]), (x[2], x[3]), (x[4], x[5])]
    ind = [0,0,0]
    if (inRect(rect2, pts[0]) and inRect(rect2, pts[1]) and inRect(rect2, pts[2])):
        for j in range(3):
            for k in range(len(frontera2)):
                if (abs(pts[j][0]-frontera2[k][0]) < 1.0 and abs(pts[j][1]-frontera2[k][1]) < 1.0):
                    ind[j] = int(k)
        triangles.append(ind)

# Transformacion afines en los parches triangulares
img1Warped =  rostro2.copy()
for t in triangles:
    t1 = [frontera1[t[j]] for j in [0,1,2]]
    t2 = [frontera2[t[j]] for j in [0,1,2]]
    r1 = cv.boundingRect(np.array(t1))
    r2 = cv.boundingRect(np.array(t2))
    triangle1Rect = [(t1[i][0]-r1[0], t1[i][1]-r1[1]) for i in [0,1,2]]
    triangle2Rect = [(t2[i][0]-r2[0], t2[i][1]-r2[1]) for i in [0,1,2]]
    triangle2RectInt = [(int(t2[i][0]-r2[0]), int(t2[i][1]-r2[1])) for i in [0,1,2]]
    # Máscara para llenar los parches triangulares
    mask = np.zeros((r2[3],r2[2], 3)).astype(np.float32)
    mask = cv.fillConvexPoly(mask, np.array(triangle2RectInt), (1.0, 1.0, 1.0), 16, 0)
    # Distorsionar los parches triangulares creados y mapearlos en la imagen de destino
    img1Rect = rostro1[r1[1]:r1[1]+r1[3],r1[0]:r1[0]+r1[2]]
    img2Rect = np.zeros((r2[3],r2[2], 3)).astype(np.float32)
    warp_mat = cv.getAffineTransform(np.array(triangle1Rect).astype(np.float32), np.array(triangle2Rect).astype(np.float32))
    img2Rect = cv.warpAffine(img1Rect, warp_mat, (np.shape(img2Rect)[1], np.shape(img2Rect)[0]), cv.INTER_LINEAR, cv.BORDER_REFLECT_101)
    img2Rect = cv.multiply(img2Rect.astype(np.float32), mask.astype(np.float32))
    img2Crop = img1Warped[r2[1]:r2[1]+r2[3],r2[0]:r2[0]+r2[2]]
    ones = np.ones(np.shape(mask)) - mask
    img2Crop = cv.multiply(img2Crop.astype(np.float32), ones.astype(np.float32))
    img2Crop = img2Crop + img2Rect
    img1Warped[r2[1]:r2[1]+r2[3],r2[0]:r2[0]+r2[2]] = img2Crop

# Máscara para colorear los parches mapeados
mhull = [(int(x[0]), int(x[1])) for x in frontera2]
mask1 = np.zeros(rostro2.shape, rostro2.dtype)
mask1 = cv.fillConvexPoly(mask1, np.array(mhull), (255,255,255))

# Colorear los parches usando la operación de clonación    
rc = cv.boundingRect(np.array(frontera2))
center = rc[0] + rc[2] // 2, rc[1] + rc[3] // 2
print(np.shape(mask1))
output = cv.seamlessClone(img1Warped, rostro2, mask1, center, cv.NORMAL_CLONE)
cv.imshow('Contracara', output)
#cv.imshow('Contracara', rostro2)
cv.waitKey()


#-- python3 face_swap.py