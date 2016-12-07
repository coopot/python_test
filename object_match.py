# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:33:15 2014
@author: duan
"""
import cv2
import cv2.cv as cv
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv2.imread('D:/pysorce/2.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('D:/pysorce/1.png',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
#umpy.where(condition[, x, y])
#Return elements, either from x or y, depending on condition.
#If only condition is given, return condition.nonzero().
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
   cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv2.imwrite('D:/pysorce/res.png',img_rgb)
cv2.imshow('test',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
