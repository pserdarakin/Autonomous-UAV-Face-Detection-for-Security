import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

logo = np.zeros((500,500,3),np.uint8)
cv.circle(logo,(160,240),43,(0,255,0),43)
cv.circle(logo,(240,120),43,(0,0,255),43)
cv.circle(logo,(320,240),43,(255,0,0),43)
pts = np.array([[160,240],[240,120],[320,240]], np.int32)

cv.polylines(logo,[pts],True,(255,255,255),10,cv.LINE_AA)






cv.imshow('logo.jpg',logo)
cv.waitKey(0)
cv.destroyAllWindows()
