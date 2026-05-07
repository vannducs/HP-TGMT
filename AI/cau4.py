#Câu 4 (2 điểm): Đọc video từ webcam và thực hiện các yêu cầu sau:
#a. In ra FPS của webcam
#b. Hiển thị video dưới dạng ảnh xám
#c. Nhấn phím S để lưu ảnh, tự động đặt tên Anh0.jpg, Anh1.jpg,...
#d. Dịch chuyển ảnh vừa lưu sang phải 100px, xuống 50px
#e. Tách biên ảnh đã dịch chuyển bằng Laplacian
#f. Hiển thị ảnh gốc, ảnh dịch chuyển, ảnh tách biên trên matplotlib
#g. Nhấn Q để thoát
import cv2
import matplotlib.pyplot as plt
import numpy as np
cap = cv2.VideoCapture(0)
print("fps cua webcam la: ",cap.get(cv2.CAP_PROP_FPS))
c=0
while True:
    ret, frame = cap.read()
    if not ret: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video",gray)
    key = cv2.waitKey(1)
    if key==ord("s"):
        cv2.imwrite(f"anh{c}.jpg",gray)
        c=c+1
        img= cv2.imread(f"anh{c-1}.jpg")
        M = np.float32([[1,0,100],[0,1,50]])
        h,w = img.shape[:2]
        dichchuyen = cv2.warpAffine(img, M, (w,h))
        laplacian = cv2.Laplacian(dichchuyen,cv2.CV_64F,3)
        lap = cv2.convertScaleAbs(laplacian) 
        plt.subplot(131),plt.imshow(img, cmap="gray")
        plt.axis("off"), plt.title("Anh goc")
        plt.subplot(132),plt.imshow(dichchuyen, cmap="gray")
        plt.axis("off"), plt.title("Dich chuyen")
        plt.subplot(133),plt.imshow(lap, cmap="gray")
        plt.axis("off"), plt.title("Tach bien")
        plt.show()
    if key==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
