# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 11:22:11 2018

@author: garima.misra
"""

import cv2 as cv
import numpy as np

img_color = cv.imread("Sun.jpg", 1)
img_grey = cv.imread("Sun.jpg", 0)
img_unchanged = cv.imread("Sun.jpg", -1)
#print(img)

cv.imshow('window1', img_color)
cv.imshow('window2', img_grey)
cv.imshow('window3', img_unchanged)

cv.namedWindow('window4', cv.WINDOW_NORMAL)

key = cv.waitKey(0)

if key == 27:
    cv.destroyAllWindows()
elif key == ord('s'):
    cv.imwrite('SUN.png', img_grey)
    cv.destroyAllWindows()
    
cv.destroyWindow('window1')
