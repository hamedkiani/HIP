import numpy as np
import os
import cv2
import sys, getopt

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
        return self

    def binarize(self, threshold = 128):
        if self.image.ndim == 3:
            self.rgb_to_gray()
        self.image[self.image >= threshold] = 255
        self.image[self.image < threshold] = 0
        return self

    def resize(self, new_size = None, ratio=(.1,.2), interpolation = cv2.INTER_AREA, use_ratio = False):

        if self.image is not None:
            if use_ratio:
                tmp_size = (int(ratio[0]*self.image.shape[0]), int(ratio[1]*self.image.shape[1]))
            else:
                tmp_size = new_size
        if tmp_size is not None:
            self.image = cv2.resize(self.image, tmp_size, interpolation=interpolation)
        return self

#     second pahse

    def crop(self, crop_size, extended_border=False):
        # crop_size = [top, left, height, width]
        crop_size[0] = max(0, crop_size[0])
        crop_size[0] = min(self.image.shape[0] - 1, crop_size[0])

        crop_size[1] = max(0, crop_size[1])
        crop_size[1] = min(self.image.shape[1] - 1, crop_size[1])

        if (crop_size[0] + crop_size[2] > self.image.shape[0]):
            crop_size[2] = self.image.shape[0] - crop_size[0]

        if (crop_size[1] + crop_size[3] > self.image.shape[1]):
            crop_size[3] = self.image.shape[1] - crop_size[1]
        self.image = self.image[crop_size[0]:crop_size[0]+crop_size[2], crop_size[1]:crop_size[1]+crop_size[3]]
        return self

    def flip(self, mode = 0):
#         mode 0 (horizontal), 1(vertical), -1 (both)
        if mode not in set([0, 1, -1]):
            print("the mode must be either horizontal = 0, vertical = 1, both = -1")
            return self
        self.image = cv2.flip(self.image, mode)
        return self

    def rotate(self, degree=0, rotate_center=None):
        row, col = self.image.shape[0], self.image.shape[1]
        if rotate_center is None:
            center = tuple(np.array([row, col]) / 2)
        else:
            center = tuple(rotate_center)
        rot_mat = cv2.getRotationMatrix2D(center, degree, 1.0)
        self.image = cv2.warpAffine(self.image, rot_mat, (col, row))
        return self

    def zero_padd(self, padd_size=[10, 0, 30, 30]):
        # padd_size=[left, right, top, bottom]

        left_zeros = np.ones((self.image.shape[0], padd_size[0], 3), np.uint8)
        self.image = np.concatenate((left_zeros, self.image), axis=1)

        right_zeros = np.ones((self.image.shape[0], padd_size[1], 3), np.uint8)
        self.image = np.concatenate((self.image, right_zeros), axis=1)

        top_zeros = np.ones((padd_size[2], self.image.shape[1], 3), np.uint8)
        self.image = np.concatenate((top_zeros, self.image), axis=0)

        bottom_zeros = np.ones((padd_size[3], self.image.shape[1], 3), np.uint8)
        self.image = np.concatenate((self.image, bottom_zeros), axis=0)
        return self

    def noisy(self, noise = "salt&pepper"):

        if noise == "salt&pepper":
            salt_rate = 0.5
            pepper_rate = 1. - salt_rate
            amount = 0.01

            num_salt = np.ceil(amount * self.image.size * salt_rate)
            num_pepper = np.ceil(amount * self.image.size * pepper_rate)
            coords = [np.random.randint(0, i - 1, int(num_salt))
                      for i in self.image.shape]
            coords_p = [np.random.randint(0, i - 1, int(num_pepper))
                      for i in self.image.shape]
            if self.image.ndim == 3:
                self.image[coords[0], coords[1],:] = (255, 255, 255)
                self.image[coords_p[0], coords_p[1], :] = (0, 0, 0)
            else:
                self.image[coords] = 255
                self.image[coords_p] = 0
            return self


# more noise types will be added!

