import cv2 as cv

img = cv.imread('photos/lady.jpg')
cv.imshow('Lady', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur
blur = cv.GaussianBlur(img, (1,1), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# edge cascade 
canny = cv.Canny(blur, 100, 80)
cv.imshow('Canny Edges', canny)

#dilating the image
dilated = cv.dilate(canny, (7,7), iterations= 3)
cv.imshow('Dilated',dilated)

#eroding

eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded',eroded)

#resize
resized = cv.resize(img, (500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('Resize', resized)

#cropping 
cropped = img[200:400, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)

