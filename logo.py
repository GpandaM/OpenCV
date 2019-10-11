# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:58:44 2019

@author: garima.misra
"""

import numpy as np
import cv2

img = np.zeros((450,350,3), np.uint8)
img[:,:] = (0,0,0)
#img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

img = cv2.ellipse(img, (165, 90), (50,50), 0, 120 ,420, (0,0,255), 30)
img = cv2.ellipse(img, (93,231), (50,50), 0, 10, 300, (0,255,0), 30)
img = cv2.ellipse(img, (246, 227), (50,50), 0, -60, 240, (255,0,0), 30)
#cv2.imshow("imgae", img,)

font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img, 'OpenCV', (56, 355), font, 4, (255,255,255), 8)
cv2.imshow("imgae", img,)

cv2.imwrite("openCV_logo.png", img)

cv2.waitKey(0) & 0xFF
#if k==27:
#    cv2.destroyAllWindows()
cv2.destroyAllWindows()
#cv2.waitKey(1) & 0xFF