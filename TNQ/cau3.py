#Đọc ảnh màu và thực hiện các yêu cầu sau.
#a. khử nhiễu ảnh bằng bộ lọc gauss.
#b. thực hiện phân ngưỡng ảnh bằng thuật toán phân ngưỡng tối ưu.
#c. tách biên ảnh bằng phương pháp tách biên canny.
#d. hiển thị ảnh ban đầu, các ảnh kết quả trên matplotlib.
#e. khử nhiễu ảnh bằng bộ lọc trung bình.
#f. thực hiện phân ngưỡng ảnh bằng thuật toán phân ngưỡng thích nghi.
#j. tách biên ảnh bằng phương pháp tách biên laplace.
import cv2
import matplotlib.pyplot as plt
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imga=cv2.GaussianBlur(img,(5,5),0)
graya = cv2.cvtColor(imga, cv2.COLOR_BGR2GRAY)
ret,imgb=cv2.threshold(graya,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
imgc=cv2.Canny(gray,100,200)
imge = cv2.blur(img,(3,3))
graye = cv2.cvtColor(imge, cv2.COLOR_BGR2GRAY)
imgf = cv2.adaptiveThreshold(graye,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,7,0)
lap = cv2.Laplacian(gray,cv2.CV_64F,3)
imgj = cv2.convertScaleAbs(lap)

plt.subplot(421), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("AnhGoc")
plt.subplot(422), plt.imshow(cv2.cvtColor(imga, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("Gauss")
plt.subplot(423), plt.imshow(imgb, cmap = "gray")
plt.axis("off"), plt.title("PN_toiuu")
plt.subplot(424), plt.imshow(imgc, cmap = "gray")
plt.axis("off"), plt.title("TB_Canny")
plt.subplot(425), plt.imshow(cv2.cvtColor(imge, cv2.COLOR_BGR2RGB))
plt.axis("off"), plt.title("BLTB")
plt.subplot(426), plt.imshow(imgf, cmap = "gray")
plt.axis("off"), plt.title("PN_tn")
plt.subplot(427), plt.imshow(imgj, cmap = "gray")
plt.axis("off"), plt.title("TB_Laplace")
plt.show()
