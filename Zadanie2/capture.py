from ximea import xiapi
import cv2

### runn this command first echo 0|sudo tee /sys/module/usbcore/parameters/usbfs_memory_mb  ###

#create instance for first connected camera
cam = xiapi.Camera()


#start communication
#to open specific device, use:
#cam.open_device_by_SN('41305651')
#(open by serial number)
print('Opening first camera...')
cam.open_device()

#settings
cam.set_exposure(10000)
cam.set_param("imgdataformat","XI_RGB24")
cam.set_param("auto_wb",1)

print('Exposure was set to %i us' %cam.get_exposure())

#create instance of Image to store image data and metadata
img = xiapi.Image()

#start data acquisition
print('Starting data acquisition...')
cam.start_acquisition()

cv2.namedWindow("video",cv2.WINDOW_NORMAL)

print("Press space to capture")

while cv2.waitKey(10) != ord(' '):
    cv2.waitKey(1)

print("Capturing!\n")

for i in range(20):
    while cv2.waitKey(1) != ord(' '):
        cam.get_image(img)
        image = img.get_image_data_numpy()
        cv2.imshow("video", image)
        continue
    #get data and pass them from camera to img
    cam.get_image(img)
    image = img.get_image_data_numpy()
    cv2.imshow("video", image)

    cv2.imwrite("xipattern" + str(i) + ".jpg",image)

  
print("Capturing done")

#stop data acquisition
print('Stopping acquisition...')
cam.stop_acquisition()

#stop communication
cam.close_device()

