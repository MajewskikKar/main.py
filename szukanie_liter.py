import cv2 as cv
import numpy as np
import glob
import pyautogui as pg


images = [cv.imread(file, cv.IMREAD_GRAYSCALE) for file in (glob.glob("litery/*.jpg"))]
#testowa plansza
test = cv.imread('test.jpg', cv.IMREAD_UNCHANGED)
test1 = cv.cvtColor(test, cv.COLOR_BGR2GRAY)
for litery in images:
    result =  pg.locateAllOnScreen(litery, confidence =0.5)
    result = cv.matchTemplate(litery, test1, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    width = litery.shape[1]
    height = litery.shape[0]
    ## #cv2.rectangle(test, max_loc, (max_loc[0] + width, max_loc[1] + height), (0,255,255), 2)

    threshold = .90
    yloc, xloc = np.where(result>= threshold)

    rectangles = []
    for (x,y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(width), int(height)])
        rectangles.append([int(x), int(y), int(width), int(height)])
    print(len(rectangles))
    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.2)

    for (x,y,w,h) in rectangles:
        cv.rectangle(test, (x,y), (x+w, y+h),(0,255,255), 2)

cv.imshow('test', test)
cv.waitKey()
cv.destroyAllWindows()
