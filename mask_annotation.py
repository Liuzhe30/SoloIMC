import cv2
import numpy as np
import os, glob  
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import shutil

def rgb2masks(background_color, mask_path, label_name):
    
    lbl_id = os.path.split(label_name)[-1].split('.')[0]
    lbl = cv2.imread(label_name, 1)
    h, w = lbl.shape[:2]
    cell_dict = {}
    idx = 0
    white_mask = np.ones((h, w, 3), dtype=np.uint8) * 255
    for i in range(h):
        for j in range(w):
            if tuple(lbl[i][j]) in cell_dict or (lbl[i][j] == background_color).all() == True:
                continue
            cell_dict[tuple(lbl[i][j])] = idx
            mask = (lbl == lbl[i][j]).all(-1)
            cell = np.where(mask[..., None], white_mask, 0)
            mask_name = mask_path + lbl_id + '_nucleus_' + str(idx) + '.png'
            cv2.imwrite(mask_name, cell)
            idx += 1

if __name__ == "__main__":
    
    I1 = cv2.imread('Data/Train/labels/000.png', 1)
    background_color = I1[0][0]        

    # test annotation
    label_dir = 'Data/Test/labels'
    label_list = glob.glob(os.path.join(label_dir, '*.png'))
    mask_path = 'Data/Test/annotations/'
    for label_name in label_list:
        rgb2masks(background_color, mask_path, label_name)
        
    # train annotation
    label_dir = 'Data/Train/labels'
    label_list = glob.glob(os.path.join(label_dir, '*.png'))
    mask_path = 'Data/Train/annotations/'
    for label_name in label_list:
        rgb2masks(background_color, mask_path, label_name)
        

    
    