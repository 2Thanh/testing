import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#the original color is BGA type
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    width = int(cap.get(3))
    height = int(cap.get(4))

    #convert color from rgb to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #lower and upper blue HSV

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv, lower_blue , upper_blue)
    
    #compare by mask if pixel has HSV between lower_blue and upper_blue => True(1)
    #anything else is False 1 1 = 1 , 1 0 = 0 , 0 0 = 0 , 0 1 = 0
    result = cv2.bitwise_and(frame, frame, mask = mask)


    cv2.imshow('frame',mask)
    cv2.imshow('mask', mask)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


#Change 1 pixel [0][0]
# BGR_color = np.array([[[255,0,0]]])
# x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
# x[0][0]