#viết chương trình đọc ảnh, hiện ảnh âm bản
import cv2
img = cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
amban = 255-img
cv2.imshow("Ket qua",amban)
cv2.waitKey(0)
cv2.destroyAllWindows() 