# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:19:41 2019

@author: Mortis
"""
import numpy as np
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters
import glob
import os
from PIL import Image
import pandas as pd
import datetime

#%% Set the output file location
run_data = datetime.datetime.now().strftime("%Y_%m_%d")
result_path=r"./Fig5_{}/".format(run_data)
if not os.path.exists(result_path):
    os.makedirs(result_path)

#%%
numberofdata=12000
Peaks_of_Nm=np.zeros(numberofdata)
Peaks_of_Np=np.zeros(numberofdata)
Peaks_of_All=np.zeros((numberofdata,2))
entry1=r'.\Euglena\N-'
entry2=r'.\Euglena\N+'
fnamelist1 = glob.glob(os.path.join(entry1, '*.tif'))
fnamelist2 = glob.glob(os.path.join(entry2, '*.tif'))

index=0
for filename in fnamelist1[:numberofdata]:
    im = Image.open(filename)
    imarray = np.array(im)
    imarray[imarray<5]=0
    image = imarray[:,:,1]
    neighborhood_size = 10
    threshold = 15
    data = imarray[:,:,1]
    data_max = filters.maximum_filter(data, neighborhood_size)
    maxima = (data == data_max)
    data_min = filters.minimum_filter(data, neighborhood_size)
    diff = ((data_max - data_min) > threshold)
    maxima[diff == 0] = 0
    labeled, num_objects = ndimage.label(maxima)
    slices = ndimage.find_objects(labeled)
    x, y = [], []
    for dy,dx in slices:
        x_center = (dx.start + dx.stop - 1)/2
        x.append(x_center)
        y_center = (dy.start + dy.stop - 1)/2    
        y.append(y_center)
    if len(x)>0:   
        Peaks_of_Nm[index]=len(x)
        Peaks_of_All[index,0]=len(x)

    else:
        Peaks_of_Nm[index]=0
        Peaks_of_All[index,0]=0
    index=index+1

index=0
for filename in fnamelist2[:numberofdata]:
    im = Image.open(filename)
    imarray = np.array(im)
    imarray[imarray<5]=0
    image = imarray[:,:,1]
    neighborhood_size = 10
    threshold = 15
    data = imarray[:,:,1]
    data_max = filters.maximum_filter(data, neighborhood_size)
    maxima = (data == data_max)
    data_min = filters.minimum_filter(data, neighborhood_size)
    diff = ((data_max - data_min) > threshold)
    maxima[diff == 0] = 0
    labeled, num_objects = ndimage.label(maxima)
    slices = ndimage.find_objects(labeled)
    x, y = [], []
    for dy,dx in slices:
        x_center = (dx.start + dx.stop - 1)/2
        x.append(x_center)
        y_center = (dy.start + dy.stop - 1)/2    
        y.append(y_center)
    if len(x)>0:   
        Peaks_of_Np[index]=len(x)
        Peaks_of_All[index,1]=len(x)
    else:
        Peaks_of_Np[index]=0
        Peaks_of_All[index,1]=0
    index=index+1
    

#%%Save to Excel
Peaks_of_All_df = pd.DataFrame(Peaks_of_All)
Peaks_of_All_df.columns = ['N-','N+']
writer = pd.ExcelWriter('{}Fig5c_Number_of_lipid_droplets.xlsx'.format(result_path))
Peaks_of_All_df.to_excel(writer,'Sheet 1',float_format='%.5f') 
writer.save()
