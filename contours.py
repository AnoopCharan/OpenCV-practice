import cv2 as cv
import numpy as np
import cvutils

img = cv.imread('5.jpg')
# img = img[:, 600:2600]
img_aspect= cvutils.aspect_ratio(img)
width = 700
height =int( width * img_aspect)
print( img_aspect , width, height)
img = cv.resize(img, (width, height))
blank = np.zeros(img.shape, dtype='uint8')
#  contour detection
#  convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur the imahge - using gaussian blur
blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
# get edges by canny edge detector
canny_blur = cv.Canny(blur, 80,175)
# canny = cv.Canny(gray, 125,175)

# get contours
contours, hierarchies = cv.findContours(canny_blur, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} Countour(s) were found!! ")

# draw contours
cv.drawContours(blank, contours, -1, (255,0,0), thickness=2)

# cv.imshow('gray', gray)
# cv.imshow('canny', canny)
cv.imshow('canny_blurred', canny_blur)
cv.imshow('Countours', blank)
cv.waitKey(0)
