import numpy as np 
import imageio
from PIL import Image

# Morphological Operator Imports
from dilation import dilate
from erosion import erode
from closing import closing
from opening import opening
from outlining import boundary

# Names of the .bmp sample files
fileNames = ['gun.bmp', 'palm.bmp']

#bmp import dict
bmp = {}

#Import the bmps
for loc in fileNames:
    bmp[loc] = np.array(imageio.imread(loc))

# Structuring array definition
# Structuring array must satisfy these requirements:
##  Same Length and Width
##  Dimensions must be odd
##  Elements must be either 255 or 0
se5 = np.array([[255, 255, 255, 255, 255],
               [255, 255 ,255, 255, 255],
               [255, 255, 255, 255, 255],
               [255, 255, 255, 255, 255],
               [255, 255, 255, 255, 255]])

se3 = np.array([[255, 255, 255],
                [255, 255, 255], 
                [255, 255, 255]])

# Dilation test run
# Iterate over all images and apply operator
dilated = {}
for key in bmp:
    dilated[key] = dilate(bmp[key], se5)
    #Save. Weird jankyness that needs a conversion to work properly
    Image.fromarray(dilated[key]).convert('L').save(key[:-4] + '_dl5.bmp')

# Repeat for erode opened and closed, using different operators
eroded = {}
for key in bmp:
    eroded[key] = erode(bmp[key], se3)
    Image.fromarray(eroded[key]).convert('L').save(key[:-4] + '_er3.bmp')

opened = {}
for key in bmp:
    opened[key] = opening(bmp[key], se3)
    Image.fromarray(opened[key]).convert('L').save(key[:-4] + '_op3.bmp')

closed = {}
for key in bmp:
    closed[key] = closing(bmp[key], se5)
    Image.fromarray(closed[key]).convert('L').save(key[:-4] + '_cl5.bmp')

# For outlined, start with the dilated image, or you wont get a good outline of anything. 
outlined = {}
for key in dilated:
    outlined[key] = boundary(dilated[key], se3)
    Image.fromarray(outlined[key]).convert('L').save(key[:-4] + '_bd3.bmp')


# To arbitrarily process the image to what I think looks best
# Dilate, then close, open, and erode the image.
arb = {}
for key in bmp:
    arb[key] = dilate(bmp[key], se3)
    arb[key] = closing(arb[key], se5)
    arb[key] = opening(arb[key], se5)
    arb[key] = erode(arb[key], se3)
    Image.fromarray(arb[key]).convert('L').save(key[:-4] + '_arb.bmp')
