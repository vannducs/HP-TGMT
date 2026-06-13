#Viết chương trình đọc ảnh, hiện ảnh lên màn hình, nhấn s để lưu ảnh, 
import cv2
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
cv2.imshow("anh",img)
k = cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite("anh.jpg",img)

cv2.destroyAllWindows()
