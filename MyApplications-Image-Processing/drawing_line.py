import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = np.zeros((512,512,3),np.uint8)

font = cv.FONT_HERSHEY_PLAIN
cv.putText(img,'OPEN',(100,200), font, 6,(0,255,255),10)
cv.ellipse(img,(210,256),(100,50),0,0,180,255,-1)
cv.line(img,(0,0),(180,180),(255,0,255),5,cv.LINE_AA)


cv.imshow('img.png',img)
cv.waitKey(0)
cv.destroyAllWindows()
