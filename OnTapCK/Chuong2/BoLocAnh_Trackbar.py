#Tạo từng trackbar cho từng bộ lọc và xem sự thay đổi của ảnh
import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
cv2.namedWindow("Trackbar")
def nothing(x): pass
cv2.createTrackbar("Blur","Trackbar",0,10,nothing)
cv2.createTrackbar("medianBlur","Trackbar",0,10,nothing)
cv2.createTrackbar("GaussianBlur","Trackbar",0,10,nothing)
cv2.createTrackbar("bilateralFilter","Trackbar",0,10,nothing)
while True:
    bl=cv2.getTrackbarPos("Blur","Trackbar")
    me=cv2.getTrackbarPos("medianBlur","Trackbar")*2+1
    ga=cv2.getTrackbarPos("GaussianBlur","Trackbar")*2+1
    bi=cv2.getTrackbarPos("bilateralFilter","Trackbar")
    if bl==0: bl=1 
    if bi==0: bi=1
    kq=cv2.blur(img,(bl,bl))
    kq=cv2.medianBlur(kq,me)
    kq=cv2.GaussianBlur(kq,(ga,ga),0)
    kq=cv2.bilateralFilter(kq,bi,75,75)
    cv2.imshow("Trackbar",kq)
    if cv2.waitKey(1)==ord("q"):break

cv2.destroyAllWindows()
