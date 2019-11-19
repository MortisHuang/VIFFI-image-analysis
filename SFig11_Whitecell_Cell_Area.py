# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:30:55 2019

@author: Mortis Huang
"""

# import the necessary packages
from PIL import Image
import numpy as np
import datetime
import os
import pandas as pd
#%% Set the output file location
run_data = datetime.datetime.now().strftime("%Y_%m_%d")
result_path=r"SFig11_{}/".format(run_data)
if not os.path.exists(result_path):
    os.makedirs(result_path)
    
#%% Read Traget Folders' Path
labels=['neutrophyl','lymphocyte']
#base_path = r'E:\DeepLearning\Mikami\Generate\White Cell'
base_path = r'.\Whitecell'

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
#%% Sort the file list
#file_list_lym = sorted(file_list_lym, key=lambda x:int(x.split('_')[-1].split('.')[0]))
#files_name_lym = sorted(files, key=lambda x:int(x.split('_')[-1].split('.')[0]))
#%% Read image files and put in a list
data_number = 11000

label='lymphocyte'   #  'lymphocyte' or 'neutrophyl'
data_of_lym_cell = []
for i, filename in enumerate(file_list_lym[:data_number]):
    
    # Read the image file again (for insure) and calculate the nucleus area 
    im = Image.open(filename)
    imarray = np.array(im)
    threadhold = np.max(imarray)*0.35
    imarray[imarray<threadhold]=0
    image = imarray[:,:,0]
    cell_area=np.count_nonzero(imarray)   
    
    # Temp. the resluts

    data_of_lym_cell.append(cell_area)

label='neutrophyl'   #  'lymphocyte' or 'neutrophyl'
data_of_neu_name = []
data_of_neu_cell = []


for i, filename in enumerate(file_list_neu[:data_number]):     
    # Read the image file again (for insure) and calculate the nucleus area 
    im = Image.open(filename)
    imarray = np.array(im)
    threadhold = np.max(imarray)*0.35
    imarray[imarray<threadhold]=0
    image = imarray[:,:,0]
    cell_area=np.count_nonzero(imarray)   
    
    # Temp. the resluts
    data_of_neu_cell.append(cell_area)


#%% Remove zeros 
data_of_lym_cell=np.asarray(data_of_lym_cell)
data_of_neu_cell=np.asarray(data_of_neu_cell)
data_of_lym_cell=data_of_lym_cell[data_of_lym_cell>0]
data_of_neu_cell=data_of_neu_cell[data_of_neu_cell>0]

#%% Save the Results
data = {'lymphocyte':data_of_lym_cell}
df1 = pd.DataFrame(data)
data = {'neutrophyl':data_of_neu_cell}
df2 = pd.DataFrame(data)
df_all = pd.concat([df1,df2], ignore_index=True, axis=1)
df_all.columns = ["Lymphocyte","Neutrophyl"] 
writer = pd.ExcelWriter('{}SFig11_35_CellArea.xlsx'.format(result_path))
#writer = pd.ExcelWriter('CellArea.xlsx')
df_all.to_excel(writer,'Sheet 1',float_format='%.2f') # float_format 
writer.save()
