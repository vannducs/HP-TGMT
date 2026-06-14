#Viết chương trình đọc ảnh
#Dùng trackbar để tách biên laplace
import cv2
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
cv2.namedWindow("Anh")
def nothing(x):pass
cv2.createTrackbar("Lap","Anh",0,10,nothing)
xam = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
while True:
    lap = cv2.getTrackbarPos("Lap","Anh")*2+1
    laplace = cv2.Laplacian(xam, cv2.CV_64F, lap)
    kq1 = cv2.convertScaleAbs(laplace)
    cv2.imshow("Anh",kq1)
    if cv2.waitKey(1)==ord("q"):
        break

cv2.destroyAllWindows()