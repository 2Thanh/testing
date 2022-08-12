from cvzone.SerialModule import SerialObject
import cv2

arduino = SerialObject("COM5")#auto detect COM
light_on = cv2.imread('Outputs/Resources/light_on.jpg')
light_off = cv2.imread('Outputs/Resources/light_off.jpg')
light_off = cv2.resize(light_off,(light_on.shape[1],light_on.shape[0]))

while True:
    arduino.sendData([1])
    cv2.imshow("Image",light_on)
    cv2.waitKey(1000)
    arduino.sendData([0])
    cv2.imshow("Image",light_off)
    cv2.waitKey(1000)
