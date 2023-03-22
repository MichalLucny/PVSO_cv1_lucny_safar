import matplotlib.pyplot as plt
import numpy as np
from ximea import xiapi
import cv2 

cam = xiapi.Camera()

cam.open_device()
cam.set_exposure(10000)
cam.set_param("imgdataformat","XI_RGB24")
cam.set_param("auto_wb",1)

image = xiapi.Image()

cam.start_acquisition()

cv2.resizeWindow('img',w,h)

while cv2.waitKey(1) != ord(' '):




    cv2.imshow('img', dst)
    


print("Press space to exit")
while cv2.waitKey(1) != ord(' '):
    continue



