import cv2 as cv
import numpy as np

img = cv.imread('photos/lady.jpg')
cv.imshow('Lady', img)

#Translation -> it is a basicaly shifting an image along the x axis and
# y axis , so using this we can shift image up down left and right 

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) #dimension is tuple
    return cv.warpAffine(img, transMat, dimensions)  #The function warpAffine transforms the source image using the specified matrix:

# -x --> left
# -y --> up
# x --> right
# y --> down

# translated = translate(img, 100, 100)
# cv.imshow('Translated',translated)

#Rotation
def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 20)
cv.imshow('Rotate',rotated)

rotated_rotated = rotate(img, -40)
cv.imshow('Rotated Rotated',rotated_rotated)

# resizing
resized = cv.resize(img, (500,500),interpolation= cv.INTER_CUBIC)
cv.imshow('Resized', resized)


#flipping

flip = cv.flip(img, 1) #0 = flipping img verticaly along x axis # 1= flipping horizontaly or y axis # -1 = both vertically and horizontally
cv.imshow('Flip',flip)

# Cropping 
cropped = img[200:400, 300:400]
cv.imshow('Cropped',cropped)



cv.waitKey(0)