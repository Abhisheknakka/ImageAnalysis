import os
from datetime import datetime
print(os. getcwd())
print(datetime.now())

import matplotlib.pyplot as plt
import numpy as np

# Read the image
myImage = plt.imread('flower.png')

# Get the height and width of the image
height = myImage.shape[0]
width = myImage.shape[1]

# Initialize an array to store the grayscale image
grey_image = np.zeros((height, width, 3))

# Convert the image to grayscale
for x in range(height):
    for y in range(width):
        red, green, blue = myImage[x, y][:3]
        grey = 0.299 * red + 0.587 * green + 0.114 * blue
        grey_image[x, y] = [grey, grey, grey]

# Display the grayscale image
plt.imshow(grey_image)
plt.show()
