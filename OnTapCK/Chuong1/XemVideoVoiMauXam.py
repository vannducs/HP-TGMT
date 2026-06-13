#Đọc video, xem video với màu xám, s lưu ảnh, q thoát
import cv2
cap = cv2.VideoCapture(r"C:\Users\DELL\Downloads\kjjjjk.mp4")
c=0
while True:
    ret, frame = cap.read()
    if not ret: break
    xam = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("video",xam)
    key = cv2.waitKey(40)
    if key==ord("s"):
        cv2.imwrite(f"anhxam{c}.jpg",xam)
        c=c+1
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
