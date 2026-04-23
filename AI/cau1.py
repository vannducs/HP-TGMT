#Câu 1 (2 điểm): Đọc ảnh màu và thực hiện các yêu cầu sau:
#a. In ra kích thước ảnh (chiều rộng, chiều cao)
#b. In ra giá trị màu BGR tại tọa độ (150, 200)
#c. Cắt ảnh lấy góc dưới bên trái, lưu ảnh vừa cắt
#d. Hiển thị ảnh gốc và ảnh cắt trên matplotlib
import cv2
import matplotlib.pyplot as plt
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
h, w=img.shape[:2]
print(f"Chieu rong la {w}, chieu cao la {h}")
b,g,r = img[150,200]
print(f"Gia tri mau la b:{b},g:{g},r:{r}")
cat = img[h//2:h,w//2:w]
cv2.imwrite("anhcat.jpg",cat)
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Anh goc")
plt.subplot(122), plt.imshow(cv2.cvtColor(cat, cv2.COLOR_BGR2RGB))
plt.title("Anh cat")
plt.show()


