import cv2 as cv
import numpy as np
from PIL import ImageGrab
from testing2 import WindowCapture
from time import time
import glob

# call static method to show window names
#WindowCapture.list_window_names()

wincap = WindowCapture('Literaki - Mozilla Firefox')

loop_time = time()
while(True):
    screenshot = ImageGrab.grab(bbox =(0, 0, 1500, 1500))
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow('computer_vision', screenshot)

    # get an updated image of the game

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
