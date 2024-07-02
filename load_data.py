### load the data (program read the image) ###

# load only one image

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
 
img = mpimg.imread('archive/BreaKHis 400X/train/benign/SOB_B_A-14-22549AB-400-002.png')

plt.imshow(img)
plt.axis('off')
plt.show()

############################################################################
# load all the images in a folder
import os
from os import listdir
import matplotlib.image as mpimg

folder_dir = "archive/BreaKHis 400X/train/benign"

for image in os.listdir(folder_dir):
    if (image.endswith(".png")):
        img_path = os.path.join(folder_dir, image)
        img = mpimg.imread(img_path)
        print(image) 
