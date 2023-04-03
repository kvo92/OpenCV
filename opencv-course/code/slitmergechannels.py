import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('/Users/kyle/Documents/GitHub/OpenCV/opencv-course/Resources/Photos/park.jpg')
b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)