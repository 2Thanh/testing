import cv2 
import numpy
import random
img = cv2.imread("assest/naruto1.jpg", 1)
img = cv2.resize(img,(0,0),fx = 0.8, fy = 0.8)

# Change pixel
# for i in range(100):
#     for j in range(img.shape[1]):
#             img[i][j] -= 100
print(img.shape)

#copy and paste a part of image to another place
tag = img[100:200,600:900]
img[200:300,200:500] = tag
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
