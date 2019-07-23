import cv2
import numpy as np
import math

def median_blur(img, kernel, padding_way):

    #检查填充方式
    if padding_way == 'zero':
        pass
    elif padding_way == 'replica':
        pass
    else:
        raise AttributeError("Error Padding Mode! 'replica' & 'zero' ONLY!!")


    #图像填充
    pdrow = (kernel.shape[0] - 1) // 2
    pdcol = (kernel.shape[1] - 1) // 2

    if padding_way == 'replica':
        img_pad = np.pad(img, ((pdrow, pdrow), (pdcol, pdcol)), 'edge')

    if padding_way == 'zero':
        img_pad = np.pad(img, ((pdrow, pdrow), (pdcol, pdcol)),
                             mode='constant', constant_values=0)

    #空白矩阵
    result = np.zeros_like(img)

    # 滤波
    for j in range(img.shape[1]):
        for i in range(img.shape[0]):
            temp = img_pad[i:i + kernel.shape[0], j:j + kernel.shape[1]]
            result[i][j] = np.median(temp)

    return result



kernel = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
img = cv2.imread('D:\lenna.jpg')
cv2.imshow('origin',img)
img_median = median_blur(img,kernel,'zero')
cv2.imshow('hello',img_median)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()