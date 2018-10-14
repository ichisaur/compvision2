import numpy as np
from erosion import erode



def boundary(bitmap, strucEl):
    working = erode(bitmap, strucEl)

    working = np.subtract(bitmap, working)

    return working