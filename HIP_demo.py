from HIP import *

path = "add the path to the image here, will fix it soon"

test = HIP(path=path)
print(test.height())
print(test.width())
print(test.channel())
test.imshow()
temp = test.get_image()
cv2.imshow("copy", temp)

test.zero_padd()
test.imshow("left_10_padd")



# test.rotate(-30)
# test.imshow("rotate-45")
test.flip(3)
test.imshow("flip-1")


crop_size = [40, -10, 1000, 1000]
test.resize((50,50)).crop(crop_size=crop_size)
test.imshow("cropped")
print("cropped_size. {}".format(test.image.shape))
#
# test.resize(use_ratio=True)
# test.imshow("resized")
# print(test.height())
# print(test.width())
#
# test.rgb_to_gray()
# test.imshow("gray")
#
# test.binarize(threshold=128)
# test.imshow("binary")
# test.save_to(path="/home/hamed/MyOffice/pythonPRojects/HIP/" + "lena2.png")
cv2.waitKey(0)
