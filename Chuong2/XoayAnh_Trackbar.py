#Dùng bộ lọc trung bình lọc ảnh, tách biên canny cho ảnh
#xoay ảnh với góc xoay lấy từ trackbar
import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
anhloc = cv2.blur(gray, (3,3))
tachbien = cv2.Canny(anhloc,100,200)
cv2.namedWindow("Trackbar")
def nothing(x): pass
cv2.createTrackbar("XoayAnh","Trackbar",0,360,nothing)
h,w=tachbien.shape[:2] 
while True:
    gx = cv2.getTrackbarPos("XoayAnh","Trackbar")
    M = cv2.getRotationMatrix2D((w//2,h//2),gx,1)
    kq = cv2.warpAffine(tachbien,M,(w,h))
    cv2.imshow("Trackbar",kq)
    if cv2.waitKey(1)==ord("q"): break

cv2.destroyAllWindows()
