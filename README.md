# VIFFI-image-analysis
Here are the source codes of all the image analysis methods presented in the research.

## Environment

-----Last Update Time: 2019/11/19 -----

Test Environment : Win 10 Version 1909

GPU：Nvidia GTX-1080 Ti (Not necessary but highly recommended)

CPU：Inten i7-8700K

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
Step 1. Download this project as a .zip file, unzip the .zip file in one folder.

Step 2. Make sure you already install all the libraries you saw above and those in the import session of the code.

Step 3. Make sure the codes, "Euglena" folder and "Whitecell" folder are in the same path. (this is the default data path in the code)

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

Step 4. Run the code, each code will automatically generate the subfolder for you.

Step 5. Check the subfoldesr and the results in it.

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

Expected output: 
* Fig4_20xx_xx_xx
  * [Fig4b_Area_Ratio.xlsx]
  * [Fig4c_Whitecell_tSNE.png]
  * [Fig4c_Whitecell_VGG16_tSNE_Result.xlsx]
  * [Whitecell_VGG16_training_history.xlsx]
  * .h5 model file.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
