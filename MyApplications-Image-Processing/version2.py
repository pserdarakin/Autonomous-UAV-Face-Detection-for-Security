import numpy as np
import cv2 as cv
filename = 'chessboard.png'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
img[dst>0.01*dst.max()]=[(0,0,255)]
cv.imshow('dst',img)
cv.waitKey(0)
cv.destroyAllWindows()