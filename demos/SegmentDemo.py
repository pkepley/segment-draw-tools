import sys
import numpy as np
from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.feature import canny

# Quick and dirty, assume we run file from this directory and point to
# code in folder root. Should fix this. Probably won't.
sys.path.append("../")
import ImageSegmenter as iss

# Where do the images live?
img_dir = "../imgs"

# Convert image to black-and-white and detect edges
img = imread(img_dir + "/gwpe4.png")
img2 = rgb2gray(img)
img2 = canny(img2, sigma = 2.0)

# Convert edges into connected components
segs = iss.ImageSegmenter(img2)
segs.constructComps()

# Plot original image and color-coded segments side-by-side
fig, ax = plt.subplots(ncols=2, sharex = True, sharey=True,
                       figsize=(7, 7))

ax[0].imshow(img, cmap=plt.cm.gray)
ax[1].imshow(img2 * np.reshape(segs.qu.id, img2.shape), 
             interpolation = 'nearest')

for a in ax:
    a.axis('off')
plt.tight_layout()
plt.show()


