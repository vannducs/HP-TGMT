import cv2
img=cv2.imread(r"C:\Users\DELL\Downloads\he.jpg")
loc = cv2.blur(img,(3,3))
gray=cv2.cvtColor(loc, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray,100,200)
cv2.imshow("Ketqua",canny)
cv2.waitKey(0)
cv2.destroyAllWindows() 