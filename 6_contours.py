import cv2 as cv
import numpy as np

# contour detection, we can detect the borders of objects, and localize them easily in an image.
img = cv.imread('photos/cats.jpg')
cv.imshow('cats', img)

blank = np.zeros(img.shape, dtype= 'uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# canny = cv.Canny(blur, 125,175)
# cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY) # below 125 convert to black and above 255 convert to white
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (0,0,255),2)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)