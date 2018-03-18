import cv2
import matplotlib.pyplot as plt
from color_converter import ColorConverter


class ImageManager:

    def __init__(self):
        self.img = None

    def upload(self, url):
        self.img = cv2.imread(url)
        return self.img

    def size(self):
        return self.img.size

    def return_img(self):
        return self.img

    def create_color_converter(self):
        return ColorConverter(self.img)

    def display_image(self, figsize, cmap=None):
        plt.figure(figsize=figsize)
        plt.imshow(self.img, cmap=cmap)

    def convert(self, convert):
        self.img = getattr(self.create_color_converter(), convert)()

    def get_reds(self):
        return self.create_color_converter().get_reds()

    def set_reds(self):
        self.create_color_converter().set_reds()
        return self.img

    def set_to_black(self):
        for idx, row in enumerate(self.img):
            for idx2, pixel in enumerate(row):
                self.img[idx][idx2] = 0

    def set_to_white(self):
        for idx, row in enumerate(self.img):
            for idx2, pixel in enumerate(row):
                self.img[idx][idx2] = 255

        return self.img
