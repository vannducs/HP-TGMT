#Viết chương trình thực hiện các yêu cầu sau.
#a. đọc video từ tệp, in ra thông tin số khung hình trong 1 giây của video.
#b. xem video với màu xám.
#c. đọc video từ tệp, lấy ra 1 ảnh từ video khi ấn phím x.
#d. thực hiện phép giãn nở dilate đối với ảnh cắt được.
import cv2
cap = cv2.VideoCapture(r"C:\Users\DELL\Downloads\PXL_20260118_043751636.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
print("So khung hinh trong 1s la: ",fps)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video",gray) 
    if cv2.waitKey(1)==ord("x"):
        cv2.imwrite("anh.jpg",gray)
    elif cv2.waitKey(1)==ord("q"):
        break
cv2.destroyAllWindows() 