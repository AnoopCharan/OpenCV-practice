import cv2 as cv
import numpy as np 
import cvutils

capture = cv.VideoCapture('4.mp4')

while True:
    isTrue, frame = capture.read()
    if isTrue == False:
        break
    else:
        edges = cvutils.contours_in(frame, color=(0,0,255))
        cv.imshow('VIdeo',edges)
        # cv.waitKey(20)
    if cv.waitKey(15) & 0xFF == 27:
        break

capture.release()
cv.destroyAllWindows()
    