import numpy as np
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    #flip the camera
    frame = cv2.flip(frame,1)
    #Get width and height in camera
    width = int(cap.get(3))
    height = int(cap.get(4))
    # img = np.zeros((10,100,3),dtype = np.uint8)
    # frame[10,100] = img
    img = cv2.line(frame,(0,0),(width,height),( 255,0,0),10)
    img = cv2.line(img,(width,0),(0,height),( 255,0,0),10)
    img = cv2.rectangle(img,(0,0),(290,60),(0,0,250),5)
    img = cv2.circle(img,(width//2,height//2),20,(68,200,3),10)
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    img = cv2.putText(img,"Tech with Thanh",(0,40),font, 1 ,(200,200,200),2,cv2.LINE_AA)
    cv2.imshow('frame',img)

    if cv2.waitKey(1) == ord('q'): #when press q => break
        break

cap.release()
cv2.destroyAllWindows()