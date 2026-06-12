#Viết chương trình đọc ảnh
#Lọc ảnh bằng bộ lọc bất kì
#Tạo trackbar lấy phân ngưỡng cho phương pháp tách biên Canny
import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
loc = cv2.GaussianBlur(img, (5,5),0)
gray = cv2.cvtColor(loc, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Trackbar")
def nothing(x): pass
cv2.createTrackbar("Threshold1","Trackbar",0,200,nothing)
cv2.createTrackbar("Threshold2","Trackbar",0,200,nothing)
while True: 
    t1=cv2.getTrackbarPos("Threshold1","Trackbar")
    t2=cv2.getTrackbarPos("Threshold2","Trackbar")
    canny = cv2.Canny(gray,t1,t2)
    cv2.imshow("Trackbar",canny)
    if cv2.waitKey(1)==ord("q"): break

cv2.destroyAllWindows()
