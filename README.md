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
Specific Libraries used in these code:
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
*Step 1. Unzip the .zip file in the same folder.

*Step 2. Make sure you already install all the library you saw above and in the import session of the code.

*Step 3. Make sure the codes, "Euglena" folder and "Whitecell" folder are in the same path. (this is the default data path in the code)

*Step 4. Run the code, each code will automatically generate the subfolder for you.

*Step 5. Check the subfolder and the files in it.

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
