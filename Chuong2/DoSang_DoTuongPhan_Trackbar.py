import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
cv2.namedWindow("Trackbar")
def nothing(x):pass
cv2.createTrackbar("DoTuongPhan","Trackbar",1,3,nothing)
cv2.createTrackbar("DoSang","Trackbar",128,254,nothing)
while True:
    alpha = cv2.getTrackbarPos("DoTuongPhan","Trackbar")/2
    beta = cv2.getTrackbarPos("DoSang","Trackbar")-127
    kq=cv2.convertScaleAbs(img,alpha,beta)
    cv2.imshow("Trackbar",kq)
    if cv2.waitKey(1)==ord("q"): break

cv2.destroyAllWindows()