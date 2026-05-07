import cv2
cap = cv2.VideoCapture(0)
c=0
while True:
    ret, frame = cap.read()
    cv2.imshow("Video",frame)
    k = cv2.waitKey(1) 
    if k==ord("s"):
        filename = f"anh{c}.jpg"
        cv2.imwrite(filename,frame)
        c=c+1
    elif k==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()