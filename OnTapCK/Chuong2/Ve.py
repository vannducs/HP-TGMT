#Đọc ảnh, chuyển ảnh sang ảnh xám,
#Vẽ hình chữ nhật, hình tròn, elip, mũi tên, đường thẳng lên ảnh
#Viết dòng chữ Hello World lên ảnh
import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
h, w = img.shape[:2]
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray= cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) 
img1=cv2.rectangle(gray,(100,100),(200,200),(0,0,255),3)
img2=cv2.circle(img1,(w//2,h//2),100,(255,255,0),-1)
img3=cv2.ellipse(img2,(w//2,h//2),(200,100),0,0,360,(255,0,0),2)
img4=cv2.line(img3,(0,0),(w,h),(0,255,0),3)
img5=cv2.putText(img4,"Hello World",(50,200),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,255),3)
cv2.imshow("Ketqua",img5)
cv2.waitKey(0)
cv2.destroyAllWindows()