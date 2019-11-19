# -*- coding: utf-8 -*-
"""
This program is to merge two TIFF files into one.
"""

import os
import numpy as np
from PIL import Image
from scipy.misc import imsave
#%% Set the RAW data type

raw_cell = "Euglena" # "Whitecell" or "Euglena"
raw_cell_type = "N-"  # in Whitecell are "lymphocyte" and "neutrophyl", in Euglena are "N+" and "N-" 
#%% Set the output file location

save_path=r"./generated/{}/{}/".format(raw_cell, raw_cell_type)
if not os.path.exists(save_path):
    os.makedirs(save_path)
#%% Make the filename list
    
labels=['ch1','ch2']
base_path = r'./{}/{}'.format(raw_cell, raw_cell_type)

file_list_ch1 = []
file_list_ch2 = []
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".TIFF"):
            filename = os.path.join(root, file)
            file_size = os.path.getsize(filename)
            category_name = os.path.basename(root)
            if labels[0] in filename:
                file_list_ch1.append(filename)
            if labels[1] in filename:
                file_list_ch2.append(filename)
#%%Generate and save
image_number = 100  # generate 100 images you can use len(file_list_ch1) to generate all

for index in range(0,image_number):
    
    #Read Ch1 Image as Red layer in the Image
    filename_CH1=file_list_ch1[index]#Put the file path here
    im = Image.open(filename_CH1)
    imarray = np.array(im)
    imarray_ch1 = imarray
    if int(np.max(imarray)) == 100:   # to skip some checking image
        continue
    #Read CH2 Image as Green layer in the Image
    filename_CH2=file_list_ch2[index]#Put the file path here
    im = Image.open(filename_CH2)
    imarray = np.array(im)
    imarray_ch2 = imarray
    if int(np.max(imarray)) == 100:  # to skip some checking image
        continue
    #Create RGB Array
    if raw_cell == "Whitecell":
        rgbArray = np.zeros((78,88,3), 'uint16')   #Adjust the image array size
        rgbArray[..., 0] = imarray_ch1
        rgbArray[..., 1] = imarray_ch2
    if raw_cell == "Euglena":
        rgbArray = np.zeros((240,128,3), 'uint16')   #Adjust the image array size
        rgbArray[..., 0] = imarray_ch2
        rgbArray[..., 1] = imarray_ch1


    
    #Save File
    imsave(r'{}Image_{}.tif'.format(save_path,index),rgbArray)


