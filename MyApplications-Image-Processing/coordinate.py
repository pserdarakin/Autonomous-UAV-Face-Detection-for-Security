import cv2      # import the OpenCV library
import numpy as np  # import the numpy library

font = cv2.FONT_HERSHEY_SIMPLEX
video_capture = cv2.VideoCapture(1)

def mouseHandler(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.circle(frame, (x, y), 3, (255, 0, 0), -1)


cv2.setMouseCallback('Video', mouseHandler)



cv2.waitKey(0)


cv2.imshow('Video',0)

video_capture.release()
cv2.destroyAllWindows()