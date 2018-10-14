import numpy as np
from erosion import erode


# Boundary returns an outline of the given image 
# Takes in bitmap and structuring element SE
# Applies an erosion using the SE and subtracts from original to return boundary
def boundary(bitmap, strucEl):

    # Erode the image, then subtract the erode from the original image
    working = erode(bitmap, strucEl)
    working = np.subtract(bitmap, working)

    return working