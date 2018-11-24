import numpy as np
import os
import cv2

class HIP:
    def __init__(self, image=None, path=None):
        self.image = image
        self.path = path
        if os.path.isfile(path):
            image = cv2.imread(path)
            self.image = image
        else:
            print("the path {} does not exist".format(path))

    def load(self, image=None, path=None):
        self.image = image
        self.path = path
        if os.path.isfile(path):
            image = cv2.imread(path)
            self.image = image
        else:
            print("the path {} does not exist".format(path))

    def imshow(self, tag="image"):
        if self.image is not None:
            cv2.imshow(tag, self.image)
        else:
            print("the image is not loaded does not exist")


    def height(self):
        if self.image is not None:
            return self.image.shape[1]
        else:
            return 0

    def width(self):
        if self.image is not None:
            return self.image.shape[0]
        else:
            return 0

    def channel(self):
        if self.image is not None:
            if self.image.ndim == 3:
                return 3
            else:
                return 2
        else:
            return 0

    def save_to(self, path=None):
        if self.image is None:
            print("there is not image to be saved!")
            return False
        # if path is None or not os.path.isfile(path):
        #     print("the path is either None or does not exist")
        #     return False
        cv2.imwrite(path, self.image)

    def get_image(self):
        return self.image

    def rgb_to_gray(self):
        if self.image.ndim == 3:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)

    def binarize(self, threshold = 128):
        if self.image.ndim == 3:
            self.rgb_to_gray()
        self.image[self.image >= threshold] = 255
        self.image[self.image < threshold] = 0

    def resize(self, new_size = None, ratio=(.1,.2), interpolation = cv2.INTER_AREA, use_ratio = False):

        if self.image is not None:
            if use_ratio:
                tmp_size = (int(ratio[0]*self.image.shape[0]), int(ratio[1]*self.image.shape[1]))
            else:
                tmp_size = new_size
        if tmp_size is not None:
            self.image = cv2.resize(self.image, tmp_size, interpolation=interpolation)



