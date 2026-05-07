#Tách biên với sobel, giá trị ksize lấy từ trackbar
import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
cv2.namedWindow("Trackbar")
def nothing(x):pass
cv2.createTrackbar("Ksize","Trackbar",0,3,nothing)
anhloc=cv2.blur(img,(3,3))
gray = cv2.cvtColor(anhloc, cv2.COLOR_BGR2GRAY)
while True:
    k = cv2.getTrackbarPos("Ksize","Trackbar")*2+1
    gradx=cv2.Sobel(gray,cv2.CV_64F,1,0,k)
    grady=cv2.Sobel(gray,cv2.CV_64F,0,1,k)
    absx= cv2.convertScaleAbs(gradx)
    absy= cv2.convertScaleAbs(grady)
    kq= cv2.addWeighted(absx,0.5,absy,0.5,0)
    cv2.imshow("Trackbar",kq)
    if cv2.waitKey(1)==ord("q"):break

cv2.destroyAllWindows() 