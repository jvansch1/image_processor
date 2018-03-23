import cv2
import matplotlib.pyplot as plt
from color_converter import ColorConverter


class ImageManager:

    def __init__(self):
        self.img = None

    def upload(self, url):
        self.img = cv2.imread(url)
        return self.img

    def reset_image(self, numpy_image):
        self.img = numpy_image

    def size(self):
        return self.img.size

    def return_img(self):
        return self.img

    def create_color_converter(self):
        return ColorConverter(self.img)

    def convert(self, convert):
        if convert == '':
            return self.img
        else:
            return getattr(self.create_color_converter(), convert)()

    def set_to_black(self):
        for idx, row in enumerate(self.img):
            for idx2, pixel in enumerate(row):
                self.img[idx][idx2] = 0

    def set_to_white(self):
        for idx, row in enumerate(self.img):
            for idx2, pixel in enumerate(row):
                self.img[idx][idx2] = 255

        return self.img
