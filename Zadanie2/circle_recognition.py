import cv2

import numpy as np
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    #cv2.imshow("test", frame)

    k = cv2.waitKey(1)
#identifikacia kruhu
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #gray = cv2.Laplacian(gray, -1, 3)
    gray = cv2.medianBlur(gray, 5)


    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=90, param2=55, minRadius=10, maxRadius=110)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(frame, center, 1, (0, 100, 100), 3)
            #cv2.circle(gray, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            #print(i[2])
            cv2.circle(frame, center, radius, (255, 0, 255), 3)
            #cv2.circle(gray, center, radius, (255, 0, 255), 3)

    cv2.imshow("test", frame)
    #cv2.imshow("test", gray)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    #elif k%256 == 32:
        # SPACE pressed
     #   img_name = "opencv_frame_{}.png".format(img_counter)
      #  cv2.imwrite("imagedata2/" + img_name, frame)

       # print("{} written!".format(img_name))
        #img_counter += 1

cam.release()

cv2.destroyAllWindows()