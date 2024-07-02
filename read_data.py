#### read file (only print the files' name) #####

# from one folder

import os
from os import listdir

folder_dir = "archive/BreaKHis 400X/train/benign" 

for image in os.listdir(folder_dir):
    if (image.endswith(".png")):
        print(image)

# from 2 subfolders
import os

main_path = "archive/BreaKHis 400X/train"
sub_folders = ['benign', 'malignant']

image_paths = []

for subfolder in sub_folders:
    f_path = os.path.join(main_path, subfolder)
    for image in os.listdir(f_path):
        print (image)
