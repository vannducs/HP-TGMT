#Đọc video, xem video với màu xám, s lưu ảnh, q thoát
import cv2
cap = cv2.VideoCapture(r"C:\Users\DELL\Downloads\PXL_20260118_043751636.mp4")
count = 0
while True:
    ret, frame = cap.read()
    if not ret: break
    anhx=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video",anhx)
    key = cv2.waitKey(1)
    if key == ord("s"):
        filename=f"anh{count}.jpg"
        cv2.imwrite(filename,anhx)
        count=count+1
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()