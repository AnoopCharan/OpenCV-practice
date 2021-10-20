import numpy as np
import cv2 as cv
import cvutils
import matplotlib.pyplot as plt


img = cv.imread('7.jpg')
img = cvutils.resize(img,None, width=800, keep_aspect_ratio=True)

gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# thresholding, sets pixels with less than set value as 1(white) less than set value to 0 (blank)

# Simple thresholding 
threshold1, thresh1  = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
threshold2, thresh2  = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
#  inverse
thresholdinv, threshinv  = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
#  threshold returns threshold value we input, thres returns with image array

# Adaptive threshold : threshold value is optimized by itself

adthreshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C  , cv.THRESH_BINARY_INV, 11, 5)



cv.imshow('Adpative Thresholding', adthreshold)
cv.imshow(f"Threshold with {threshold1}", thresh1)
# cv.imshow(f"Threshold with {thresholdinv}", threshinv)
cv.imshow('Gray scale', gray)

cv.waitKey(0)