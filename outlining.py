from erosion import erode
from numpy import np

def boundary(bitmap, strucEl):
    working = erode(bitmap, strucEl)

    working = np.subtract(bitmap, working)

    return working