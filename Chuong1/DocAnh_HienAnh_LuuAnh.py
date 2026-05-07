import cv2
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
cv2.imshow("ketqua",img)
k = cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite("Chuong1/anh.jpg",img)

cv2.destroyAllWindows() 

