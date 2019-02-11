import cv2
import numpy as np

coord = []

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
       global coord
       coord.append(np.array((x ,y)))



def loadImage():
    img = cv2.imread("C:\\Users\\danie\\Desktop\\rectified_images\\undistorted0.jpg")
    cv2.imshow('Image', img)
    pressedkey = cv2.waitKey(0)

    # Wait for ESC key to exit
    if pressedkey == 27:
        cv2.destroyAllWindows()
        global coord
        dist = np.linalg.norm(coord[0]-coord[1])
        print(dist)


cv2.namedWindow('Image')
cv2.setMouseCallback('Image', onMouse)
loadImage()

