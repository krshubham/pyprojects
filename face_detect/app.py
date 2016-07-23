#All the software dependencies
try:
	import numpy as np
	import cv2
except ImportError:
	print("Error in importing the dependencies")


img = cv2.imread('obama.jpg',0)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
