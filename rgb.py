from PIL import Image
import numpy as np
# Open the image
img = Image.open("/home/rguktrkvaleey/dhana.jpeg")
# Convert image to a NumPy array
img_array = np.array(img)

# Reshape the array to access individual pixel values
pixel_values = img_array.reshape(-1, 3)

# Write pixel values to CSV
np.savetxt("rgb_value.csv", pixel_values, delimiter=",", fmt="%d")
