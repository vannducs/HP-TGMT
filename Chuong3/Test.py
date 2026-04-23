import cv2
import numpy as np

img= cv2.imread("Anh0.jpg")
loc = cv2.medianBlur(img,5)
gray = cv2.cvtColor(loc, cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(gray, cv2.CV_64F,3)
laplace = cv2.convertScaleAbs(laplacian)
img3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,7,2)

contours, _ = cv2.findContours(laplace,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img4 = cv2.drawContours(img,contours,-1,(0,255,0),2)
s = cv2.contourArea(contours[3])
p = cv2.arcLength(contours[3],True)
print("Dien tich contours[3]=",s)
print("Chu vi contours[3]=",p)
x,y,w,h = cv2.boundingRect(contours[3])
img4= cv2.rectangle(img4,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("a",laplace)
cv2.imshow("b",img3)
cv2.imshow("c",img4)
cv2.waitKey(0)
cv2.destroyAllWindows()

