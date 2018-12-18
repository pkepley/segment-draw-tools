import sys
import numpy as np
from scipy.ndimage import imread
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.feature import canny

# Quick and dirty, assume we run file from this directory and point to
# code in folder root. Should fix this. Probably won't.
sys.path.append("../")
import RegularImageTriangulator as rit

# Where do the images live?
img_dir = "../imgs"

# Convert image to black-and-white and detect edges
img = imread(img_dir + "/gwpe4.png")

# Create a regular image triangulator
rit_obj = rit.RegularImageTriangulator(img, ncol = 50)

for cmap_name in ["Reds_r", "Greens_r", "Blues_r"]:
    fig, ax = rit_obj.plotLinTriang(cmap = cmap_name)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    fig.savefig("{}/gwpe_lin_triang_{}.png".format(img_dir, cmap_name), 
                transparent= True,
                bbox_inches='tight',
                pad_inches=0)
