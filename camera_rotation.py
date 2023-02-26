import cv2
import numpy as np


img = cv2.imread('out.jpg')
img2 = cv2.imread('out.jpg')
#--------------------------------------------------------------
screen_res = 600, 600
scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)
#resized window width and height
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)
#cv2.WINDOW_NORMAL makes the output window resizealbe
cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
cv2.namedWindow('Window', cv2.WINDOW_NORMAL)
#resize the window according to the screen resolution
cv2.resizeWindow('Resized Window', window_width, window_height)
cv2.resizeWindow('Window', window_width, window_height)
#--------------------------------------------------------------
#img2 = img
dim = (2100,2100)
height, width, Bpp = img.shape
img_pos = img[0:(height // 2), (width // 2):width, :]
resized = cv2.resize(img_pos, dim, interpolation=cv2.INTER_AREA)
rh, rw, rb = resized.shape

N = rh
for i in range(N // 2):
    for j in range(i, N - i - 1):
        temp = resized[i, j, :]
        resized[i, j, :] = resized[(N - 1 - j), i, :]
        resized[(N - 1 - j), i, :] = resized[(N - 1 - i), (N - 1 - j), :]
        resized[(N - 1 - i), (N - 1 - j), :] = resized[j, (N - 1 - i), :]
        resized[j, (N - 1 - i), :] = temp
height2, width2, Bpp2 = img_pos.shape
dim2= (width2,height2)
img_resize = cv2.resize(resized, dim2, interpolation=cv2.INTER_AREA)
img[0:(height // 2), (width // 2):width, :] = img_resize


while(True):
    cv2.imshow("Resized Window", img2)
    cv2.imshow("Window", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#cv2.imwrite('out3.png', img)