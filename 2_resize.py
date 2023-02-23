import cv2 as cv

img = cv.imread('photos/cat.jpg')
cv.imshow('cat',img)

def rescaleFrame(frame, scale = 0.5 ):
    width = int(frame.shape[1] * scale)  #frame.shape[1] is basically width and frame.shape[0] is height
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA) # resize frame to a paticular dimension 
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

# reading video
# capture = cv.VideoCapture('videos/dog.mp4') #capture is instance of videocapture class
# while True:           
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame, scale = .2) #here we change the size using rescale functio 

#     cv.imshow('video',frame)   # display each frame using imshow
#     cv.imshow('Video Resized', frame_resized)
#     if cv.waitKey(20) & 0xFF==ord('d'):    # if letter d is pressed break the loop
#         break
# capture.release()   # release the capture device
# cv.destroyAllWindows()  

cv.waitKey(0)