#ĐỌc video, hiển thị video, in ra các chỉ số fps, tổng số khung hình
#thời lượng video, nhấn phím s để lưu ảnh màu và ảnh xám, nhấn q để thoát
import cv2
cap = cv2.VideoCapture(r"C:\Users\DELL\Downloads\PXL_20260118_043751636.mp4")
count = 0
fps = cap.get(cv2.CAP_PROP_FPS)
total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
time = total_frame/fps 
while True:
    ret, frame = cap.read()
    if not ret: break
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key==ord("s"):
        fn =f"anhmau{count}.jpg"
        fnx =f"anhxam{count}.jpg"
        cv2.imwrite(fn,frame)
        cv2.imwrite(fnx, cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY))
        count=count+1
    elif key==ord("q"):
        break

cap.release()
print("FPS la: ",fps)
print("Tong so frame: ",total_frame)
print("Thoi luong video: ",time)
cv2.destroyAllWindows()



