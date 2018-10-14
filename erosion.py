import numpy as np

# erode takes in bitmap and SE
# Loops through bitmap to apply SE
# Returns eroded image in array form
def erode(bitmap, strucEl):

    # Calculates offset for use later in the image
    offset = len(strucEl)//2

    working = np.zeros(bitmap.shape)

    # Only loops through bitmap an offset away from the edges, to avoid edge cases
    # SE will always not be true at the edges anyways due to not enough true pixels for a pattern match
    for x in range(offset, len(bitmap)-offset):
        for y in range(offset, len(bitmap[0])-offset):

            # (re)Set the test condition to be true
            test = True
            for xx in range(len(strucEl)):
                for yy in range(len(strucEl)):
                    # checks if all pixels surrounding in the SE are on, and if the SE correspondign pixel is on as well. 
                    # If not, set test to false
                    if (bitmap[xx-offset+x][yy-offset+y] == 0) & (strucEl[xx][yy] == 255):
                        test = False

            # only if test is true do you set the working pixel to be on
            if test == True:
                working[x][y] = 255

    return working # Return the working array
