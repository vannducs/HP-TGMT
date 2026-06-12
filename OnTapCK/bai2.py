import cv2
cap = cv2.VideoCapture(r"C:\Users\DELL\Downloads\vdppt.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
c =0
print("Fps la; ",fps)
while True:
    ret, frame = cap.read()
    cv2.imshow("Goc",frame)
    cv2.imshow("Xam", cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    k = cv2.waitKey(1)
    if k == ord("s"):
        cv2.imwrite(f"anh{c}.jpg",frame)
        anhxam = cv2.imread(f"anh{c}.jpg",1)
        canny = cv2.Canny(anhxam,100,200)
        cv2.imwrite(f"canny{c}.jpg",canny)
        c=c+1
    elif k == ord("q"): break

cap.release()
cv2.destroyAllWindows()

