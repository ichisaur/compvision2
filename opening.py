#erode then dilate
from erosion import erode
from dilation import dilate


def opening(bitmap, strucEl):

    working = erode(bitmap, strucEl)
    working = dilate(working, strucEl)

    return working