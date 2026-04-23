#dùng bộ lọc song phương lọc ảnh, tách biên bằng lapacian
#dịch chuyển ảnh sang phải 100pixel
#in ra kích thước ảnh ban đầu và lúc sau
#in ra giá trị màu của 1 pixel bất kì
#hiển thị ảnh lúc đầu và lúc sau trên subplot
import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
locanh = cv2.bilateralFilter(img,9,75,75)
gray = cv2.cvtColor(locanh, cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(gray,cv2.CV_64F,3)
tachbien = cv2.convertScaleAbs(laplacian)
M = np.float32([[1,0,100],[0,1,0]])
h,w = tachbien.shape[:2]
kq = cv2.warpAffine(tachbien,M,(w,h))
h_pre, w_pre = img.shape[:2]
print(f"Kich thuoc anh ban dau lan luot la: {h_pre}x{w_pre}" )
print(f"Kich thuoc anh luc sau lan luot la: {h}x{w}")
b,g,r = img[200,200]
print(f"Gia tri mau tai vi tri (200,200) co b:{b},g:{g},r:{r}")
plt.subplot(211), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Anh ban dau")
plt.subplot(212), plt.imshow(kq, cmap="gray")
plt.title("Anh luc sau")
plt.show()
