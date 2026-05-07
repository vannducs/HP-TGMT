import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
cv2.namedWindow("Trackbar")
def nothing(x):pass
cv2.createTrackbar("TyLe","Trackbar",1,10,nothing)
while True:
    tyle = cv2.getTrackbarPos("TyLe","Trackbar")
    h,w = img.shape[:2]
    if tyle==0: 
        tyle=1
    kq= cv2.resize(img,(w*tyle,h*tyle))
    cv2.imshow("Trackbar",kq)
    if cv2.waitKey(1)==ord("q"):break

cv2.destroyAllWindows()