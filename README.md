# HIP - Hamed's Image Processing Library

## V1.0.1: December 2017

## Overview

HIP contains basic image processing functionality, including *load*, *imshow*, *saveas*, and *color conversion*.

HIP also supports *image resizing*, *rotation*, *cropping*, *edge detection*, *gradient magnitude*, *affine transforms* and adding different types of noise. These basic operations are used broadly in many image processing and computer vision pre-processing applications.

## Tutorial

### The following functions are implemented in HIP

1. load() that loads an image using path to image or image values

        load(self, image=None, path=None)

2. reset() that resets current instance with the original image which was used to construct HIP
        
        reset(self)
      
3. imshow() that visualizes current image in HIP

        imshow(self, tag="image")
        
4. height() that returns the height of the image

        height(self)
       
5. width() that returns the width of the image

        height(self)
        
6. channle() that returns the number of dimention of image (2D, 3D, etc)

        channel(self)
        
7. save_as() that saves current image in HIP in a given path

        save_as(self, path=None)
        
8. get_image() that returns current image

        get_image(self)
        
9. rgb_to_gray() converts the RGB image to gray

        rgb_to_gray(self)
        
10. binarize() that converts the image to a binary image given a threshold

        binarize(self, threshold=128):
        
11. resize() that resizes the image given a resize ratio or another size(h,w)

        resize(self, new_size=None, ratio=(0.5, 0.5), interpolation=cv2.INTER_AREA, use_ratio=False)
        
12. crop() that crops a region of the image given a crop window size

        crop(self, crop_size)
        
13. flip() that flips the image horizantaly, vertically or both

        flip(self, mode=0)
        
14. rotate() performs 2D rotation respect to a center and/or a rotation angle

        rotate(self, degree=0, rotate_center=None)
        
15. zero_padd that adds zeros to the border of the image, given the padd size(left, right, top, bottom)

        zero_padd(self, padd_size=[10, 10, 30, 30])
        
16. add_noise() for adding *salt and pepper* and *gauss* noise to the image

        add_noise(self, noise="salt&pepper")
        
17. gradient() that returns dx and dy as gradient in x and y directions

        gradient(self)
        
18. magnitude() that computes the magnitude of a the image

        magnitude(self)
        
19. edge() computes the *Sobel* edge of the image

        magnitude(self)
        
20. get_path() that returns the path of the image

        get_path(self)
        