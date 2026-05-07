#Câu 3 (3 điểm): Đọc ảnh màu và thực hiện các yêu cầu sau:
#a. Khử nhiễu bằng bộ lọc song phương (bilateralFilter)
#b. Chuyển ảnh sang xám, phân ngưỡng bằng Otsu
#c. Phân ngưỡng thích nghi với blockSize và C lấy từ trackbar
#d. Tách biên bằng Canny với 2 ngưỡng lấy từ trackbar
#e. Tìm contours từ ảnh Canny, vẽ contours lên ảnh gốc
#f. In ra diện tích, chu vi của contour lớn nhất
#g. Vẽ hình chữ nhật bao quanh contour lớn nhất
#h. Hiển thị ảnh gốc, ảnh Otsu, ảnh Canny, ảnh contours trên matplotlib
import cv2 
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
loc = cv2.bilateralFilter(img, 9,75,75)
gray = cv2.cvtColor(loc, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.namedWindow("Trackbar1")
cv2.namedWindow("Trackbar2")
def nothing(x):pass
cv2.createTrackbar("BlockSize","Trackbar1",2,10,nothing)
cv2.createTrackbar("C","Trackbar1",0,10,nothing)
cv2.createTrackbar("N_tren","Trackbar2",100,200,nothing)
cv2.createTrackbar("N_duoi","Trackbar2",0,100,nothing)
while True:
    b =cv2.getTrackbarPos("BlockSize","Trackbar1")*2+1
    if b in [0,1,2]: b=3
    c =cv2.getTrackbarPos("C","Trackbar1")
    nt =cv2.getTrackbarPos("N_tren","Trackbar2")
    nd =cv2.getTrackbarPos("N_duoi","Trackbar2")
    pntn = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,b,c)
    canny = cv2.Canny(gray,nd,nt)
    contours, _ = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    ve = cv2.drawContours(img.copy(), contours, -1, (0,255,0),2)
    cntmax = sorted(contours, key=cv2.contourArea, reverse=True)[0]
    s = cv2.contourArea(cntmax)
    p = cv2.arcLength(cntmax,True)
    x,y,w,h = cv2.boundingRect(cntmax)
    cnthcn= cv2.rectangle(ve,(x,y),(x+w,y+h),(0,255,255),2)
    cv2.imshow("Trackbar1",pntn)
    cv2.imshow("Trackbar2",canny)
    if cv2.waitKey(1)==ord("q"):
        print("Dien tich contours lon nhat: ",s)
        print("Chu vi contours lon nhat: ",p)
        plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.axis("off"), plt.title("Anh goc")
        plt.subplot(222), plt.imshow(otsu, cmap="gray")
        plt.axis("off"), plt.title("OTSU")
        plt.subplot(223), plt.imshow(canny, cmap="gray")
        plt.axis("off"), plt.title("CANNY")
        plt.subplot(224), plt.imshow(cv2.cvtColor(cnthcn, cv2.COLOR_BGR2RGB))
        plt.axis("off"), plt.title("contour")
        plt.show()
        break
cv2.destroyAllWindows()


