import numpy as np 
import imageio
from PIL import Image

# Names of the .bmp sample files
fileNames = [   'gun.bmp', 
                'palm.bmp']

#bmp import dict
bmp = {}

#Import the bmps
for loc in fileNames:
    bmp[loc] = np.array(imageio.imread(loc))