import cv2 
img = cv2.imread('assest/naruto1.jpg', 1)
#resize image unchage ratio (ti le) 
img = cv2.resize(img,(0,0), fx = 0.5 , fy = 0.5)
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("re_naruto.jpg",img)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()