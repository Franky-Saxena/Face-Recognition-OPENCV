"""
WARP: In this we can be able to extract the OBJECT from the images
"""

import cv2
import numpy as np

img = cv2.imread('card.jpeg')
width, height = 250, 350
pts1 = np.float32([[234, 60], [341, 53], [254, 213], [367, 203]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow('card Image', img)
cv2.imshow('card Output', imgOutput)
cv2.waitKey(0)

