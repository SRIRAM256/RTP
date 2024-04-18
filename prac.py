import cv2  as cv  
import numpy as np

img = np.zeros((200,300,3),np.uint8)
cv.imshow('black',img)
cv.waitKey(0)