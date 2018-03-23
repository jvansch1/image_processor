import cv2
from invalid_input_error import InvalidInputError
import numpy


class ColorConverter:
    def __init__(self, img):
        # passed in img should already be a valid image file
        if type(img) != numpy.ndarray:
            raise InvalidInputError("Not a valid image input")
        self.img = img

    def to_RGB(self):
        return cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

    def to_grayscale(self):
        return cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def grayscale_to_RGB(self):
        return cv2.cvtColor(self.img, cv2.COLOR_GRAY2RGB)

    def get_reds(self):
        return self.img.item(10, 10, 2)

    def set_reds(self):
        self.img.itemset((10, 10, 2), 100)
        return self.img
