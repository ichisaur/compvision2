import numpy as np

def erode(bitmap, strucEl):

    offset = len(strucEl)//2

    working = np.zeros(bitmap.shape)

    for x in range(offset, len(bitmap)-offset):
        for y in range(offset, len(bitmap[0])-offset):
            test = True
            for xx in range(len(strucEl)):
                for yy in range(len(strucEl)):
                    if (bitmap[xx-offset+x][yy-offset+y] == 0) & (strucEl[xx][yy] == 255):
                        test = False

            if test == True:
                working[x][y] = 255

    return working
