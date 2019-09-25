# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:11:32 2019

@author: garima.misra
"""

import cv2
import numpy as np

ix, iy = -1,-1
left_press = False

def value_change(x):
    pass

def mouse_brush(event,x,y,flags, param):
    global ix, iy, left_press
    if event == cv2.EVENT_LBUTTONDOWN:
        ix = x
        iy = y
        left_press = True
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if left_press == True:
            cv2.circle(img, (x,y), param[0], param[1], -1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        left_press = False

#create a black image
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

#create colorTrackBar
cv2.createTrackbar('R', 'image',0,255, value_change)
cv2.createTrackbar('G', 'image',0,255, value_change)
cv2.createTrackbar('B', 'image',0,255, value_change)
#create brush
brush = 'OFF:0 \nON:1'
cv2.createTrackbar('brush', 'image',0,1, mouse_brush)
radius = 'Min:1 \nMax:10'
cv2.createTrackbar('radius', 'image',1,10, value_change)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    B = cv2.getTrackbarPos('brush', 'image')
    R = cv2.getTrackbarPos('radius', 'image')
    
    if B == 0:
        img[:] = [255,255,255]
    else:
        param = [R, (r,g,b)]
        cv2.setMouseCallback('image', mouse_brush, param)
        
cv2.destroyAllWindows()
    
