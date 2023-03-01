import cv2
import numpy as np

#img = cv2.imread('out.jpg')

def kernel_mask(img):
    height, width,  Bpp = img.shape

    #print(img.shape)

    img_roi = img[0:(height//2), 0:(width//2),  :] 

    kernel_mask = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]], np.float32) 

    result = cv2.filter2D(img_roi, -1, kernel_mask)

    img[0:(height//2), 0:(width//2),  :]  = result


#cv2.imwrite('out2.png', img)
