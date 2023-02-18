import cv2
import numpy as np

img1 = cv2.imread('imagedata/image0.jpg')
img2 = cv2.imread('imagedata/image1.jpg')
img3 = cv2.imread('imagedata/image2.jpg')
img4 = cv2.imread('imagedata/image3.jpg')

vis = np.concatenate((img1, img2), axis=1)
vis2 = np.concatenate((img3, img4), axis=1)

vis3 = np.concatenate((vis, vis2), axis=0)


cv2.imwrite('out.png', vis3)