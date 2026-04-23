import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
locanh = cv2.bilateralFilter(img,9,75,75)
gray = cv2.cvtColor(locanh, cv2.COLOR_BGR2GRAY)
Laplacian = cv2.Laplacian(gray, cv2.CV_64F, 3)
kq = cv2.convertScaleAbs(Laplacian)
cv2.imshow("Ketqua",kq)
cv2.waitKey(0)
cv2.destroyAllWindows()