# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:17:30 2019

@author: garima.misra
"""

from pathlib import Path
import numpy as np
import time
import glob
import os
import cv2
import re

dirname = os.path.dirname(__file__)
#print(dirname)
path = os.path.join(dirname, 'Exercise_Airthmetic')

img2 = np.zeros((100,100,3), np.uint8)
 
for file in os.listdir(path):
    if file.endswith(".png") or file.endswith(".jpg"):
        img1 = cv2.imread(path+'/'+file)
        img2_resize = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
        for alpha in range(1, 10, 1):
            alpha = alpha/10
            beta = 1 - alpha
            cv2.imshow("window", cv2.addWeighted(img1, alpha, img2_resize, beta, 0))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            time.sleep(0.1)
        img2 = img1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  

cv2.destroyAllWindows()

#for filename in Path('C:\\Users\\garima.misra\\AppData\\Local\\Continuum\\anaconda2\\envs\\NewEnv\\New\\Video\\Exercise_Airthmetic').glob('**/*.png'):
#    print(filename)
#
#for filename in Path(path).glob('**/*.png'):
#    images.append(filename)
#    
##for filepath in glob.iglob('C:\\Users\\garima.misra\\AppData\\Local\\Continuum\\anaconda2\\envs\\NewEnv\\New\\Video\\Exercise_Airthmetic/*.png'):
##    print(filepath)
#