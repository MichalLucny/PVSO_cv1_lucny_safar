import matplotlib.pyplot as plt
import numpy as np
from ximea import xiapi
import cv2 


#cv2.namedWindow('XIMEA cam',cv2.WINDOW_NORMAL)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a new figure and axis
fig, ax = plt.subplots()

# Plot the data on the axis
line, = ax.plot(x, y)

# Add a title and axis labels
ax.set_title('Line Plot')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

# Display the plot
plt.show(block=False)

# Periodically redraw the plot
while True:
    # Update the data
    y = y*y
    line.set_ydata(y)
    
    # Redraw the plot
    plt.draw()
    plt.pause(1)  # Pause for 1 second


