import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("zurbaran/limones.jpg"))
if img is None:
   sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)

# If the user hits the key "S", a PNG image will be saved
if k == ord("s"):
    cv.imwrite("limones.png", img)