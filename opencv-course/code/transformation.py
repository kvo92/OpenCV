import cv2 as cv
import numpy as np

img = cv.imread(
    '/Users/kyle/Documents/GitHub/OpenCV/opencv-course/Resources/Photos/park.jpg')
cv.imshow('PARK', img)

# translation

# -x --> left
# -y --> up
# x --> right
# y --> down


def translate(img, x, y):
    # translation matrix is a 2x3 matrix
    transMatrix = np.float32([[1, 0, x], [0, 1, y]])
    # shape[1] is width, shape[0] is height
    dimensions = (img.shape[1], img.shape[0])
    # warpAffine is used for translation, rotation, and resizing
    return cv.warpAffine(img, transMatrix, dimensions)


translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    # if no rotation point is specified, use the center of the image
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    # getRotationMatrix2D takes in the rotation point, angle, and scale (1.0)
    rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMatrix, dimensions)


# negative angle is clockwise
# positive angle is counter-clockwise
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# resizing
# INTER_AREA is good for shrinking
# INTER_CUBIC is good for enlarging, but slow
# INTER_LINEAR is good for enlarging
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# flipping
# 0 --> flip vertically
# 1 --> flip horizontally
# -1 --> flip both vertically and horizontally
flip = cv.flip(img, 0)
cv.imshow('Flip', flip)
h_flip = cv.flip(img, 1)
cv.imshow('Horizontal Flip', h_flip)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
