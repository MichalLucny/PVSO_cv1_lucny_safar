import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('flamingos.jpg')
red = np.array(img[:, :,  2]).flatten() 
blue = np.array(img[:, :, 0]).flatten()
green  = np.array(img[:, :,  1]).flatten() 

x = [1, 2, 3, 4, 65]
#b = np.linspace(start = 0, stop = 255, num = )


fig, ax = plt.subplots(2,2,figsize =(10, 7))
ax[0,0].hist(red, range(0,255,1), histtype='stepfilled', color='red' )
ax[0,1].hist(blue, range(0,255,1), histtype='stepfilled',color='blue')
ax[1,0].hist(green, range(0,255,1), histtype='stepfilled',color='green')
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

