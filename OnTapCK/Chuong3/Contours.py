#Viết chương trình đọc ảnh
#Chuyển xám, lọc ảnh bằng bộ lọc trung vị
#Tách biên sobel cho ảnh
#Tìm contours và vẽ contours
import cv2
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
xam = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
loc = cv2.medianBlur(xam, 5)

gradx = cv2.Sobel(loc, cv2.CV_64F, 1,0,3)
grady = cv2.Sobel(loc, cv2.CV_64F,0,1,3)
absx = cv2.convertScaleAbs(gradx)
absy = cv2.convertScaleAbs(grady)
tb = cv2.addWeighted(absx, 0.5, absy, 0.5, 0)

contours, _ = cv2.findContours(tb, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
kq = cv2.drawContours(img, contours, -1, (0,255,0),2)

cv2.imshow("Anh",kq)
cv2.waitKey(0)
cv2.destroyAllWindows()