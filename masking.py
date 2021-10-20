import numpy as np
import cv2 as cv
import cvutils


img = cv.imread('5.jpg')
img = cvutils.resize(img,None, width=800, keep_aspect_ratio=True)

blank = np.zeros((img.shape[:2]), dtype='uint8')
# create a mask of shape
mask= cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

# merge mask and image
masked = cv.bitwise_and(img, img, mask = mask)

cv.imshow('mask', mask)
cv.imshow('Masked image', masked)
cv.imshow('original', img)
cv.waitKey(0)
