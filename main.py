import cv2
import numpy as np
import matplotlib.pyplot as plt
from uploader import ImageUploader

# Color is strange because OpenCV us BGR for color and matplotlib uses RGB
# Need to convert to RGB before plot with matplotlib

# img = cv2.imread("john.png")
img = ImageUploader("john.png").img
print(img)
RGB_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.subplots(nrows=1, ncols=1), plt.imshow(RGB_image)
# plt.show()

# probably want to generate the figsize based off of pic dimensions
plt.figure(figsize=(5, 6)), plt.imshow(RGB_image)
# use this to turn off axis
plt.axis('off')
plt.show()
