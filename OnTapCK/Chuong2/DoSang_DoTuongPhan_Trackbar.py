#Viết chương trình đọc video, nhấn s để lấy ra 1 ảnh
#lấy track bar chỉnh độ sáng và độ tương phản cho ảnh màu
import cv2
cap = cv2.VideoCapture(0)
cv2.namedWindow("Anh")
def nothing(x): pass
cv2.createTrackbar("DTP","Anh",0,2,nothing)
cv2.createTrackbar("DS","Anh",0,255,nothing)
img =None
while True:
    ret, frame = cap.read()
    if not ret: break
    cv2.imshow("Video",frame)
    k=cv2.waitKey(1)
    if k==ord("s"):
        img = frame.copy()

    if img is not None: 
        alpha = cv2.getTrackbarPos("DTP","Anh")*0.25
        beta = cv2.getTrackbarPos("DS","Anh")
        alpha = max(alpha, 0.1)
        kq = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
        cv2.imshow("Anh",kq)
    
    if k==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

