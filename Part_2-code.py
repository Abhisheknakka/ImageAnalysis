import os
from datetime import datetime
print(os. getcwd())
print(datetime.now())

import matplotlib.pyplot as plt
import numpy as np

myImage = plt.imread('flower.png')

height = myImage.shape[0]
width = myImage.shape[1]

blurred_image = np.copy(myImage)
num_passes = 10  # No. of times to apply the blurring algorithm

for _ in range(num_passes):
    temp_image = np.copy(blurred_image)
    for x in range(1, height - 1):
        for y in range(1, width - 1):
            for channel in range(3):  # Iterate over R, G, B channels
                blurred_image[x, y, channel] = (
                    temp_image[x - 1, y, channel] +
                    temp_image[x + 1, y, channel] +
                    temp_image[x, y - 1, channel] +
                    temp_image[x, y + 1, channel]
                ) / 4

plt.imshow(blurred_image)
plt.show()
