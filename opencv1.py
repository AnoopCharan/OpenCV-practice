import cv2 as cv
import numpy as np

# make a blank image of 500x500 pixels
blank = np.zeros((500,500,3), dtype='uint8')
# print(blank)

# cv.imshow('blank', blank)
# cv.waitKey(0)

#straight horizontal line - select pixels in width 
red = blank
red[240:260] = 0,0,255
# cv.imshow('red',red)
# cv.waitKey(0)

#straight vertical line - select pixels in width 
# red = blank
red[:,240:260] = 0,0,255
# cv.imshow('red',red)
# cv.waitKey(0)
# circle 
cv.circle(red, (250,250), 100, (0,255,0) , thickness=5)
# line
cv.line(red, (0,0), (500,500), (255,255,255), thickness= 2)

cv.line(red, (0,500), (500,0), (255,255,255), thickness= 2)

#  write text use put
cv.putText(red, 'XDXDDXXXDDD',(125,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), thickness=2)


cv.imshow('red', red)
cv.waitKey(0)