from erosion import erode
from dilation import dilate

# Opening takes in bitmap and SE
# First erodes the bitmap using the SE and then dilates usign SE
# Returns opened bitmap
def opening(bitmap, strucEl):

    working = erode(bitmap, strucEl)
    working = dilate(working, strucEl)

    return working