import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype= "uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200),200,255,-1)

# bitwise AND operation ( 1 & 1 is 1, rest zero) --> intersecting region (common area)
bitwise_and= cv.bitwise_and(rectangle, circle,)

# bitwise OR operation ( 1 OR 0 is 1, 0 OR 1 is 1, rest zero) --> all region
bitwise_or= cv.bitwise_or(rectangle, circle)

#bitwise XOR operation ( 0 & 0 is 1, rest zero) gives opposite result of AND --> all non intersection area ( opposite of intersection)
bitwise_xor= cv.bitwise_xor(rectangle, circle)

# bitwise NOT 
bitwise_not = cv.bitwise_not(rectangle)


cv.imshow('circle AND rectangle', bitwise_and)
cv.imshow('circle XOR rectangle', bitwise_xor)
cv.imshow('circle OR rectangle', bitwise_or)
# # cv.imshow('Circle', circle)
# cv.imshow('Rectangle', rectangle)
cv.waitKey(0)
