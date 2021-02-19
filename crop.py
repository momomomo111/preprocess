import numpy as np
import cv2
import glob

for name in glob.glob('./orig/*'):
    img = cv2.imread(name)

    print(img.shape)

    # 任意のサイズに切り取り（Cut to desired size）
    result = img[550:-550, 550:-550]

    cv2.imwrite('./add/' + name[7:-4] + 'crop.jpg', result)