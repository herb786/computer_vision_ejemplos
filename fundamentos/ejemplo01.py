import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("zurbaran/limones.jpg"))
if img is None:
   sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)

# Si el usuario teclea "S", la image será guardad con extensión PNG
if k == ord("s"):
    cv.imwrite("limones.png", img)