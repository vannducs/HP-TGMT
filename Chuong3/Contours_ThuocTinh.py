#Hiển thị contours của ảnh, In ra các thuộc tính của contour
import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
loc = cv2.blur(img, (3,3))
gray = cv2.cvtColor(loc, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 100,200)
contours, _ = cv2.findContours(canny,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
draw = cv2.drawContours(img, contours,-1, (0,255,0),2)
cv2.imshow("Ketqua",draw)
#DIENTICH CONTOURS
s = cv2.contourArea(contours[0])
print("Dien tich: ", s)
#CHU VI CONTOURS
p= cv2.arcLength(contours[0],True)
print("Chu vi: ",p)
#SAP XEP CONTOURS
sort = sorted(contours,key=cv2.contourArea)
#print(sort)
#HCN bao quanh contours
x,y,w,h = cv2.boundingRect(contours[0])
hcn = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#XAPXI contours bang da giac
epsilon=0.1*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
print("Xap xi bang: ",len(approx))
cv2.imshow("hcn",hcn)
cv2.waitKey(0)
cv2.destroyAllWindows()