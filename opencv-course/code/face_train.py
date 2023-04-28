import os 
import numpy as np
import cv2 as cv

peoples = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'/Users/kyle/Documents/GitHub/OpenCV/opencv-course/Resources/Faces/train'
haar_cascade = cv.CascadeClassifier('/Users/kyle/Documents/GitHub/OpenCV/haars/haarcascade_frontalface_default.xml')

features = []
labels = []

def create_train():
  for people in peoples:
    path = os.path.join(DIR, people)
    label = people.index(people)

    for img in os.listdir(path):
      img_path = os.path.join(path, img)

      img_array = cv.imread(img_path)
      gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

      faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

      for (x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]
        features.append(faces_roi)
        labels.append(label)

create_train()
print('Training done ---------------')
face_recognizer = cv.face.LBPHFaceRecognizer_create()
features = np.array(features, dtype='object')
labels = np.array(labels)
# Train the Recognizer on the features list and the labels list
face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)