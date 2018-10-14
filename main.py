import numpy as np 
import imageio
from PIL import Image
from dilation import dilate
from erosion import erode
from closing import closing
from opening import opening

# Names of the .bmp sample files
fileNames = [   'gun.bmp', 
                'palm.bmp']

#bmp import dict
bmp = {}

#Import the bmps
for loc in fileNames:
    bmp[loc] = np.array(imageio.imread(loc))

#Structuring array definition
se = np.array([[255, 255, 255],
               [255, 255 ,255],
               [255, 255, 255]])

dilated = {}
for key in bmp:
    dilated[key] = dilate(bmp[key], se)
    #sanity output line
    #TODO change to save line
    Image.fromarray(dilated[key]).show()

#Test line to sanity check['gun.bmp']


eroded = {}
for key in bmp:
    eroded[key] = erode(bmp[key], se)
    #sanity output line
    #TODO change to save line
    Image.fromarray(eroded[key]).show()

opened = {}
for key in bmp:
    opened[key] = opening(bmp[key], se)
    #TODO change to save line
    Image.fromarray(opened[key]).show()

closed = {}
for key in bmp:
    closed[key] = closing(bmp[key], se)
    #TODO change to save line
    Image.fromarray(closed[key]).show()

