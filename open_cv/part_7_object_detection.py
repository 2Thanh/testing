import numpy as np
import cv2

img = cv2.imread('assest/soccer_practice.jpg',0)
img = cv2.resize(img,(0,0), fx = 0.5,fy = 0.5)
template = cv2.imread('assest/shoe.png',0)
template = cv2.resize(template,(0,0), fx = 0.5,fy = 0.5)


h,w = template.shape

methods = [cv2.TM_CCOEFF,cv2.TM_CCORR_NORMED,cv2.TM_CCOEFF,
            cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2, template,method)
    #max_val or min_val depend on the method you use
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc #location
    #w: width of the template and h: height of the template
    bottom_right = (location[0] + w , location[1] +h)
    #location is the colation where we find the template in the original image
    cv2.rectangle(img2 , location, bottom_right  , 255,2)
    cv2.imshow("match",img2)
    cv2.waitKey()
    cv2.destroyAllWindows()

#heigh width