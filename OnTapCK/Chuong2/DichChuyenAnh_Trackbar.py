#Chuyển ảnh sang màu xám và tăng độ sáng cho ảnh
#Dịch chuyển ảnh với khoảng cách trục x, y lấy từ trackbar
import cv2
import numpy as np
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.convertScaleAbs(gray,alpha=1, beta=90)
cv2.namedWindow("Trackbar")
def nothing(x):pass 
cv2.createTrackbar("TrucX","Trackbar",0,1000,nothing)
cv2.createTrackbar("TrucY","Trackbar",0,500,nothing)
while True:
    x = cv2.getTrackbarPos("TrucX","Trackbar")
    y = cv2.getTrackbarPos("TrucY","Trackbar")
    M = np.float32([[1,0,x],[0,1,y]])
    h,w = gray2.shape[:2]
    kq = cv2.warpAffine(gray2,M,(w,h))
    cv2.imshow("Trackbar",kq)
    if cv2.waitKey(1)==ord("q"): break

cv2.destroyAllWindows()


