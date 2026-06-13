#viết chương trình đọc ảnh, hiện thị chiều cao, chiều rộng ảnh
#lọc ảnh bằng bộ lọc song phương, xoay ảnh âm bản 1 góc 30 độ tâm xoay giữa ảnh
import cv2
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
h, w = img.shape[:2]
print(f"Chieu cao la: {h},Chieu rong la: {w}")
loc = cv2.bilateralFilter(img,9,75,75)
amban = 255-loc
M = cv2.getRotationMatrix2D((w//2,h//2),30,1)
kq = cv2.warpAffine(amban, M, (w,h))
cv2.imshow("Ketqua",kq)

cv2.waitKey(0)
cv2.destroyAllWindows()
