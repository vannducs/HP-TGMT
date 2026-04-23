#Đọc ảnh màu và thực hiện các yêu cầu sau.
#a. in ra chiều rộng và cao của ảnh.
#b. in giá trị màu của ảnh tại điểm có tọa độ nhập vào.
#c. tăng độ tương phản của ảnh với hệ số tương phản nhập vào từ bàn phím, lưu lại ảnh kết quả.
#d. cắt một phần ảnh với các tọa độ nhập vào từ bàn phím, lưu ảnh vừa cắt.
import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
h,w=img.shape[:2]
x=int(input("Nhap toa do x: "))
y=int(input("Nhap toa do y: "))
alpha=int(input("Nhap he so tuong phan: "))
if alpha<=0:
    print("he so tuong phan >0, nhap lai!")
    alpha=int(input("Nhap he so tuong phan: "))
kq1= cv2.convertScaleAbs(img, alpha=alpha, beta=0)
cv2.imwrite("tuongphan.jpg",kq1)
x1=int(input("Nhap toa do cat anh x1: "))
y1=int(input("Nhap toa do cat anh y1: "))
x2=int(input("Nhap toa do cat anh x2: "))
y2=int(input("Nhap toa do cat anh y2: "))
kq2=img[y1:y2,x1:x2]
cv2.imwrite("catanh.jpg",kq2)
print(f"Chieu rong la {w}, chieu cao la {h}")
b,g,r = img[x,y]
print(f"Gia tri mau tai toa do ({x},{y}) lan luot la b:{b},g:{g},e{r}")



