"""

Here we'll see how to merge more than two image on side by side
or one above the other.

"""
# import cv2
# import numpy as np
#
# img1 = cv2.imread('girl.jpeg')
# print(img1.shape)
# img2 = cv2.imread('Lenna.png')
#
# img2Resized = cv2.resize(img2, (236, 224))
# print(img2Resized.shape)
#
# # *To merge two images you have to know the size of those images to merge
# """
# ValueError: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 224 and the array at index 1 has size 220
# """
# hstack = np.hstack((img1, img2Resized))  # it'll merge the images HORIZONTALLY
# vstack = np.vstack((img1, img2Resized))  # it'll merge the images VERTICALLY
#
#
# cv2.imshow('horizontalImage', hstack)
# cv2.imshow('VerticalImage', vstack)
# cv2.waitKey(0)

"""
IF YOU HAVE ONE COLOURED AND ONE GRAY IMAGE
"""
# --------------------------------- General Function for Stacking images -----------

import cv2
import numpy as np


def stackImages(scale, imgArray):
 rows = len(imgArray)
 cols = len(imgArray[0])
 rowsAvailable = isinstance(imgArray[0], list)
 width = imgArray[0][0].shape[1]
 height = imgArray[0][0].shape[0]
 if rowsAvailable:
  for x in range(0, rows):
   for y in range(0, cols):
    if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
    else:
     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
    if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
  imageBlank = np.zeros((height, width, 3), np.uint8)
  hor = [imageBlank] * rows
  hor_con = [imageBlank] * rows
  for x in range(0, rows):
   hor[x] = np.hstack(imgArray[x])
  ver = np.vstack(hor)
 else:
  for x in range(0, rows):
   if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
    imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
   else:
    imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
   if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
  hor = np.hstack(imgArray)
  ver = hor
 return ver


img1 = cv2.imread('girl.jpeg')
img1Gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
print(img1.shape)
img2 = cv2.imread('Lenna.png')
img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

imagStack = stackImages(1, ([img1, img2, img1Gray], [img2, img2Gray, img1]))

# img2Resized = cv2.resize(img2, (236, 224))
# print(img2Resized.shape)

# hstack = np.hstack((img1, img2Resized))  # it'll merge the images HORIZONTALLY
# vstack = np.vstack((img1, img2Resized))  # it'll merge the images VERTICALLY

cv2.imshow('gray&coloured', imagStack)
# cv2.imshow('VerticalImage', vstack)
cv2.waitKey(0)

