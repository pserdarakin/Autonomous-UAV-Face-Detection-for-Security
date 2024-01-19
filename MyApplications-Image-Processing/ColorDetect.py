import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_yellow = np.array([20, 110, 110])
	upper_yellow = np.array([40, 255, 255])

	yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

	(_,contours,_) = cv2.findContours(yellow_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for contour in contours: 		
		area = cv2.contourArea(contour)

		if(area > 800):
			x,y,w,h = cv2.boundingRect(contour)
			frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),10)


	cv2.imshow("tracking", frame)

	k = cv2.waitKey(5) & 0XFF 
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()