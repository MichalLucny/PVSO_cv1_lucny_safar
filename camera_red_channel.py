import cv2
import numpy as np

img = cv2.imread('out.jpg')

height, width,  Bpp = img.shape

print(img.shape)

img[(height//2):height, 0:(width//2),  0] = 0
img[(height//2):height, 0:(width//2),  1] = 0

cv2.imwrite('out2.png', img)
