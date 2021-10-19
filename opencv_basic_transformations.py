import cv2 as cv
import numpy as np
img = cv.imread('5.jpg')
img = cv.resize(img, (1000,1000), interpolation= cv.INTER_AREA)
# Translations :
def translate(img, x, y):
    transMAT = np.float32([[1,0,x], [0,1,y]])
    dims = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMAT, dims)

# rotated
def rotate(img, angle, rotpoint= None):
    (h, w) = img.shape[:2]
    if rotpoint == None:
        rotpoint =(w//2, h//2)
    rotmat = cv.getRotationMatrix2D(rotpoint, angle, scale= 1.0)
    dims= (w, h)
    return cv.warpAffine(img, rotmat, dims)
# flipping 
flip = cv.flip(img , 1)
cv.imshow('vertical flip', flip)
cv.imshow('original', img)
# cv.imshow('translated', translate(img, 100,100))
# cv.imshow('rotated', rotate(img,60))
# cv.waitKey(0)
if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()