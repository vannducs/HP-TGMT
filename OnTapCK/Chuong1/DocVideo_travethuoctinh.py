#ĐỌc video, hiển thị video, in ra các chỉ số fps, tổng số khung hình
#thời lượng video, nhấn phím s để lưu ảnh màu và ảnh xám, nhấn q để thoát
import cv2
cap = cv2.VideoCapture(r"C:\Users\DELL\Downloads\kjjjjk.mp4")
c=0
fps = cap.get(cv2.CAP_PROP_FPS)
tf = cap.get(cv2.CAP_PROP_FRAME_COUNT)
time = tf/fps
while True:
    ret, frame = cap.read()
    if not ret: break
    cv2.imshow("video",frame)
    k = cv2.waitKey(40)
    if k==ord("s"):
        cv2.imwrite(f"anhmau{c}.jpg",frame)
        cv2.imwrite(f"anhxam{c}.jpg",cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        c=c+1
    elif k==ord("q"):break

print("fps la: ",fps)
print("tong so khung hinh: ",tf)
print("thoi luong video: ",time)
cap.release()
cv2.destroyAllWindows()




