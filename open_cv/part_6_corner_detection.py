
import numpy as np
import cv2
from random import randint
img = cv2.imread("assest/chessboard.png",1) 
img = cv2.resize(img,(0,0),fx = 0.5 ,fy = 0.5)

#requied to gray
gray_img =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Toshira muira algorithm to detect coordinate of corners in an image
corners = cv2.goodFeaturesToTrack(gray_img, 100 , 0.01 , 10)

#convert float coordinate to int
corners = np.int0(corners)

#draw cirle at the each corners
for corner in corners:
    x,y = corner.ravel() #remover [] sample: [[1,2]] => [1,2] ; [[1,2],[2,3]] =>[1,2,2,3]
    cv2.circle(img,(x,y),5,(255,255,0),-1)#bgr color BUT NOT BECAUSE WE ARE ON GRAY COLOR 

#draw lines at the each of corner
for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = (randint(0,255),randint(0,255),randint(0,255))
        cv2.line(img,corner1,corner2,color,1)

cv2.imshow("chess board image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()