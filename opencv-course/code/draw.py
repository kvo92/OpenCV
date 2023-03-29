import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# img = cv.imread(
#     '/Users/kyle/Documents/GitHub/OpenCV/opencv-course/Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

# 1. Paint the image a certain color
# blank[:] = 0, 255, 0

# painting a red spare
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Green', blank)

# drawing a rectangle
# thickness=-1 will fill the rectangle or circle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0),
             thickness=-1)  # -1 will fill the rectangle
cv.imshow('Rectangle', blank)
# DRAWING A CIRCLE
cv.circle(blank, (blank.shape[1] // 2,
          blank.shape[0] // 2), 40, (0, 0, 255), thickness=3)

# drawing a line
cv.line(blank, (0, 0),
        (blank.shape[1] // 2, blank.shape[0] // 2), (255, 255, 255), thickness=3)

# writing text
cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_TRIPLEX,
           1.0, (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)

cv.waitKey(0)
