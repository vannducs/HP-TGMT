#Biến đổi phối cảnh ảnh,
#in ra kích thước ảnh trước và sau khi biến đổi
import cv2
import numpy as np
img = cv2.imread(r"C:\Users\DELL\Downloads\tenduong.jpg")
M1 = np.float32([(1055,491),(1620,320),(1649,743),(1060,798)])
M2 = np.float32([(0,0),(500,0),(500,300),(0,300)])
M = cv2.getPerspectiveTransform(M1,M2)
kq= cv2.warpPerspective(img,M,(500,300))
h_pre, w_pre = img.shape[:2]
h,w = kq.shape[:2]
print(f"Kich thuoc ban dau: {h_pre}x{w_pre}")
print(f"Kich thuoc luc sau: {h}x{w}")
cv2.imshow("Ketqua",kq)
cv2.waitKey(0)
cv2.destroyAllWindows()
