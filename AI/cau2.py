#Câu 2 (3 điểm): Đọc ảnh màu và thực hiện các yêu cầu sau:
#a. Tạo trackbar để chọn kích thước kernel (số lẻ)
#b. Tạo trackbar để chọn độ sáng (-127 đến 127)
#c. Lọc ảnh bằng GaussianBlur với kernel lấy từ trackbar
#d. Thay đổi độ sáng ảnh với giá trị lấy từ trackbar
#e. Nhấn phím S để lưu ảnh, nhấn Q để thoát
import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
cv2.namedWindow("Trackbar")
def nothing(x):pass
cv2.createTrackbar("Kernel","Trackbar",1,10,nothing)
cv2.createTrackbar("DoSang","Trackbar",127,255,nothing)
while True:
    k = cv2.getTrackbarPos("Kernel","Trackbar")*2+1
    beta = cv2.getTrackbarPos("DoSang","Trackbar")-127
    kq=cv2.GaussianBlur(img, (k,k),0)
    kq=cv2.convertScaleAbs(kq, alpha=1, beta=beta)
    cv2.imshow("Trackbar",kq)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite("Anhcau2.jpg",kq)

cv2.destroyAllWindows()