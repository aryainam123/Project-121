import cv2  
import numpy as np  
frame = cv2.VideoCapture(0)
image = "image.jpg"

cap = cv2.VideoCapture(0)  
frame = cv2.resize(frame, (640, 480)) 
image = cv2.resize(image, (640, 480)) 
u_black = np.array([104, 153, 70]) 
l_black = np.array([30, 30, 0]) 
mask = cv2.inRange(frame, l_black, u_black) 
res = cv2.bitwise_and(frame, frame, mask = mask) 
f = frame - res 
f = np.where(f == 0, image, f) 
  
cv2.imshow("Magic",frame)
cv2.waitKey(1)

frame.release() 
cv2.destroyAllWindows() 