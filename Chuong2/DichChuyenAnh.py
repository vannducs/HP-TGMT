#Dịch chuyển ảnh sang phải và lên trên
import cv2
import numpy as np
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
M = np.float32([[1,0,50],[0,1,-30]])
h,w= img.shape[:2]
kq= cv2.warpAffine(img,M,(w,h))
cv2.imshow("ketqua",kq)
cv2.waitKey(0) 
cv2.destroyAllWindows()
