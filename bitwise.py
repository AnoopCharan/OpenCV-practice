import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype= "uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

cv.imshow('Blank', rectangle)
cv.waitKey(0)
