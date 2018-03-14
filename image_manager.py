import cv2
import matplotlib.pyplot as plt
from color_converter import ColorConverter


class ImageManager:

    def __init__(self):
        self.img = None

    def upload(self, url):
        self.img = cv2.imread(url)
        return self.img

    def img(self):
        return self.img

    def display_image(self, figsize, cmap=None):
        plt.figure(figsize=figsize)
        plt.imshow(self.img, cmap=cmap)

    def make_grayscale(self):
        self.img = ColorConverter(self.img).make_grayscale()
