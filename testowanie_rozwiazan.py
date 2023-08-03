import numpy as np
import sys
import cv2 as cv
import os

template = cv.imread('test.jpg', cv.IMREAD_UNCHANGED)
litera = cv.imread('litery/a.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(litera, template, cv.TM_CCOEFF_NORMED)
thershold = 0.95
location = np.where(result >= thershold)
location = list(zip(*location[::-1]))
print(location)