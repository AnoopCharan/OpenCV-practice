from caer.io.resize import resize
import cv2 as cv 
import caer

tray = cv.imread('5.jpg')
tray = caer.resize(tray, resize_factor= 0.35)

# Convert image from standard BGR to greyscale
tray_gray =cv.cvtColor(tray, cv.COLOR_BGR2GRAY)

# BLur to reduce noise (gaussian blur is most common)
blur = cv.GaussianBlur(tray_gray, (5,5), cv.BORDER_DEFAULT)

# Sobel operator
# sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
# sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
# sobelxy = cv.Sobel(src=blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=7) # Combined X and Y Sobel Edge Detection

#  Edge cascade - Canny edge detector is common
canny = cv.Canny(blur, 80,100)

# Dilating the image - increases size of selected type pixels, decreases size of unselected
dialated = cv.dilate(canny, (7,7), iterations=1)

#edoring 
# eroded = cv.erode(dialated, (3,3), iterations=1)

# resize and crop
resized = cv.resize(tray, (500,500))

# cropping
cropped = tray[1000:2000, 1000:2000]

cv.imshow('resized',resized)
cv.imshow('cropped', cropped)
cv.imshow('canny', canny)
cv.imshow('dilated', dialated)
cv.imshow('blurred', blur)
# cv.imshow('Sobel',sobelxy)
cv.waitKey(0)
if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()
