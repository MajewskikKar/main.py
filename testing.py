import numpy as np
import pyautogui
import cv2

while(True):

    # get an updated image of the game
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    cv2.imshow('Computer Vision', screenshot)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
