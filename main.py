import numpy as np
from PIL import Image
import math

# Simulate a laser beam with a gaussian distribution
# Creates an image with dimensions `size` by `size` pixels
def create_gaussian_beam(size = 1000):
    values = np.linspace(-1, 1, size)
    image_buffer = np.zeros(shape = (size, size))
    scale = math.floor(math.log(size, 2))
    for row in range(size):
        for column in range(size):
            x = values[column]
            y = values[row]
            r = math.sqrt(x**2 + y**2)
            image_buffer[row][column] = math.e**(-scale*r**2) # Range: [0, 1]
    image = Image.fromarray(np.uint8(image_buffer * 255) , "L")
    return image

image = create_gaussian_beam()
image.show()