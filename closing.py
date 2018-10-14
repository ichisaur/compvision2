#Dilating then eroding

from dilation import dilate
from erosion import erode

def closing(bitmap, strucEl):
    working = dilate(bitmap, strucEl)
    working = erode(working, strucEl)

    return working
