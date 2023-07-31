import cv2
import numpy as np
import glob
from testing2 import WindowCapture
from time import time
import pyautogui
# call static method to show window names
#WindowCapture.list_window_names()

wincap = WindowCapture('Literaki - Mozilla Firefox')

loop_time = time()
while(True):

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    cv2.imshow('Computer Vision', screenshot)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

    # get an updated image of the game
    screenshot = wincap.screen()
    screenshot = pyautogui.screenshot()

    cv2.imshow('Computer Vision', screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
# images = [cv2.imread(file) for file in glob.glob("litery/*.jpg")]
# #testowa plansza
# test = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)

# for litery in images:
#     result = cv2.matchTemplate(litery, test, cv2.TM_CCORR_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#
#     width = litery.shape[1]
#     height = litery.shape[0]
#     ## #cv2.rectangle(test, max_loc, (max_loc[0] + width, max_loc[1] + height), (0,255,255), 2)
#
#     threshold = .99
#     yloc, xloc = np.where(result>= threshold)
#
#     rectangles = []
#     for (x,y) in zip(xloc, yloc):
#         rectangles.append([int(x), int(y), int(width), int(height)])
#         rectangles.append([int(x), int(y), int(width), int(height)])
#     print(len(rectangles))
#     rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
#
#     for (x,y,w,h) in rectangles:
#         cv2.rectangle(test, (x,y), (x+w, y+h),(0,255,255), 2)
#
# cv2.imshow('test', test)
# cv2.waitKey()
# cv2.destroyAllWindows()
