import numpy as np
import cv2 
from ximea import xiapi


cv2.namedWindow('img',cv2.WINDOW_NORMAL)


cv2.waitKey(10)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((5*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:5].T.reshape(-1,2)

objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

for i in range(20):
    img = cv2.imread("xipattern" + str(i) + ".jpg")
   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret, corners = cv2.findChessboardCorners(gray,(7,5),None)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners, (5,5), (-1,-1), criteria)
        imgpoints.append(corners2)
        cv2.drawChessboardCorners(img, (7,5), corners2, ret)
        
        #cv2.imshow('img', img)
        #cv2.waitKey(10)

    else:
        continue

print("Checkerboard patterns processed\n")

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

h,  w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

x, y, w, h = roi

print (newcameramtx)

fx = newcameramtx[0,0]
fy = newcameramtx[1,1]
cx = newcameramtx[0,2]
cy = newcameramtx[1,2]

print ("focal length: " + str(fx) + " , " + str(fy) + "\n")
print ("optical centre: " + str(cx) + " , " + str(cy) + "\n")

print("Calibration done! Press space view result")
while cv2.waitKey(1) != ord(' '):
    continue

cam = xiapi.Camera()

cam.open_device()
cam.set_exposure(10000)
cam.set_param("imgdataformat","XI_RGB24")
cam.set_param("auto_wb",1)

image = xiapi.Image()

cam.start_acquisition()

cv2.resizeWindow('img',w,h)

while cv2.waitKey(1) != ord(' '):


    cam.get_image(image)
    img = image.get_image_data_numpy()
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
    dst = dst[y:y+h, x:x+w]
    cv2.imshow('img', dst)
    


print("Press space to exit")
while cv2.waitKey(1) != ord(' '):
    continue

