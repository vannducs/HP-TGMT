#Chuyển ảnh sang màu xám và tăng độ sáng cho ảnh
#Xoay ảnh 1 góc 180 độ
#Tách biên sobel cho ảnh
#Dịch chuyển ảnh với khoảng cách trục x, y lấy từ trackbar
import cv2
import numpy as np
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
xam = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ds = cv2.convertScaleAbs(xam, alpha=1, beta=100)
h, w=img.shape[:2]
Mx = cv2.getRotationMatrix2D((w//2,h//2),180,1)
anhxoay = cv2.warpAffine(ds, Mx, (w,h))

loc = cv2.GaussianBlur(anhxoay, (5,5),0)

gradx=cv2.Sobel(loc,cv2.CV_64F,1,0,3)
grady=cv2.Sobel(loc,cv2.CV_64F,0,1,3)
absx = cv2.convertScaleAbs(gradx)
absy = cv2.convertScaleAbs(grady)
tb = cv2.addWeighted(absx,0.5,absy,0.5,0)

cv2.namedWindow("Trackbar")
def nothing(x): pass
cv2.createTrackbar("Trucx","Trackbar",0,1000,nothing)
cv2.createTrackbar("Trucy","Trackbar",0,500,nothing)
while True:
    tx = cv2.getTrackbarPos("Trucx","Trackbar")
    ty = cv2.getTrackbarPos("Trucy","Trackbar")
    M = np.float32([[1,0,tx],[0,1,ty]])
    kq = cv2.warpAffine(tb, M, (w,h))
    cv2.imshow("Trackbar",kq)
    if cv2.waitKey(1)==ord("q"):
        break

cv2.destroyAllWindows()





