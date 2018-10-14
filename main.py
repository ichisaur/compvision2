import numpy as np 
import imageio
from PIL import Image
from dilation import dilate
from erosion import erode

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

#Test line to sanity check['gun.bmp']
Image.fromarray(dilated['gun.bmp']).show()

eroded = {}
for key in dilated:
    eroded[key] = erode(dilated[key], se)

Image.fromarray(eroded['gun.bmp']).show()