import cv2
import numpy as np

# Read image in OpenCV
input_img = cv2.imread("001.jpg")
img = cv2.resize(input_img, (640, 480))

# Convert RGB/ BGR to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of red color in HSV
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
 
# create a mask for red color
mask_red = cv2.inRange(hsv, lower_red, upper_red)
 
# Display filtered image
cv2.imshow('mask_red', mask_red)
cv2.waitKey(0)

