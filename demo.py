import cv2
image = cv2.imread("clouds.jpg")
vidcap = cv2.VideoCapture("security_cam_feed.mov");
count = 0
while vidcap.isOpened():
    ret,frame = vidcap.read()
    cv2.imshow('window-name',frame)
    cv2.imwrite("frame%d.jpg" % count, frame)
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cap.destroyAllWindows()
