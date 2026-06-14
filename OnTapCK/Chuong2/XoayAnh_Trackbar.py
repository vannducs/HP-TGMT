#Phân ngưỡng thích nghi cho ảnh
#xoay ảnh với góc xoay lấy từ trackbar
import cv2
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
loc = cv2.GaussianBlur(img, (5,5),0)
xam = cv2.cvtColor(loc, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(xam,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7,0)

cv2.namedWindow("Anh")
def nothing(x):pass
h, w = thresh.shape[:2]
cv2.createTrackbar("GX","Anh",0,360,nothing)
while True:
    gx = cv2.getTrackbarPos("GX","Anh")
    M = cv2.getRotationMatrix2D((w//2,h//2),gx,1)
    kq = cv2.warpAffine(thresh, M, (w,h))
    cv2.imshow("Anh",kq)
    if cv2.waitKey(1)==ord("q"):break

cv2.destroyAllWindows()