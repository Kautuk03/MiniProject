import numpy as np
import cv2
# printing all the different types of EVENTS available.
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

# these parameters int the function given below are fixed
def click_event(event, x, y, flags, param):
    #this will print (x, y) coordinates of the pixel clicked
     if event == cv2.EVENT_LBUTTONDOWN:
         cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
         #saving the coordinates wherever the mouse is clicked in an array
         points.append((x, y))
         if len(points) >=2:

             #joining the last two points clicked with a lin
             cv2.line(img, points[-1], points[-2], (255, 0, 0), 5 )
         cv2.imshow('image', img)


# plain black IMAGE using Numpy from the statement below
img = np.zeros((512, 512, 3), np.uint8)

#importing a colored image
#img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points = []
# calling the click_event function
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
