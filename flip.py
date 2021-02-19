import numpy as np
import cv2
import glob

for name in glob.glob('./orig/*'):
    img = cv2.imread(name)

    print(img.shape)

    # 上下反転（upside down）
    img_flip_ud = cv2.flip(img, 0)
    cv2.imwrite('./add/' + name[7:-4] + '_ud.jpg', img_flip_ud)

    # 左右反転（left and right reversals）
    img_flip_lr = cv2.flip(img, 1)
    cv2.imwrite('./add/' + name[7:-4] + '_lr.jpg', img_flip_lr)

    # 上下左右反転（upside down, down side up）
    img_flip_ud_lr = cv2.flip(img, -1)
    cv2.imwrite('./add/' + name[7:-4] + '_ud_lr.jpg', img_flip_ud_lr)