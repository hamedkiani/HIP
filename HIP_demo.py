from HIP import *

path = "/home/hamed/MyOffice/pythonPRojects/HIP/lena.png"

test = HIP(path=path)
print(test.height())
print(test.width())
print(test.channel())
test.imshow()
temp = test.get_image()
cv2.imshow("copy", temp)

test.resize(use_ratio=True)
test.imshow("resized")
print(test.height())
print(test.width())

test.rgb_to_gray()
test.imshow("gray")

test.binarize(threshold=128)
test.imshow("binary")
test.save_to(path="/home/hamed/MyOffice/pythonPRojects/HIP/" + "lena2.png")
cv2.waitKey(0)
