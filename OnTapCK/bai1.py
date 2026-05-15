import cv2
import matplotlib.pyplot as plt
img= cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
x =int(input("Nhap toa do x: "))
y=int(input("Nhap toa do y: "))
h, w = img.shape[:2]
cat = img[0:y,0:x]
M = cv2.getRotationMatrix2D((w//2,h//2),-30,1)
xoay = cv2.warpAffine(img,M,(w,h))
loc = cv2.GaussianBlur(img, (5,5),0)
xam = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(xam,127,255, cv2.THRESH_BINARY)
plt.subplot(231), plt.imshow(cv2.cvtColor(cat,cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("Anh cat")
plt.subplot(232), plt.imshow(cv2.cvtColor(xoay, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("Anh xoay")
plt.subplot(233), plt.imshow(cv2.cvtColor(loc, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("Anh loc")
plt.subplot(234), plt.imshow(thresh, cmap="gray")
plt.axis("off"), plt.title("Anh pn")
plt.subplot(235), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("Anh goc")
plt.show()