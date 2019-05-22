import numpy as np
from matplotlib import pyplot as plt
import nibabel 
from utils import *


seg_file_path = "./data/Brats18_2013_10_1_seg.nii.gz"

seg = load_img(seg_file_path)
seg = color_code_segmentation(seg)
# seg = min_max_normalize(seg)
seg_slice = seg[55]
# seg_stacked = np.stack((seg_slice,seg_slice, seg_slice), axis = 2)

seg_min = np.min(seg)
print("Min value : ", seg_min)
seg_max = np.max(seg)
print("max value : ", seg_max)

plt.imshow(seg_slice, cmap = 'gray')
plt.show()
