import cv2
import numpy as np

#Natiahnem obrazok
img = cv2.imread('out.jpg')
dim = (2100,2100)
height, width, Bpp = img.shape
img_pos = img[0:(height // 2), (width // 2):width, :]
resized = cv2.resize(img_pos, dim, interpolation=cv2.INTER_AREA)
rh, rw, rb = resized.shape

#otocim obrazok
N = rh
for i in range(N // 2):
    for j in range(i, N - i - 1):
        temp = resized[i, j, :]
        resized[i, j, :] = resized[(N - 1 - j), i, :]
        resized[(N - 1 - j), i, :] = resized[(N - 1 - i), (N - 1 - j), :]
        resized[(N - 1 - i), (N - 1 - j), :] = resized[j, (N - 1 - i), :]
        resized[j, (N - 1 - i), :] = temp

#ulozim obrazok
height2, width2, Bpp2 = img_pos.shape
dim2= (width2,height2)
img_resize = cv2.resize(resized, dim2, interpolation=cv2.INTER_AREA)
img[0:(height // 2), (width // 2):width, :] = img_resize
cv2.imwrite('out3.png', img)