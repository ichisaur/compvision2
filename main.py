import numpy as np 
import imageio
from PIL import Image
from dilation import dilate
from erosion import erode
from closing import closing
from opening import opening
from outlining import boundary

# Names of the .bmp sample files
fileNames = [   'gun.bmp', 
                'palm.bmp']

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

dilated = {}
for key in bmp:
    dilated[key] = dilate(bmp[key], se5)
    #sanity output line
    #TODO change to save line
    Image.fromarray(dilated[key]).convert('L').save(key[:-4] + '_dl5.bmp')

#Test line to sanity check['gun.bmp']


eroded = {}
for key in bmp:
    eroded[key] = erode(bmp[key], se3)
    #sanity output line
    #TODO change to save line
    Image.fromarray(eroded[key]).convert('L').save(key[:-4] + '_er3.bmp')

opened = {}
for key in bmp:
    opened[key] = opening(bmp[key], se3)
    #TODO change to save line
    Image.fromarray(opened[key]).convert('L').save(key[:-4] + '_op3.bmp')

closed = {}
for key in bmp:
    closed[key] = closing(bmp[key], se5)
    #TODO change to save line
    Image.fromarray(closed[key]).convert('L').save(key[:-4] + '_cl5.bmp')

outlined = {}
for key in dilated:
    outlined[key] = boundary(dilated[key], se3)
    Image.fromarray(outlined[key]).convert('L').save(key[:-4] + '_bd3.bmp')


# To arbitrarily process the image

arb = {}
for key in bmp:
    arb[key] = dilate(bmp[key], se3)
    arb[key] = closing(arb[key],se5)
    arb[key] = opening(arb[key],se5)
    arb[key] = erode(arb[key], se3)
    Image.fromarray(arb[key]).convert('L').save(key[:-4] + '_arb.bmp')
    