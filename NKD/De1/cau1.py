#Câu 1 (5 điểm) Đọc ảnh và thực hiện các thao tác sau:
#- Thay đổi kích thước ảnh với hệ số tỉ lệ trục x và trục y nhập vào từ bàn phím. Dùng ảnh này để thực hiện các phép biến đổi tiếp theo
#- Biến đổi ảnh vừa cắt thành ảnh âm bản
#- Tách biên ảnh bằng phương pháp Canny
#- Hiển thị ảnh thay đổi kích thước, ảnh âm bản, ảnh tách biên trên matplotlib
import cv2
import matplotlib.pyplot as plt
anh = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
fx=float(input("Nhap he so truc x: "))
fy=float(input("Nhap he so truc y: "))
img = cv2.resize(anh,None,fx=fx, fy=fy)
neg = 255 -img
loc = cv2.blur(img, (3,3))
gray = cv2.cvtColor(loc, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 100,200)
plt.subplot(311), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("TD KT")
plt.subplot(312), plt.imshow(cv2.cvtColor(neg, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("AmBan")
plt.subplot(313), plt.imshow(canny, cmap="gray")
plt.axis("off"), plt.title("TachBien")
plt.show()
