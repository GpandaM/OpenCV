# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:19:56 2019

@author: garima.misra
"""

import cv2

img = cv2.imread('messi.jpg', 0)
cv2.namedWindow('Messi')

def value_change():
    pass

cv2.createTrackbar('MinThres', 'Messi', 0, 255, value_change)
cv2.createTrackbar('MaxThres', 'Messi', 0, 255, value_change)

while(1):
    minThres = cv2.getTrackbarPos('MinThres', 'Messi')
    maxThres = cv2.getTrackbarPos('MaxThres', 'Messi')
    
    k = cv2.waitKey(5) & 0xFF
    if k==ord('q'):
        break
    
    edges = cv2.Canny(img, minThres, maxThres)
    
    cv2.imshow('image', img)
    cv2.imshow('Messi', edges)
    
cv2.destroyAllWindows()