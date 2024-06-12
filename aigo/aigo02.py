
'''
import cv2
img = cv2.imread('001.jpg')
cv2.imshow('My Image', img)
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("001.jpg"))
if img is None:
   sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)