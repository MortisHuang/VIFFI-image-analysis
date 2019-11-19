# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:30:55 2019

@author: Mortis Huang
"""

# import the necessary packages
import cv2
from PIL import Image
import numpy as np
import datetime
import os
import pandas as pd

#%% Set the output file location
run_data = datetime.datetime.now().strftime("%Y_%m_%d")
result_path=r"./Fig4_{}/".format(run_data)
if not os.path.exists(result_path):
    os.makedirs(result_path)
    
#%% Read Traget Folders' Path
labels=['neutrophyl','lymphocyte']
#base_path = r'E:\DeepLearning\Mikami\Generate\White Cell'
base_path = r'./Whitecell'

file_list_lym = []
file_list_neu = []
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".tif"):
            filename = os.path.join(root, file)
            file_size = os.path.getsize(filename)
            category_name = os.path.basename(root)
            if category_name == labels[0]:
                file_list_neu.append(filename)

            else :
                file_list_lym.append(filename)

#%% Read image files and put in a list
data_number = 2500

label='lymphocyte'   #  'lymphocyte' or 'neutrophyl'
data_of_lym_name = []
data_of_lym_nucleus = []
data_of_lym_box = []
data_of_lym_ratio = []
for i, filename in enumerate(file_list_lym[:data_number]):
    threadhold=140       
    im = Image.open(filename)
    imarray = np.array(im)
    imarray[imarray<threadhold]=0
    image = imarray[:,:,1]
    
    # Find the enclosing box and draw it 
    x, y, w, h = cv2.boundingRect(imarray[:,:,1])
    cv2.rectangle(imarray, (x,y), (x+w,y+h), (0,0,255), 1)
    imarray[:,:,0]=0
    
    # Save the resluts as png files
#    cv2.imwrite('{}\Result_of_{}_{}_all.png'.format(label,label,i), imarray)
#    cv2.imwrite('{}\Result_of_{}_{}_box.png'.format(label,label,i), imarray[y-5:y+h+5,x-5:x+w+5,:])
    
    # Calculate the enclosing box area
    box_area=w*h
    
    if box_area ==0:
        box_area = 1
    # Read the image file again (for insure) and calculate the nucleus area 
    im = Image.open(filename)
    imarray = np.array(im)
    imarray[imarray<threadhold]=0
    image = imarray[:,:,1]
    cell_area=np.count_nonzero(imarray[y-5:y+h+5,x-5:x+w+5,1])   
    
    # Temp. the resluts

    data_of_lym_nucleus.append(cell_area)
    data_of_lym_box.append(box_area)
    data_of_lym_ratio.append(cell_area/box_area)

    
label='neutrophyl'   #  'lymphocyte' or 'neutrophyl'
data_of_neu_name = []
data_of_neu_nucleus = []
data_of_neu_box = []
data_of_neu_ratio =[]
for i, filename in enumerate(file_list_neu[:data_number]):
    threadhold=140       
    im = Image.open(filename)
    imarray = np.array(im)
    imarray[imarray<threadhold]=0
    image = imarray[:,:,1]
    
    # Find the enclosing box and draw it 
    x, y, w, h = cv2.boundingRect(imarray[:,:,1])
    cv2.rectangle(imarray, (x,y), (x+w,y+h), (0,0,255), 1)
    imarray[:,:,0]=0
    
    # Save the resluts as png files
#    cv2.imwrite('{}\Result_of_{}_{}_all.png'.format(label,label,i), imarray)
#    cv2.imwrite('{}\Result_of_{}_{}_box.png'.format(label,label,i), imarray[y-5:y+h+5,x-5:x+w+5,:])
    
    # Calculate the enclosing box area
    box_area=w*h
    
    if box_area ==0:
        box_area =1
    # Read the image file again (for insure) and calculate the nucleus area 
    im = Image.open(filename)
    imarray = np.array(im)
    imarray[imarray<threadhold]=0
    image = imarray[:,:,1]
    cell_area=np.count_nonzero(imarray[y-5:y+h+5,x-5:x+w+5,1])   
    
    # Temp. the resluts

    data_of_neu_nucleus.append(cell_area)
    data_of_neu_box.append(box_area)
    data_of_neu_ratio.append(cell_area/box_area)

#%% Remove zeros 
data_of_lym_ratio=np.asarray(data_of_lym_ratio)
data_of_neu_ratio=np.asarray(data_of_neu_ratio)
data_of_lym_ratio=data_of_lym_ratio[data_of_lym_ratio>0]
data_of_neu_ratio=data_of_neu_ratio[data_of_neu_ratio>0]

#%% Save the Results
data = {'lymphocyte':data_of_lym_ratio}
df1 = pd.DataFrame(data)
data = {'neutrophyl':data_of_neu_ratio}
df2 = pd.DataFrame(data)
df_all = pd.concat([df1,df2], ignore_index=True, axis=1)
df_all.columns = ["lymphocyte","neutrophyl"] 
writer = pd.ExcelWriter('{}Fig4b_Area_Ratio.xlsx'.format(result_path))
df_all.to_excel(writer,'Sheet 1',float_format='%.2f') 
writer.save()
