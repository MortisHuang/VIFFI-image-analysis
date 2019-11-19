# VIFFI-image-analysis
Here are the source codes of all the image analysis methods presented in the research.

## Environment

-----Last Update Time: 2019/11/19 -----

Test Environment : Win 10 Version 1909

GPU：Nvidia GTX-1080 Ti (Not necessary but highly recommended)

CPU：Inten i7-8700K

RAM：32GB

Environment Tool : [Anaconda 3](https://www.anaconda.com/) 
```bash
Python Version : 3.6

Tensorflow Version : 2.0.0  (1.x should be fine)
Keras Version : 2.3.1
Pandas Version : 0.24.2
Open-CV Version : 4.1.0
Scipy Version : 1.2.1
sklearn Version : 0.21.2
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the libraries mentioned above.

```bash
pip install libiary_name
```
or
```bash
pip3 install libiary_name
```
### Step 1. Download this project as a .zip file, unzip the .zip file in one folder.

### Step 2. Make sure you already install all the libraries you saw above and those in the import session of the code.

### Step 3. Make sure the codes, "Euglena" folder and "Whitecell" folder are in the same path. (this is the default data path in the code)

It should be like this:

 * Source Codes (.py files)
 * Euglena
   * N-
     * Image_0.tif
     * Image_1.tif
     ...
   * N+
     * Image_0.tif
     * Image_1.tif
     ...
 * Whitecell
   * lymphocyte
     * Image_0.tif
     * Image_1.tif
     ...
   * neutrophyl
     * Image_0.tif
     * Image_1.tif
     ...
 * README.md

### Step 4. Run the code, each code will automatically generate the subfolder for you.

### Step 5. Check the subfoldesr and the results in it.

## Typical Install time：

For a non-python computer：1.5 hours 

For a python-ready computer：less than 15 minutes

## Demo

You don't need to change any parameter in the codes, just make sure the codes, "Euglena" folder and "Whitecell" folder are in the same path.

Expected run time on a GPU support environment for all the codes is less than 30 minutes.

### Fig4b_Whitecell_Area_Ratio.py

Expected output: 
* Fig4_20xx_xx_xx
  * [Fig4b_Area_Ratio.xlsx]

### Fig4c_VGG16_whitecell.py
![t-SNE result](https://github.com/MortisHuang/VIFFI-image-analysis/blob/master/Fig4_2019_11_14/Fig4c_Whitecell_tSNE.png)

(t-SNE has a cost function that is not convex, i.e. with different initializations we can get different results.)

Expected output: 
* Fig4_20xx_xx_xx
  * [Fig4c_Whitecell_tSNE.png]
  * [Fig4c_Whitecell_VGG16_tSNE_Result.xlsx]
  * [Whitecell_VGG16_training_history.xlsx]
  * .h5 model file.
### Fig5b_lipid_droplets_area.py

Expected output: 
* Fig5_20xx_xx_xx  
  * [Fig_5_b_Lipid_Drpolet_Area.xlsx]
  
### Fig5c_Number_of_lipid_droplets.py

Expected output: 
* Fig5_20xx_xx_xx  
  * [Fig5_c_Number_of_lipid_droplets.xlsx]
  
### SFig11_Whitecell_Cell_Area.py

Expected output: 
* SFig11_20xx_xx_xx  
  * [SFig11_35_CellArea.xlsx]
  
### SFig12_VGG16_euglena.py
![t-SNE result](https://github.com/MortisHuang/VIFFI-image-analysis/blob/master/SFig12_2019_11_14/Euglena_tSNE.png)

(t-SNE has a cost function that is not convex, i.e. with different initializations we can get different results.)

Expected output:
* SFig12_20xx_xx_xx
  * [Euglena_tSNE.png]
  * [SFig12_Euglena_VGG16_tSNE_Result.xlsx]
  * [Euglena_VGG16_training_history.xlsx]
  * .h5 model file.

## How to use your own data

These codes were written for 2 classes and the images are TIFF format. If you want to use your data, follow the steps below:

### Step 1: Make the right folder structure.

It should be like:

 * Cell
   * cell_type_a
     * Image_0.png
     * Image_1.png
     ...
   * cell_type_b
     * Image_0.png
     * Image_1.png
     ...
     
### Step 2: Replace the data path and the class name.

#### In the codes whose name start from Fig4, SFig11 and SFig12:
from
```python
labels=['neutrophyl','lymphocyte']
base_path = r'.\Whitecell'
```
to
```python
labels=['cell_type_a','cell_type_b']
base_path = r'G:\Data\Cell'
```
#### In the codes whose name start from Fig5:
from
```python
entry1=r'.\Euglena\N-'
entry2=r'.\Euglena\N+'
```
to
```python
entry1=r'G:\Data\Cell\cell_type_a'
entry2=r'G:\Data\Cell\cell_type_b'
```
### Step 3: Change the data format

#### In the codes whose name start from Fig4, SFig11 and SFig12:
from
```python
if file.endswith(".tif"):   
```
to
```python
if file.endswith(".png"):
```

#### In the codes whose name start from Fig5:
from
```python
fnamelist1 = glob.glob(os.path.join(entry1, '*.tif'))
fnamelist2 = glob.glob(os.path.join(entry2, '*.tif'))
```
to
```python
fnamelist1 = glob.glob(os.path.join(entry1, '*.png'))
fnamelist2 = glob.glob(os.path.join(entry2, '*.png'))
```

## Restrictions on the file format 
For VGG16 classification codes, you can use any type of image data, but the recommened shape of the image is better less than ( 250 x 250 ).

Otherwise you will need a lot of time and RAM for training the model.

**Make sure all the images in the folder are in the same shape.

For other codes, the main logic is to use the first two layers of the image to do the image processing.

normal RGB image:
* Layer 1 -R (red color)
* Layer 2 -G (green color)
* Layer 3 -B (blue color)

demo image:
Whitecell image (8 bit):
* Layer 1 - cytoplasm
* Layer 2 - nucleus
* Layer 3 - not used (abandon)

Euglena image (8 bit):
* Layer 1 - chlorophyll
* Layer 2 - lipids
* Layer 3 - not used (abandon)

Make sure your information are in the right layer before you start the processing.

## License
[MIT](https://choosealicense.com/licenses/mit/)
