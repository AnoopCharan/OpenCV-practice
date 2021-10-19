import cv2 as cv

def aspect_ratio(img):
    (height, width) = (img.shape[0], img.shape[1])
    return (height/width) 

def resize(img, height, width, keep_aspect_ratio = False ):
    if keep_aspect_ratio == False:
        return cv.resize(img, (height, width))
    asr = aspect_ratio(img)
    if width == None:
        h =height
        w = int(h *asr)
    elif height == None:
        w = width
        h =int(w /asr)
    return cv.resize(img, (h,w))
    
def contours_in(img, blursize =(3,3), cannythreshold= (100,175), color = (255,0,0) ):
    blur =cv.GaussianBlur(img, blursize, cv.BORDER_DEFAULT)
    # blur= cv.medianBlur(img, blursize[0] )
    edges = cv.Canny(blur, cannythreshold[0], cannythreshold[1])
    contours, heirachies = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    return cv.drawContours(img, contours, -1, color, thickness=2)
