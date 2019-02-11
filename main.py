import cv2
import numpy as np


def loadImage():
    img = cv2.imread("C:\\Users\\danie\\Desktop\\rectified_images\\undistorted0.jpg")
    print("22")
    cv2.imshow('Image', img)
    pressedkey = cv2.waitKey(0)

    # Wait for ESC key to exit
    if pressedkey == 27:
        cv2.destroyAllWindows()

loadImage()