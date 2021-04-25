import numpy as np
import cv2

img = cv2.imread("messi5.jpg")
img2 = cv2.imread('opencv-logo.png')

print(img.shape) # returns a tuple of number of rows, columns, and channels
print(img.size)  # returns total no. of pixels is accessed
print(img.dtype) # returns Image data type is obtained 
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# copypasting the ball at a diff location
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# in order to overlap/merge the two images
# their size needs to be same, hence resizing them
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# merge both the images (normal merge)
# dst = cv2.add(img, img2);

# merging two images and setting their weights Ex: 80% 1st img, 20% 2nd img
dst = cv2.addWeighted(img, .8, img2, .2, 0);
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()