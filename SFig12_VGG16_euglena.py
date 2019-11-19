# -*- coding: utf-8 -*-
import os
import keras
from keras.models import Model
from keras.callbacks import EarlyStopping
import numpy as np
from PIL import Image
import pandas
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import datetime

#%% Set the output file location
run_data = datetime.datetime.now().strftime("%Y_%m_%d")
result_path=r"SFig12_{}/".format(run_data)
if not os.path.exists(result_path):
    os.makedirs(result_path)
    
#%% Read Traget Folders' Path
labels=['N-','N+']
base_path = r'.\Euglena'

file_list_Nplus = []
file_list_Nminus = []
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".tif"):
            filename = os.path.join(root, file)
            file_size = os.path.getsize(filename)
            category_name = os.path.basename(root)
            if category_name == labels[0]:
                file_list_Nminus.append(filename)

            else :
                file_list_Nplus.append(filename)


#%% Read Image Files (*.tif)
nplus_img_list=[]
nminus_img_list=[]
read_number = 2500

for file in file_list_Nplus[:read_number]:
    im = Image.open(file)
    imarray = np.array(im)
    nplus_img_list.append(imarray)
nplus_img_array = np.asarray(nplus_img_list)
nplus_img_label = np.ones(nplus_img_array.shape[0])*0

for file in file_list_Nminus[:read_number]:
    im = Image.open(file)
    imarray = np.array(im)
    nminus_img_list.append(imarray)
nminus_img_array = np.asarray(nminus_img_list)
nminus_img_label = np.ones(nminus_img_array.shape[0])*1

#%% Combine two class

img_arr   = np.concatenate((nminus_img_array, nplus_img_array), axis = 0)
img_label = np.concatenate((nminus_img_label, nplus_img_label), axis = 0) 
img_label = keras.utils.to_categorical(img_label, num_classes = 2)

#%% Shuffle and seperate data

import random
temp = list(zip(img_arr, img_label))
random.shuffle(temp)
img_arr, img_label = zip(*temp)
img_arr=np.asarray(img_arr)
img_label=np.asarray(img_label)
del temp

from sklearn.model_selection import train_test_split

train_data, test_data, train_label, test_label = train_test_split(img_arr, img_label, test_size=0.2)


#%% VGG 16 only for classification

batch_size = 64
size = np.shape(train_data)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD
# Generate model
model = Sequential()
# input: 190x190 images with 3 channels -> (190, 190, 3) tensors.
# this applies 32 convolution filters of size 3x3 each.
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(size[1],size[2],size[3]),padding='same',name='block1_conv2_1'))
model.add(Conv2D(64, (3, 3), activation='relu',padding='same',name='block1_conv2_2'))
model.add(MaxPooling2D(pool_size=(2, 2),name='block1_MaxPooling'))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), activation='relu',padding='same',name='block2_conv2_1'))
model.add(Conv2D(128, (3, 3), activation='relu',padding='same',name='block2_conv2_2'))
model.add(MaxPooling2D(pool_size=(2, 2),name='block2_MaxPooling'))
model.add(Dropout(0.25))

model.add(Conv2D(256, (3, 3), activation='relu',padding='same',name='block3_conv2_1'))
model.add(Conv2D(256, (3, 3), activation='relu',padding='same',name='block3_conv2_2'))
model.add(Conv2D(256, (3, 3), activation='relu',padding='same',name='block3_conv2_3'))
model.add(MaxPooling2D(pool_size=(2, 2),name='block3_MaxPooling'))
model.add(Dropout(0.25))

model.add(Conv2D(512, (3, 3), activation='relu',padding='same',name='block4_conv2_1'))
model.add(Conv2D(512, (3, 3), activation='relu',padding='same',name='block4_conv2_2'))
model.add(Conv2D(512, (3, 3), activation='relu',padding='same',name='block4_conv2_3'))
model.add(MaxPooling2D(pool_size=(2, 2),name='block4_MaxPooling'))
model.add(Dropout(0.25))

model.add(Conv2D(512, (3, 3), activation='relu',padding='same',name='block5_conv2_1'))
model.add(Conv2D(512, (3, 3), activation='relu',padding='same',name='block5_conv2_2'))
model.add(Conv2D(512, (3, 3), activation='relu',padding='same',name='block5_conv2_3'))
model.add(MaxPooling2D(pool_size=(2, 2),name='block5_MaxPooling'))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(4096, activation='relu',name='final_output_1'))
model.add(Dropout(0.5))
model.add(Dense(4096, activation='relu',name='final_output_2'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax',name='class_output'))



sgd = SGD(lr=0.0008, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])


EStop = EarlyStopping(monitor='val_accuracy', min_delta=0, 
                      patience=3, verbose=1, mode='auto')
#%% Start Traning Model
history = model.fit(train_data, train_label, batch_size=32, epochs=30, validation_split=0.20,callbacks=[EStop])
#%%
model.save('{}Euglena_model.h5'.format(result_path)) 
#%% Save the Training History
import collections
historysavepath = result_path
if not os.path.exists(historysavepath):
    os.makedirs(historysavepath)
hist = history.history
# Count the number of epoch
for key, val in hist.items():
    numepo = len(np.asarray(val))
    break
hist = collections.OrderedDict(hist)
pandas.DataFrame(hist).to_excel(historysavepath  + 'Euglena_VGG16_training_history.xlsx', index=False)

#%% tSNE Down Diemention

intermediate_layer_model = Model(inputs=model.input,
                                 outputs=model.get_layer('final_output_2').output)
intermediate_output = intermediate_layer_model.predict(
        test_data, batch_size=batch_size, verbose=1)
Y = TSNE(n_components=2, init='random', random_state=0, perplexity=30, 
         verbose=1).fit_transform(intermediate_output.reshape(intermediate_output.shape[0],-1))

layer_output_label = np.argmax(test_label, axis=1)
df = pandas.DataFrame(dict(x=Y[:,0], y=Y[:,1], label=layer_output_label))
groups = df.groupby('label')

#%% Plot tSNE
fig, ax = plt.subplots()

ax.margins(0.05)  # Optional, just adds 5% padding to the autoscaling
for label, group in groups:
    name = labels[label]
    point,=ax.plot(group.x, group.y, marker='o', linestyle='', ms=5, label=name, alpha=0.8)


plt.title('t-SNE Scattering Plot')
ax.legend()
plt.savefig("{}Euglena_tSNE.png".format(result_path))
#%% Save tSNE Result
import pandas as pd

writer = pd.ExcelWriter('{}SFig12_Euglena_VGG16_tSNE_Result.xlsx'.format(result_path))
df.to_excel(writer,'t-SNE Result',float_format='%.2f') 
writer.save()
