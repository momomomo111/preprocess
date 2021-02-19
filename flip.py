import numpy as np
import cv2
import glob

for name in glob.glob('./orig/*'):
    img = cv2.imread(name)

    print(img.shape)
    # (225, 400, 3)

    img_flip_ud = cv2.flip(img, 0)
    cv2.imwrite('./add/' + name[7:-4] + '_ud.jpg', img_flip_ud)
    # True

    img_flip_lr = cv2.flip(img, 1)
    cv2.imwrite('./add/' + name[7:-4] + '_lr.jpg', img_flip_lr)
    # True

    img_flip_ud_lr = cv2.flip(img, -1)
    cv2.imwrite('./add/' + name[7:-4] + '_ud_lr.jpg', img_flip_ud_lr)
    # True