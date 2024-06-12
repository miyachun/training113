import cv2
import numpy as np

# Read image in OpenCV
input_img = cv2.imread("001.jpg")
img = cv2.resize(input_img, (640, 480))
# Make a copy to draw contour outline
input_image_cpy = img.copy()
 
# Display input image
cv2.imshow('image', img)
cv2.waitKey(0)