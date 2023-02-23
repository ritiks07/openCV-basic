import cv2 as cv

# reading image 

# img = cv.imread('photos/cat_large.jpg')
# cv.imshow('cat',img)
# cv.waitKey(0) # wait key //0- wait infinity time

# reading video
#we use while loop to read frame
capture = cv.VideoCapture('videos/dog.mp4') #capture is instance of videocapture class
while True:           
    isTrue, frame = capture.read()
    cv.imshow('video',frame)   # display each frame using imshow
    if cv.waitKey(20) & 0xFF==ord('d'):    # if letter d is pressed break the loop
        break
capture.release()   # release the capture device
cv.destroyAllWindows()    