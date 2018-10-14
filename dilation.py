import numpy as np

def dilate(bitmap, strucEl):

	offset = len(strucEl)//2

	bitmapCopy = np.zeros(np.add(bitmap.shape,[len(strucEl)-1,len(strucEl)-1]))
	bitmapCopy[offset:bitmap.shape[0] + offset, offset:bitmap.shape[1]+offset] = bitmap

	working = np.zeros(np.add(bitmap.shape,[len(strucEl)-1,len(strucEl)-1]))

    #TODO edge cases - 4 edges and 4 corners

	for x in range(len(bitmapCopy)):
		for y in range(len(bitmapCopy[0])):
				if bitmapCopy[x][y] == 255:

					for xx in range(len(strucEl)):
						for yy in range(len(strucEl)):
							working[xx-offset+x][yy-offset+y] = strucEl[xx][yy]

	working = working[offset:bitmap.shape[0]+offset, offset:bitmap.shape[1]+offset]

	return working

                        
            

