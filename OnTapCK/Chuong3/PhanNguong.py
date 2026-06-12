#Viết chương trình đọc video từ webcam, nhấn s để lưu ảnh, nhấn q để thoát
#1)dịch chuyển ảnh vừa lưu sang phải 50pixel, lên trên 10pixel
#2)xoay ảnh vừa lưu sang phải 1 góc 180 độ
#3)phân ngưỡng thích nghi cho ảnh, tách biên bằng Laplace
#4)vẽ contours và in ra diện tích, chu vi, vẽ HCN bao quanh contours thứ i=3
# hiển thị 4 ảnh lên subplot
import cv2
import numpy as np
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)
count=0
while True:
    ret, frame = cap.read()
    if not ret: break
    cv2.imshow("Video",frame)
    key= cv2.waitKey(1)
    if key == ord("s"):
        filename=f"Anh{count}.jpg"
        cv2.imwrite(filename,frame)
        count=count+1
    elif key == ord("q"): break
img= cv2.imread("Anh0.jpg")
M = np.float32([[1,0,50],[0,1,-10]])
h,w = img.shape[:2]
img1 = cv2.warpAffine(img,M,(w,h)) #1 

M1 = cv2.getRotationMatrix2D((w//2,h//2),180,1)
img2= cv2.warpAffine(img, M1, (w,h))

loc = cv2.medianBlur(img,5)
gray = cv2.cvtColor(loc, cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(gray, cv2.CV_64F,3)
laplace = cv2.convertScaleAbs(laplacian)
img3 = cv2.adaptiveThreshold(laplace,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,7,2)

contours, _ = cv2.findContours(laplace,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img4 = cv2.drawContours(img,contours,-1,(0,255,0),2)
s = cv2.contourArea(contours[3])
p = cv2.arcLength(contours[3],True)
print("Dien tich contours[3]=",s)
print("Chu vi contours[3]=",p)
x,y,w,h = cv2.boundingRect(contours[3])
img4= cv2.rectangle(img4,(x,y),(x+w,y+h),(255,0,0),2)

plt.subplot(221), plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("Dich chuyen")
plt.subplot(222), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("Xoay anh")
plt.subplot(223), plt.imshow(img3, cmap="gray")
plt.axis("off"), plt.title("Phan nguong")
plt.subplot(224), plt.imshow(cv2.cvtColor(img4, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("Contours")
plt.show()




    