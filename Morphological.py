# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:49:07 2019

@author: garima.misra
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret==True:
        frame = cv2.flip(frame, 180)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_red = np.array([30, 150, 50])
        upper_red = np.array([255, 255, 180])
        
        mask = cv2.inRange(frame, lower_red, upper_red)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        
        kernal = np.ones((5,5), np.uint8)
        
        erosion = cv2.erode(mask, kernal, iterations=1)
        dilate = cv2.dilate(mask, kernal, iterations=1)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
        
        cv2.imshow('Orginal', frame)
        cv2.imshow('Mask', mask)
        cv2.imshow('Erosion', erosion)
        cv2.imshow('Dilate', dilate)
        cv2.imshow('Opening', opening)
        cv2.imshow('Closing', closing)
        
        k = cv2.waitKey(5) & 0xFF
        if k==ord('q'):
            break

cap.release()
cv2.destroyAllWindows()