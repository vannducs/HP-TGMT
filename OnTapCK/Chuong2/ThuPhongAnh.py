#Viết chương trình đọc ảnh
#In ra giá trị màu tại 1 tọa độ nhập vào từ bàn phím
#Thu phóng ảnh theo 1 tỷ lệ nhập vào từ bàn phím
#Lọc ảnh bằng 4 bộ lọc khác nhau bằng ảnh đã thu phóng
#Chuyển màu xám cho ảnh đã thu phóng
#Hiển thị tất cả 6 ảnh sau bằng thư viện matplotlib bao gồm ảnh gốc
import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
x = int(input("Nhập tọa độ x: "))
y = int(input("Nhập tọa độ y: "))
b, g, r = img[y,x]
h, w = img.shape[:2]
print(f"gia tri mau b={b} ,g={g} ,r={r}")
tl = int(input("Nhap ty le: "))

tp = cv2.resize(img,(w*tl,h*tl))
xam = cv2.cvtColor(tp, cv2.COLOR_BGR2GRAY)

tb = cv2.blur(tp, (3,3))
tv = cv2.medianBlur(tp, 5)
gauss = cv2.GaussianBlur(tp, (5,5),0)
sp = cv2.bilateralFilter(tp, 9, 75,75)

plt.subplot(321), plt.imshow(cv2.cvtColor(tb, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("Trung binh")
plt.subplot(322), plt.imshow(cv2.cvtColor(tv, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("Trung vi")
plt.subplot(323), plt.imshow(cv2.cvtColor(gauss, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("Gaussian")
plt.subplot(324), plt.imshow(cv2.cvtColor(sp, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("Song phuong")
plt.subplot(325), plt.imshow(xam, cmap="gray")
plt.axis("off"), plt.title("Xam")
plt.subplot(326), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("Goc")
plt.show()