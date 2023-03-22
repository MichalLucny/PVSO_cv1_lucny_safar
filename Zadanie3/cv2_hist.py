import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('flamingos.jpg')


histogram_b = cv2.calcHist([img], [0], None, [256], [0, 256])
histogram_g = cv2.calcHist([img], [1], None, [256], [0, 256])
histogram_r = cv2.calcHist([img], [2], None, [256], [0, 256])

fig, ax = plt.subplots(2,2,figsize =(10, 7))
ax[0,0].plot(histogram_r, color='r')
ax[0,1].plot(histogram_b, color='b')
ax[1,0].plot(histogram_g, color='g')



# Add a title and axis labels
ax[0,0].set_title('Histogram Red')
ax[0,0].set_xlabel('Pixel Value')
ax[0,0].set_ylabel('Number of Occurences')
 
ax[0,1].set_title('Histogram Blue')
ax[0,1].set_xlabel('Pixel Value')
ax[0,1].set_ylabel('Number of Occurences') 
 
ax[1,0].set_title('Histogram Blue')
ax[1,0].set_xlabel('Pixel Value')
ax[1,0].set_ylabel('Number of Occurences')
# Show plot
plt.show()

