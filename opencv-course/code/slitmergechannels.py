import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('/Users/kyle/Documents/GitHub/OpenCV/opencv-course/Resources/Photos/park.jpg')
b,g,r = cv.split(img)


cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

# avering 
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# guassian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss) 

# median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# bilateral blur
# retains edges
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)

