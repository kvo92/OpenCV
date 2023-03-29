import cv2 as cv
import numpy as np

img = cv.imread(
    '/Users/kyle/Documents/GitHub/OpenCV/opencv-course/Resources/Photos/park.jpg')
cv.imshow('PARK', img)

# 1. Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# 2. Blur
# kernal size must be odd
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# 3. Edge Cascade
# threshold1 = 125
# threshold2 = 175
cany = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', cany)

# to make the edges more clear, using blur
cany_with_blur = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges with Blur', cany_with_blur)

# 4. Dilating the image
dilated = cv.dilate(cany_with_blur, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# 5. Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# 6. Resize
# INTER_AREA is good for shrinking
# INTER_CUBIC is good for enlarging, but slow
# INTER_LINEAR is good for enlarging
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# 7. Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
