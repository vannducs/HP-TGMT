#Câu 2 (5 điểm)  Đọc ảnh và thực hiện các thao tác sau:
#- Tạo trackbar để lấy kích thước cho kernel.
#- Tạo trackbar để lấy độ tương phản của ảnh
#- Sử dụng bộ lọc trung bình để lọc ảnh với kích thước bộ lọc lấy từ trackbar
#- Thay đổi độ tương phản của ảnh với hệ số tương phản lấy từ trackbar
#- Ấn phím C để lưu lại ảnh kết quả.
import cv2
anh = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
cv2.namedWindow("Trackbar")
def nothing(x):pass
cv2.createTrackbar("Kenel","Trackbar",1,10,nothing)
cv2.createTrackbar("Tuongphan","Trackbar",1,10,nothing)
c=0
while True:
    k = cv2.getTrackbarPos("Kenel","Trackbar")
    alpha = cv2.getTrackbarPos("Tuongphan","Trackbar")
    if k==0: k=1
    if alpha==0: alpha=1
    kq = cv2.blur(anh,(k,k)) 
    kq = cv2.convertScaleAbs(kq, alpha=alpha, beta=0)
    cv2.imshow("Trackbar",kq)
    key = cv2.waitKey(1)
    if key==ord("c"):
        cv2.imwrite(f"Anh{c}.jpg",kq)
        c=c+1
    elif key==ord("q"):
        break
cv2.destroyAllWindows()
