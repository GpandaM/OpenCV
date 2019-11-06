# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:53:07 2019

@author: garima.misra
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('openCV_logo.png',0)

laplacian = cv2.Laplacian(image, cv2.CV_64F)

#derivative in x dir
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
#derivative in y dir
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
#total derivative
sobel = np.hypot(sobel_x, sobel_y)
sobelABS = np.absolute(sobel)
sobel_8U = np.uint8(sobelABS)

plt.figure(figsize=(12, 10))
plt.subplot(321), plt.imshow(laplacian), plt.title("Laplacian")
plt.subplot(322), plt.imshow(sobel_x), plt.title("Sobel_x")
plt.subplot(323), plt.imshow(sobel_y), plt.title("Sobel_y")
plt.subplot(324), plt.imshow(sobel), plt.title("Sobel")
plt.subplot(325), plt.imshow(sobel_8U), plt.title("Sobel_8U")

plt.show()
    