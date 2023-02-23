
# convert between different colorspaces using the OpenCV function cvtColor() 
# popular color spaces are RGB (Red, Green, Blue), CMYK (Cyan, Magenta, Yellow, Black), HSV (Hue, Saturation, Value),
# function cv. cvtColor(input_image, flag)

import cv2 as cv
#import matplotlib.pyplot as plt


img = cv.imread('photos/park.jpg')
cv.imshow('Park', img)

# plt.imshow(img)
# plt.show()


# bgr to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# bgr to hsv  # we can't convert grayscale to hsv . for that 
               # first grayscale to bgr and then bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# bgr to L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# hsv to bgr
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv -> bgr', hsv_bgr)

cv.waitKey(0)