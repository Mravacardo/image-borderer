import cv2
import numpy as np

img=cv2.imread("Box.png", 0)
cv2.imshow("Box.png", img)

borderedImage = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT, value = 1)

cv2.imshow("Bordered Image", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
