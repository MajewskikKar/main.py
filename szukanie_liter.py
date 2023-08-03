import cv2 as cv
import numpy as np
import glob
import os
from PIL import ImageGrab
from time import time

#wyswietlanie obrazu
# loop_time = time()
# if window_name is None:
#     self.hwnd = win32gui.GetDesktopWindow()
# else:
#     self.hwnd = win32gui.FindWindow(None, 'Literaki — Mozilla Firefox')
#     if not self.hwnd:
#         raise Exception("Literaki nie są włączone")
# while(True):
#     screenshot = ImageGrab.grab(bbox =(0, 0, 1500, 1500))
#     screenshot = np.array(screenshot)
#     screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
#
#     cv.imshow('computer_vision', screenshot)
#
#     # get an updated image of the game
#
#     # debug the loop rate
#     print('FPS {}'.format(1 / (time() - loop_time)))
#     loop_time = time()
#
#     # press 'q' with the output window focused to exit.
#     # waits 1 ms every loop to process key presses
#     if cv.waitKey(1) == ord('q'):
#         cv.destroyAllWindows()
#         break



#szukanie liter
images = [cv.imread(file, cv.IMREAD_UNCHANGED) for file in (glob.glob("litery/*.jpg"))]
dir_names = os.listdir('litery')
diction = {'a':[], '':[],'c':[],'d':[],'e':[],'f':[]}
assert images is not None, "file could not be read, check with os.path.exists()"



#testowa plansza
test1 = cv.imread('test1.jpg', cv.IMREAD_UNCHANGED)
#test1 = cv.cvtColor(test, cv.COLOR_BGR2GRAY)
for litery in images:
    letter_name = dir_names[0][0]
    result = cv.matchTemplate(litery, test1, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    width = litery.shape[1]
    height = litery.shape[0]

    threshold = 0.85
    yloc, xloc = np.where(result>= threshold)

    rectangles = []
    rectangles_size = []
    for (x,y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(width), int(height)])
        rectangles.append([int(x), int(y), int(width), int(height)])
    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)

    for (x,y,w,h) in rectangles:
        cv.rectangle(test1, (x,y), (x+w, y+h),(0,255,255), 2)
        rectangles_size.append([x , y, w+x ,h+y])
    dir_names.pop(0)
    #diction[letter_name].append(rectangles_size)
    print(sum)
cv.imshow('test', test1)
cv.waitKey()
cv.destroyAllWindows()
#TEST