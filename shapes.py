
# SHAPES AND TEXT

# lines, rectangles, circles, text on images

# create matrix with zeros(0). Zero represent black

import cv2
import numpy as np
#
# img = np.zeros((500, 500))
# img2 = np.zeros((500, 500, 3))
#
# print(img.shape)
# print(img2.shape)
#
# cv2.imshow('image', img)
# cv2.imshow('image 2', img2)
# cv2.waitKey(0)


# STEP 2: Add colour to image

# img = np.zeros((500, 500))
# img2 = np.zeros((500, 500, 3))
# img3 = np.zeros((500, 500, 3))
#
# img2[:] = 255, 0, 0              # BGR
# img3[0:450, 100:400] = 250, 0, 0
#
# cv2.imshow('image', img)
# cv2.imshow('image 2', img2)
# cv2.imshow('image 3', img3)
# cv2.waitKey(0)


# STEP 3: Add Lines
#
# img = np.zeros((500, 500, 3))
#
# cv2.line(img, (0, 0), (200, 200), (0, 0, 255), 3)
#
# cv2.imshow('image', img)
# cv2.waitKey(0)


# STEP 4: Add rectangle

# img = np.zeros((500, 500, 3))
#
# # cv2.rectangle(img, (0, 0), (200, 350), (0, 255, 0), 3)
# cv2.rectangle(img, (0, 0), (200, 350), (0, 255, 0), cv2.FILLED)
#
# cv2.imshow('image', img)
# cv2.waitKey(0)

# STEP 5: Add Circle

# img = np.zeros((500, 500, 3))
#
# cv2.circle(img, (250, 250), 100, (255, 0, 0), 2)
#
# cv2.imshow('image', img)
# cv2.waitKey(0)

# STEP 6: Adding Text

img = np.zeros((500, 500, 3))

cv2.circle(img, (250, 250), 100, (255, 0, 0), 2)
cv2.putText(img, 'This is a Circle', (150, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
cv2.imshow('image', img)
cv2.waitKey(0)
