# we know `RGB` but in OpenCV it is `BGR`
# STEP 1: from colour to gray scale image
# import cv2
#
# img = cv2.imread('girl.jpeg')
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # cvtCOLOR: Convert Color to
#
# cv2.imshow('Coloured Image', img)
# cv2.imshow('Gray Image', imgGray)
# cv2.waitKey(0)


# STEP 2: Image Detection Techniques
# import cv2
#
# img = cv2.imread('girl.jpeg')
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
#
# cv2.imshow('Coloured Image', img)
# cv2.imshow('Gray Image', imgGray)
# cv2.imshow('Blur Image', imgBlur)
# cv2.waitKey(0)


# STEP 3: Edge Detection
# import cv2
#
# img = cv2.imread('girl.jpeg')
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
# imgCanny = cv2.Canny(img, 100, 100)
#
# cv2.imshow('Coloured Image', img)
# cv2.imshow('Gray Image', imgGray)
# cv2.imshow('Blur Image', imgBlur)
# cv2.imshow('Canny Image', imgCanny)
# cv2.waitKey(0)


# STEP 4: Dilation and Erode
import cv2
import numpy as np

img = cv2.imread('Lenna.png')
kernel = np.ones((5, 5), np.uint8)  # unassigned integer 8 bit, meaning values ranging 0 to 255
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDilation = cv2.dilate(img, kernel, iterations=1)
imgEroded = cv2.erode(img, kernel, iterations=1)

cv2.imshow('Coloured Image', img)
cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilated Image', imgDilation)
cv2.imshow('Eroded Image', imgEroded)
cv2.waitKey(0)
