import cv2
import numpy as np

# Read image in OpenCV
input_img = cv2.imread("001.jpg")
img = cv2.resize(input_img, (640, 480))
input_image_cpy = img.copy()
# Convert RGB/ BGR to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of red color in HSV
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])


# create a mask for red color
mask_red = cv2.inRange(hsv, lower_red, upper_red)


# find contours in the red mask
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 
# Draw detected contour in input image
contour_red_cap = cv2.drawContours(input_image_cpy, contours_red, -1, (0, 0, 0), 3)
 
# Dispay contour
cv2.imshow('contour_red_cap', contour_red_cap)
cv2.waitKey(0)


