import cv2 as cv 
import cvutils
import matplotlib

img =cv.imread('5.jpg')
img = cvutils.resize(img, height=None, width= 1000, keep_aspect_ratio=True)


#  change color spaces to BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#  change color space to BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
 
#  BG to l A B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# BGR to RGB
aargbe   = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow('gray', gray)
cv.imshow('HSV', hsv)
cv.imshow('L.A.B', lab)
cv.imshow('rgb' ,aargbe)
cv.waitKey(0)