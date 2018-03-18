import cv2
import numpy as np
import matplotlib
# need to specify matplot lib to use "tkAgg before pyplot is imported"
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from image_manager import ImageManager
from color_converter import ColorConverter
from gui import GUI


# Color is strange because OpenCV us BGR for color and matplotlib uses RGB
# Need to convert to RGB before plot with matplotlib

manager = ImageManager()
img = manager.upload("john.png")
RGB_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gui = GUI()
# print(img[0])
# print(RGB_image[0])

# def make_grayscale(img):
#     return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# probably want to generate the figsize based off of pic dimensions
# plt.figure(figsize=(5, 6)), plt.imshow(RGB_image)

#grey image(must specify a gray color map in imshow)

# manager.make_grayscale()
manager.convert('to_grayscale')
# reds = manager.get_reds()
# manager.set_reds()
# print(reds)
# manager.display_image(figsize=(5, 6), cmap='gray')
# figure = plt.figure(figsize=(5, 6))
gui.create_canvas(manager.return_img())
gui.set_labels()
gui.create_main_loop()


# use this to turn off axis
# plt.axis('off')
# plt.show()
