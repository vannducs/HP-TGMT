import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
kq=cv2.resize(img,(300,400))
cv2.imshow("Ketqua",kq)
cv2.waitKey(0)
cv2.destroyAllWindows()