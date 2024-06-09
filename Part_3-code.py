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

# Convert the image to grayscale
grey_image = np.zeros((height, width))

for x in range(height):
    for y in range(width):
        red, green, blue = myImage[x, y][:3]
        grey = 0.299 * red + 0.587 * green + 0.114 * blue
        grey_image[x, y] = grey

# Define the threshold for edge detection
threshold = 0.01  # Adjust accorindgly

# Initialize an array to store the edge-detected image
edge_image = np.ones((height, width)) * 255

# Apply the basic line detection algorithm
for x in range(height - 1): 
    for y in range(width - 1):
        if abs(grey_image[x, y] - grey_image[x + 1, y]) > threshold and abs(grey_image[x, y] - grey_image[x, y + 1]) > threshold:
            edge_image[x, y] = 0  # Mark as edge

# Convert the edge-detected image to RGB format
edge_image_rgb = np.zeros((height, width, 3))

for x in range(height):
    for y in range(width):
        edge_image_rgb[x, y] = [edge_image[x, y], edge_image[x, y], edge_image[x, y]]

# Display the edge-detected image in RGB format
plt.imshow(edge_image_rgb)
plt.show()
