import numpy
from numpy import *
import cv2

#img = cv2.imread('out.jpg')
def print_info(img):    
    print("Datovy typ:", img.dtype)
    print("\nRozmer:", img.shape[0], "x", img.shape[1])
    print("\nVelkost:", img.size, "px")