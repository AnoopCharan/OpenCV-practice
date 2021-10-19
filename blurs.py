import cv2 as cv 
import cvutils
import matplotlib
import numpy as np
img =cv.imread('5.jpg')
img = cvutils.resize(img, height=None, width= 1000, keep_aspect_ratio=True)

# Averaging Blur
avg = cv.blur(img, (3,3))

# Gaussian BLue
gaussian = cv.GaussianBlur(img, (3,3), 0)

# Median Blur
median = cv.medianBlur(img, 3)

# Bilateral Blurring
bilateral = cv.bilateralFilter(img, 10, 2, 2)

cv.imshow('Avearge blur',avg)
cv.imshow('Gaussian Blur', gaussian)
cv.imshow('Median', median)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)