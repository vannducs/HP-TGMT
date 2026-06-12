import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
kq=cv2.convertScaleAbs(img, alpha=0.7, beta=0)
cv2.imshow("Ketqua",kq)
cv2.waitKey(0) 
cv2.destroyAllWindows()
