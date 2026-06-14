#Tạo từng trackbar cho từng bộ lọc và xem sự thay đổi của ảnh
import cv2
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
cv2.namedWindow("Anh")
def nothing(x):pass
cv2.createTrackbar("Trungbinh","Anh",1,5,nothing)
cv2.createTrackbar("Trungvi","Anh",1,5,nothing)
cv2.createTrackbar("Gauss","Anh",1,5,nothing)
cv2.createTrackbar("Songphuong","Anh",1,10,nothing)
while True:
    tb = cv2.getTrackbarPos("Trungbinh","Anh")
    tv = cv2.getTrackbarPos("Trungvi","Anh")*2+1
    gauss = cv2.getTrackbarPos("Gauss","Anh")*2+1
    sp = cv2.getTrackbarPos("Songphuong","Anh")
    if tb==0: tb=1
    if sp==0: sp=1
    imgtb = cv2.blur(img, (tb,tb))
    imgtv = cv2.medianBlur(imgtb, tv)
    imgg = cv2.GaussianBlur(imgtv, (gauss,gauss),0)
    imgsp = cv2.bilateralFilter(imgg, sp, 75,75)
    cv2.imshow("Anh",imgsp)
    if cv2.waitKey(1)==ord("q"):
        break

cv2.destroyAllWindows()


