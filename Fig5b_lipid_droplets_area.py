# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:35:15 2019

@author: Mortis
"""
import numpy as np
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters
import glob
import os
from PIL import Image
import pandas as pd
import copy
import datetime

#%% Set the output file location
run_data = datetime.datetime.now().strftime("%Y_%m_%d")
result_path=r"./Fig5_{}/".format(run_data)
if not os.path.exists(result_path):
    os.makedirs(result_path)
#%%
numberofdata=12000
Area_of_Nm=np.zeros(numberofdata)
Area_of_Np=np.zeros(numberofdata)
Area_of_All=np.zeros((numberofdata,2))
Peaks_of_Nm=np.zeros(numberofdata)
Peaks_of_Np=np.zeros(numberofdata)
entry1=r'.\Euglena\N-'
entry2=r'.\Euglena\N+'
fnamelist1 = glob.glob(os.path.join(entry1, '*.tif'))
fnamelist2 = glob.glob(os.path.join(entry2, '*.tif'))
r=3
index=0
for filename in fnamelist1[:numberofdata]:
    im = Image.open(filename)
    imarray = np.array(im)
    imarray[imarray<5]=0
    image = imarray[:,:,1]
    neighborhood_size = 10
    threshold = 25
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
        new_imarray=imarray
        total_area=0
        for i in range(0,len(x)):
            y2=int(y[i])
            x2=int(x[i])
            #Find Area
            averg=np.mean(new_imarray[y2-r:y2+r,x2-r:x2+r,1])
            #Mark the Area
            new_imarray[y2-r:y2+r,x2-r:x2+r,1][new_imarray[y2-r:y2+r,x2-r:x2+r,1]>=averg]=255
            cut = copy.deepcopy(new_imarray[y2-r:y2+r,x2-r:x2+r,1])
            cut[cut<255]=0
    #        print('Peak {} : X:{} Y:{} Area:{}'.format(i,x[i],y[i],np.sum(cut==255)))
            total_area+=np.sum(cut==255)
    else:
        total_area=1
#    print('Total_Area:{}'.format(total_area))
    Area_of_Nm[index]=total_area
    Area_of_All[index,0]=total_area
    index+=1
    
index=0
for filename in fnamelist2[:numberofdata]:
    im = Image.open(filename)
    imarray = np.array(im)
    imarray[imarray<5]=0
    image = imarray[:,:,1]
    neighborhood_size = 10
    threshold = 25
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
        new_imarray=imarray
        total_area=0
        for i in range(0,len(x)):
            y2=int(y[i])
            x2=int(x[i])
            #Find Area
            averg=np.mean(new_imarray[y2-r:y2+r,x2-r:x2+r,1])
            #Mark the Area
            new_imarray[y2-r:y2+r,x2-r:x2+r,1][new_imarray[y2-r:y2+r,x2-r:x2+r,1]>=averg]=255
            cut = copy.deepcopy(new_imarray[y2-r:y2+r,x2-r:x2+r,1])
            cut[cut<255]=0
    #        print('Peak {} : X:{} Y:{} Area:{}'.format(i,x[i],y[i],np.sum(cut==255)))
            total_area+=np.sum(cut==255)
            
    else:
        total_area=1
#    print('Total_Area:{}'.format(total_area))
    Area_of_Np[index]=total_area
    Area_of_All[index,1]=total_area
    index+=1
#%%
Area_of_All_df = pd.DataFrame(Area_of_All)
Area_of_All_df.columns = ['N-','N+']
writer = pd.ExcelWriter('{}Fig_5b_Lipid_Drpolet_Area.xlsx'.format(result_path))
Area_of_All_df.to_excel(writer,'Intensity',float_format='%.5f') 
writer.save()