import cv2

print('Package imported')

# STEP: 1
# reading image

# img = cv2.imread("girl.jpeg")
#
# # it'll not show image in this only because it shows the image and go offline in a millisecond only
# cv2.imshow("girlImage", img)
#
# cv2.waitKey(0)  # if u put '0' then it'll be there rather u close it if u put '1000' then it will there for 1second


# STEP: 2
# Streaming Video: we will read the video as series of images
#
# cap = cv2.VideoCapture('video 2.mp4')
# while True:
#     success, img = cap.read()
#     cv2.imshow('videos', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# STEP: 3
# Streaming from WebCam

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 100)  # brightness
while True:
    success, img = cap.read()
    cv2.imshow('webcam video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

