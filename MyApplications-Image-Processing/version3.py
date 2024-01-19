import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
video_capture = cv2.VideoCapture(1)

def mouseHandler(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.circle(frame, (x, y), 3, (255, 0, 0), -1)


cv2.setMouseCallback('Video', mouseHandler)


while(True):

frame = video_capture.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('Video',frame)

video_capture.release()
cv2.destroyAllWindows()