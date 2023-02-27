import cv2
import numpy as np

from camera_red_channel import red_channel
from camera_kernel_mask import kernel_mask
from camera_rotation import rotation
from print_info import print_info

def camera_process_images():
    #mozaika
    img1 = cv2.imread('imagedata/image0.jpg')
    img2 = cv2.imread('imagedata/image1.jpg')
    img3 = cv2.imread('imagedata/image2.jpg')
    img4 = cv2.imread('imagedata/image3.jpg')

    vis = np.concatenate((img1, img2), axis=1)
    vis2 = np.concatenate((img3, img4), axis=1)

    img = np.concatenate((vis, vis2), axis=0)

    #zapis na disk
    cv2.imwrite('mosaic.png', img)

    #spracovanie

    #kernel maska
    kernel_mask(img)

    #otocenie
    rotation(img)

    #izolovanie cerveneho kanala
    red_channel(img)

    print_info(img)


    cv2.imwrite('out.png', img)
