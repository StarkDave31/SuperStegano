import cv2
import numpy as np

image1 = cv2.imread('001.jpg')

img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)


cv2.imshow('Binary Threshold', thresh1)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
