import sys
from HIP import *

# path to image
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = "./lena.png"
print("path is {}".format(path))
test = HIP(path=path)
test.imshow()
test.rgb_to_gray()
test.imshow("gray")

dx, dy = test.gradient(visualize=True)
cv2.imshow("dx", dx)
cv2.imshow("dy", dy)

mag = test.magnitude()
cv2.imshow("mag", mag)

ed = test.edge()
cv2.imshow("edge", ed)


# test.add_noise(noise="gauss")
# test.imshow("noisy")
# temp = test.get_image()
# cv2.imshow("copy", temp)

cv2.waitKey(0)