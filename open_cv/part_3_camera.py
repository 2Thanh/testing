import numpy as np
import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(3))#get width
height = int(cap.get(4))
while True:
    ret, frame = cap.read()
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame,(0,0), fx = 0.5,fy = 0.5)
    image[:height//2,:width//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180) #top left
    image[:height//2,width//2:] = smaller_frame #top right
    image[height//2:,:width//2] = smaller_frame#bottom left
    image[height//2:,width//2:] = smaller_frame# bottom right
    cv2.imshow("frame",image)
    if (cv2.waitKey(1 ) == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()