#viết chương trình đọc ảnh
#sau đó cắt ảnh tùy ý
import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
h,w = img.shape[:2]
kq=img[0:h//2,0:w//2]
cv2.imshow("bd",img)
cv2.imshow("kq",kq)
cv2.waitKey(0) 
cv2.destroyAllWindows()