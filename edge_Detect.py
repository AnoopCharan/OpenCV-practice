import numpy as np
import cv2 as cv
import cvutils
import matplotlib.pyplot as plt


img = cv.imread('5.jpg')
img = cvutils.resize(img,None, width=800, keep_aspect_ratio=True)

gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#  Laplacean edge detection algorithm
lap =cv.Laplacian(gray, cv.CV_64F )
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, dx=1, dy=0)
sobely = cv.Sobel(gray, cv.CV_64F, dx=0, dy=1)
sobelxy = cv.Sobel(gray, cv.CV_64F, dx=1, dy=1)
sobelxy =cv.bitwise_not(sobelxy)
# cv.imshow('Sobel x', sobelx)
# cv.imshow('Sobel y', sobely)

canny = cv.Canny(gray, 100,175)
cv.imshow('COmbinedsobel', sobelxy)
cv.imshow('Canny', canny)
cv.waitKey(0)
