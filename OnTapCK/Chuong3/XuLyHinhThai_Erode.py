#Viết chương trình đọc ảnh
#cắt ảnh góc dưới bên phải
#thực hiện phép co và dãn cho ảnh đã cắt
import cv2
import numpy as np
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
h, w =img.shape[:2]
cat = img[h//2:h,w//2:w]

loc = cv2.blur(cat, (3,3))
xam = cv2.cvtColor(loc, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(xam, 100,200)

kernel = np.ones((5,5),np.uint8)
co = cv2.erode(canny, kernel, iterations=1)
dan = cv2.dilate(canny, kernel, iterations=1)
mo = cv2.morphologyEx(canny, cv2.MORPH_OPEN, kernel)
dong = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Ketqua",dong)
cv2.waitKey(0)
cv2.destroyAllWindows()
