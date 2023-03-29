import cv2 as cv

# read image
# img = cv.imread(
#     "/Users/kyle/Documents/GitHub/OpenCV/opencv-course/Resources/Photos/cat_large.jpg")
# cv.imshow("Cat", img)
# wait for any key to be pressed
# cv.waitKey(0)

# read video
capture = cv.VideoCapture(
    "/Users/kyle/Documents/GitHub/OpenCV/opencv-course/Resources/Videos/dog.mp4")

while True:
    # capture frame by frame
    isTrue, frame = capture.read()
    # display the resulting frame
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
