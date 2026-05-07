#Đọc ảnh màu và thực hiện các yêu cầu sau.
#a. tạo trackbar để chọn kích thước mặt nạ lọc.
#b. lọc ảnh bằng bộ lọc trung bình với kích thước mặt nạ lấy từ trackbar.
#c. tạo trackbar để chọn kích thước dx, dy.
#d. dịch chuyển ảnh với khoảng cách theo trục x và trục y là dx, dy lấy từ trackbar.
import cv2
import numpy as np
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
cv2.namedWindow("Trackbar")
def nothing(x):pass
cv2.createTrackbar("Matna","Trackbar",1,10,nothing)
cv2.createTrackbar("DX","Trackbar",0,500,nothing)
cv2.createTrackbar("DY","Trackbar",0,500,nothing)
h,w=img.shape[:2]
while True:
    k= cv2.getTrackbarPos("Matna","Trackbar") 
    dx=cv2.getTrackbarPos("DX","Trackbar")
    dy=cv2.getTrackbarPos("DY","Trackbar")
    kq=cv2.blur(img,(k,k))
    M = np.float32([[1,0,dx],[0,1,dy]])
    kq = cv2.warpAffine(kq,M,(w,h))
    cv2.imshow("Trackbar",kq)
    if cv2.waitKey(1)==ord("q"):break

cv2.destroyAllWindows()