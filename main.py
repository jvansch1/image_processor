import cv2
import numpy as np
import matplotlib.pyplot as plt
from image_manager import ImageManager
from color_converter import ColorConverter

# Color is strange because OpenCV us BGR for color and matplotlib uses RGB
# Need to convert to RGB before plot with matplotlib

# img = cv2.imread("john.png")
manager = ImageManager()
img = manager.upload("john.png")
print(type(img))
RGB_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(img[0])
# print(RGB_image[0])

# def make_grayscale(img):
#     return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



# plt.subplots(nrows=1, ncols=1), plt.imshow(RGB_image)
# plt.show()

# probably want to generate the figsize based off of pic dimensions
# plt.figure(figsize=(5, 6)), plt.imshow(RGB_image)

#grey image(must specify a gray color map in imshow)

manager.make_grayscale()
manager.display_image(figsize=(5, 6), cmap='gray')

# plt.figure(figsize=(5, 6)), plt.imshow(grayscale_image, cmap="gray")


# use this to turn off axis
plt.axis('off')
plt.show()
