# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:02:18 2019

@author: garima.misra
"""

import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

img = cv2.imread("commodity.jpg", 0)

def sNp(image, prob):
    out = np.zeros(image.shape, np.uint8)
    t = 1-prob
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rand = random.random()
            if rand < prob: #less than 0.04
                out[i][j] = 0
            elif rand > t: #greater than 0.96
                out[i][j] = 255 
            else:
                out[i][j] = image[i][j] #except prob<R<1-prob
    return out


img_noise = sNp(img, 0.04)
cv2.imwrite("commodity_noisy.jpg", img_noise)

#Box Filter
img_boxF = cv2.boxFilter(img_noise, -1, (5,5))

#Gaussian Filter
img_gausF = cv2.GaussianBlur(img_noise, (7,7), 0)

#Median Filter
img_mediF = cv2.medianBlur(img_noise, 5)

#Bilateral Filter
img_bilatF = cv2.bilateralFilter(img_noise, 10,80,80)


plt.figure(figsize=(18,12))
plt.subplot(321), plt.imshow(img), plt.title("Gray original Image")
plt.subplot(322), plt.imshow(img_noise), plt.title("Noisy Image")
plt.subplot(323), plt.imshow(img_boxF), plt.title("Box Filter")
plt.subplot(324), plt.imshow(img_gausF), plt.title("Gaussian Filter")
plt.subplot(325), plt.imshow(img_mediF), plt.title("Median Filter")
plt.subplot(326), plt.imshow(img_bilatF), plt.title("Bilateral Filter")

