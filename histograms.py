import numpy as np
import cv2 as cv
import cvutils
import matplotlib.pyplot as plt


img = cv.imread('7.jpg')
img = cvutils.resize(img,None, width=800, keep_aspect_ratio=True)

blank = np.zeros((img.shape[:2]), dtype='uint8')
# # create a mask of shape
mask= cv.circle(blank, (img.shape[1]//2 + 200, img.shape[0]//2), 100, 255, -1)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# gray_hist = cv.calcHist([gray], [0], mask,  [256],[0, 256])

masked = cv.bitwise_and(img,img, mask = mask)


plt.figure()
plt.title('BGR  Histograms')
plt.xlabel('Bins')
plt.ylabel('no of pixels')

colors= ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist)
    plt.xlim([0,256])


# plt.plot(gray_hist)
# plt.xlim([0,256])


cv.imshow('Image', masked)
plt.show()
cv.waitKey(0)