import numpy as np
import cv2
# printing all the different types of EVENTS available.
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

# these parameters int the function given below are fixed
def click_event(event, x, y, flags, param):
    #this will print (x, y) coordinates of the pixel clicked
     if event == cv2.EVENT_LBUTTONDOWN:
         print(x,", ", y)
         font = cv2.FONT_HERSHEY_SIMPLEX
         strXY = str(x) + ', ' + str(y)
         cv2.putText(img, strXY, (x, y), font, .5, (255, 255,0), 2)
         cv2.imshow('image', img)

     #this strBGR will print BGR values of every pixel
     if event == cv2.EVENT_RBUTTONDOWN:
         blue = img[y, x, 0]
         green = img[y, x, 1]
         red = img[y, x, 2]
         font = cv2.FONT_HERSHEY_SIMPLEX
         strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
         cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
         cv2.imshow('image', img)

# plain black IMAGE using Numpy from the statement below
#img = np.zeros((512, 512, 3), np.uint8)

#importing a colored image
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

# calling the click_event function
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
