import cv2 as cv 
import cvutils
import matplotlib
import numpy as np
img =cv.imread('5.jpg')
img = cvutils.resize(img, height=None, width= 1000, keep_aspect_ratio=True)
blank = np.zeros(img.shape[:2], dtype='uint8')


b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank,g, blank])
red = cv.merge([blank, blank, r])

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('red', red)
cv.waitKey(0)


