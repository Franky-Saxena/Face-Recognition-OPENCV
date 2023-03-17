
import cv2

# facescascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
#
# img = cv2.imread('face.jpeg')
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = facescascade.detectMultiScale(img, 1.1, 4)
#
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# cv2.imshow('girlface', img)
# cv2.waitKey(0)


# -------------VIDEO---------------

import cv2

facescascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture('faces.mp4')  # 0: for using the webcam, and if you want to use the video just put the path of the video
while True:
    _, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facescascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
    cv2.imshow('Video', img)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
