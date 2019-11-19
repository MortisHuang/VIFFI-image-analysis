-----Last Update Time: 2019/11/18 -----

Test Environment : Win 10 Version 1909
GPU：Nvidia GTX-1080 Ti (Not necessary but highly recommended)
CPU：Inten i7-8700K

Python Version : 3.6
Specific Libraries used in these code:
Tensorflow Version : 2.0.0  (1.x should be fine)
Keras Version : 2.3.1
Pandas Version : 0.24.2
Open-CV Version : 4.1.0
Scipy Version : 1.2.1
sklearn Version : 0.21.2

Environment Tool : Anaconda 3 (Highly Recommended!!)

This project is covered under the MIT License.
--------------------------------------------
There're 6 folders and 6 .py files in the .zip file.

(Please do not change the paths of Euglena and Whitecell folders!)

Euglena
	-N- 3000 tif images
	-N+ 3000 tif images
Whitecell
	-lymphocyte 4000 tif images
	-neutrophyl 4000 tif images

Fig4_2019_xx_xx
Fig5_2019_xx_xx
SFig11_2019_xx_xx
SFig12_2019_xx_xx

--------------------------------------------
Installation Guide：

Step 1. Unzip the .zip file in the same folder.

Step 2. Make sure you already install all the library you saw above and in the import session of the code.

Step 3. Make sure the codes, "Euglena" folder and "Whitecell" folder are in the same path. (this is the default data path in the code)

Step 4. Run the code, each code will automatically generate the subfolder for you.

Step 5. Check the subfolder and the files in it.

--------------------------------------------
Typical Install time：

For a non-python computer：1.5 hours 

For a python-ready computer：less than 15 minutes

--------------------------------------------
Demo and Instructions for use

You don't need to change any parameter in the codes, just make sure the codes, "Euglena" folder and "Whitecell" folder are in the same path.

Expected run time on a GPU support environment for all the codes is less than 30 minutes.

============================================
Fig4b_Whitecell_Area_Ratio.py

Expected output: Fig4_20xx_xx_xx / Fig4b_Area_Ratio.xlsx

============================================
Fig4c_VGG16_whitecell.py

Expected output: Fig4_20xx_xx_xx / Fig4c_Whitecell_tSNE.png, Fig4c_Whitecell_VGG16_tSNE_Result.xlsx, Whitecell_VGG16_training_history.xlsx and a .h5 model file.

============================================
Fig5b_lipid_droplets_area.py

Expected output: Fig5_20xx_xx_xx / Fig_5_b_Lipid_Drpolet_Area.xlsx

============================================
Fig5c_Number_of_lipid_droplets.py

Expected output: Fig5_20xx_xx_xx / Fig5_c_Number_of_lipid_droplets.xlsx

============================================
SFig11_Whitecell_Cell_Area.py

Expected output: SFig11_20xx_xx_xx / SFig11_35_CellArea.xlsx

============================================
SFig12_VGG16_euglena.py

Expected output: SFig12_20xx_xx_xx / Euglena_tSNE.png, Euglena_VGG16_training_history.xlsx, SFig12_Euglena_VGG16_tSNE_Result.xlsx and a .h5 model file.

--------------------------------------------
Instructions for use your data

These codes were written for 2 classes and the images are TIFF format. If you want to use your data, follow the steps below:

Step 1: Make the right folder structure.

It should be like:

Cell
    -cell_type_a
	-image_0001.png
	-image_0002.png
	...
    -cell_type_b
	-image_0001.png
	-image_0002.png
	...

Step 2: Replace the data path and the class name.


In the codes whose name start from Fig4, SFig11 and SFig12:

labels=['neutrophyl','lymphocyte']   ----->   labels=['cell_type_a','cell_type_b']

base_path = r'.\Whitecell'   ----->   base_path = r'G:\Data\Cell'   


In the codes whose name start from Fig5:

entry1=r'.\Euglena\N-'   ----->   entry1=r'G:\Data\Cell\cell_type_a'
entry2=r'.\Euglena\N+'   ----->   entry2=r'G:\Data\Cell\cell_type_b'


Step 3: Change the data format.


In the codes whose name start from Fig4, SFig11 and SFig12:

if file.endswith(".tif"):   ----->   if file.endswith(".png"):


In the codes whose name start from Fig5:

fnamelist1 = glob.glob(os.path.join(entry1, '*.tif'))   ----->   fnamelist1 = glob.glob(os.path.join(entry1, '*.png'))
fnamelist2 = glob.glob(os.path.join(entry2, '*.tif'))   ----->   fnamelist2 = glob.glob(os.path.join(entry2, '*.png'))

--------------------------------------------
Restrictions on the file format 

For VGG16 classification codes, you can use any type of image data, but the recommened shape of the image is better less than ( 250 x 250 ).

Otherwise you will need a lot of time and RAM for training the model.

**Make sure all the images in the folder are in the same shape.

For other codes, the main logic is to use the first two layers of the image to do the image processing.

normal RGB image:
Layer 1 -R (red color)
Layer 2 -G (green color)
Layer 3 -B (blue color)

demo image:
Whitecell image (8 bit):
Layer 1 - cytoplasm
Layer 2 - nucleus
Layer 3 - not used (abandon)

Euglena image (8 bit):
Layer 1 - chlorophyll
Layer 2 - lipids
Layer 3 - not used (abandon)

Make sure your information are in the right layer before you start the processing.

--------------------------------------------
License:

This project is covered under the MIT License.