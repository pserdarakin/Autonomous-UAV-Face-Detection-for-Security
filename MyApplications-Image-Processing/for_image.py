import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('image_process.jpg',0)
plt.imshow(img, cmap='Blues',interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()