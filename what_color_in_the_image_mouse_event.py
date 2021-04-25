import numpy as np
import cv2


# these parameters int the function given below are fixed
def click_event(event, x, y, flags, param):
    # this will print (x, y) coordinates of the pixel clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

        # creating a coloured image using numpy
        mycolorImage = np.zeros((512, 512, 3), np.uint8)

        # this is still a black coloured image, thus the code below changes it into coloured one
        mycolorImage[:] = [blue, green, red]

        # new window named color which shows the color of different pixels
        cv2.imshow('color', mycolorImage)


# plain black IMAGE using Numpy from the statement below
# img = np.zeros((512, 512, 3), np.uint8)

# importing a colored image/loading a colored img
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points = []
# calling the click_event function
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
