import cv2
import numpy as np
def nothing(x):
    pass
while True:
    frame = cv2.imread('smarties.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)