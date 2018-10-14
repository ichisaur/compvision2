from dilation import dilate
from erosion import erode

# closing takes in bitmap and SE
# First dilates then erodes the bitmap using the given SE
# Returns closed bitmap
def closing(bitmap, strucEl):
    working = dilate(bitmap, strucEl)
    working = erode(working, strucEl)

    return working
