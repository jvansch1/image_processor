import cv2
from invalid_input_error import InvalidInputError
import numpy


class ColorConverter:
    def __init__(self, img):
        # passed in img should already be a valid image file
        if type(img) != numpy.ndarray:
            raise InvalidInputError("Not a valid image input")
        self.img = img

    def make_grayscale(self):
        return cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
