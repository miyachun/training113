
import cv2
img = cv2.imread('002.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 圖像數值超過170取255，小於170的變成0
ret,thresh = cv2.threshold(img,170,255,cv2.THRESH_BINARY)

# 在draw畫板上繪製輪廓；畫第幾個輪廓，-1代表所有輪廓；BGR分別對應(0,0,255)，用紅色線畫輪廓；線條寬2
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

draw = img.copy()
res = cv2.drawContours(draw, contours,-1, (0, 0, 255), 1)

cv2.imshow('My Image', res)
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()