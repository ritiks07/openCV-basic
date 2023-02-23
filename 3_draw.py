import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Black',blank)

# img = cv.imread('photos/cat.jpg') #uint8 is basically an image
# cv.imshow('Cat', img)

#1. Paint the image a certain colour
# blank[:] = 0,255,0 #whole screan is coloured
# blank[100:200, 250:400] = 140,213,214 #colour the specific dimension
# cv.imshow('Green', blank)

#2. draw a rectangle

# cv.rectangle(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,250,0), thickness=cv.FILLED) #cv.filled or -1 # (250,250) or blank.shape[1]//2, blank.shape[0]//2
# cv.imshow('Rectangle',blank)

# #3. draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.imshow('Circle',blank)

#4. draw a line
# cv.line(blank,(0,0),(100,250),(255,250,255),thickness=3 )
# cv.imshow('Line',blank)

#5. write text
cv.putText(blank,"hello ritik, how are you!!",(10,255),cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255),2)
cv.imshow('Text',blank)




cv.waitKey(0)