# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:19:43 2019

@author: garima.misra
"""

import cv2
import numpy as np

imageA = cv2.imread("Messi.jpg",0)
imgA = imageA.copy()
imageB = cv2.imread("openCV.png", 0)
imgB = imageB.copy()
imgA = cv2.resize(imgA, (imgB.shape[1], imgB.shape[0]), interpolation=cv2.INTER_CUBIC)

def gauss_laplace(img):
    gauss_pyr = [img]
    for i in range(3):
        img = cv2.pyrDown(img)
        gauss_pyr.append(img)
    
    #top of laplace will be same as top of gauss 
    laplace_top = gauss_pyr[-1]
    laplace_pyr = [laplace_top]
    for i in range(3,0,-1):
        size = (gauss_pyr[i-1].shape[1], gauss_pyr[i-1].shape[0])
        laplace = cv2.pyrUp(gauss_pyr[i], dstsize=size)
        laplace_up = cv2.subtract(laplace, gauss_pyr[i-1])
        laplace_pyr.append(laplace_up)
    return laplace_pyr

imgA_lap = gauss_laplace(imgA)
imgB_lap = gauss_laplace(imgB)

join_img = []
for lA, lB in zip(imgA_lap, imgB_lap):
    rows, cols = lA.shape
    st = np.hstack((lA[:, 0:int(cols/2)], lB[:, int(cols/2):]))
    join_img.append(st)

#now reconstruct laplacian
LS = join_img[0]
print(len(join_img))
for i in range(1,len(join_img)):
    LS = cv2.pyrUp(LS)
    try:
        LS = cv2.add(LS, join_img[i])
    except Exception as e:
        print("In exception", e)
    
#Direct Blending 
direct_blending = np.hstack((imgA[:,:int(imgA.shape[1]/2)], imgB[:,int(imgB.shape[1]/2):]))
cv2.imshow("Direct", direct_blending)
cv2.imshow("LaplaceBlending", LS)
cv2.waitKey(0)  
