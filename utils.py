import numpy as np
from matplotlib import pyplot as plt
import nibabel 


COLORMAP = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]


def load_img(file_path):
    """
    Reads a nifty image volume and returns it as a numpy array.
    Output dimensions: [depth, y, x]
    """
    img = nibabel.load(file_path).get_data()
    return img.transpose(2,0,1)


def color_code_segmentation(seg_map):
    """
    Converts segmentation map to an RGB image with a unique color for each 
    label.
    """
    # Stack the segmentation map to form 3 channels.
    color_seg = np.stack((seg_map, seg_map, seg_map), axis = 3)

    labels = np.unique(seg_map)
    for i in range(len(labels)):
        color_seg[seg_map == labels[i]] = COLORMAP[i]
    
    return color_seg


def min_max_normalize(arr):
    """
    Scales all values of 'arr' to the range [0,1]
    """
    min_val = np.min(arr)
    max_val = np.max(arr)

    return (arr- min_val)/ (max_val - min_val)

