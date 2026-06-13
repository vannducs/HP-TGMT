#viết chương trình đọc video, xem video
#Nhấn phím s để lưu video sao cho mỗi lần nhấn sẽ lưu thành các file khác nhau
#Nhấn q để thoát
import cv2
cap = cv2.VideoCapture(r"C:\Users\DELL\Downloads\kjjjjk.mp4")
c=0
while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    if not ret: break
    key = cv2.waitKey(40)
    if key == ord("s"):
        cv2.imwrite(f"anh{c}.jpg",frame)
        c=c+1
    elif key ==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
