import cv2 as cv

# img = cv.imread(
#     "/Users/kyle/Documents/GitHub/OpenCV/opencv-course/Resources/Photos/cat_large.jpg")
# cv.imshow("Cat", img)

capture = cv.VideoCapture(0)


def rescaleFrame(frame, scale=0.75):
    # works for images, videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    #  3 and 4 are the width and height respectively
    # Live Video only
    capture.set(3, width)
    capture.set(4, height)


# capture = cv.VideoCapture(
#     "/Users/kyle/Documents/GitHub/OpenCV/opencv-course/Resources/Videos/dog.mp4")

while True:
    # capture frame by frame
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    # display the resulting frame
    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
