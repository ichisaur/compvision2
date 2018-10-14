import numpy as np

# Dilate takes in bitmap and SE
# Loops through bitmap to apply SE
# Returns dilated image in array form
def dilate(bitmap, strucEl):

	# Calculates the offset factor needed based of SE array size
	offset = len(strucEl)//2

	# Create an array that is bigger than what we need, padded by offset width zeros
	# This avoids edge cases
	bitmapCopy = np.zeros(np.add(bitmap.shape,[len(strucEl)-1,len(strucEl)-1]))
	bitmapCopy[offset:bitmap.shape[0] + offset, offset:bitmap.shape[1]+offset] = bitmap

	# Create a working array of the same size
	working = np.zeros(np.add(bitmap.shape,[len(strucEl)-1,len(strucEl)-1]))

	# Loops through that padded array. Note that since the edges are always zero, an array oob error should never occur
	for x in range(len(bitmapCopy)):
		for y in range(len(bitmapCopy[0])):

				# Checks if pixel is white or not
				if bitmapCopy[x][y] == 255:

					#if it is, set all working pixels to white, if not already, for all elements in the SE
					for xx in range(len(strucEl)):
						for yy in range(len(strucEl)):
							working[xx-offset+x][yy-offset+y] = max(working[xx-offset+x][yy-offset+y],strucEl[xx][yy])

	# Grab only the portion of the working that was not padded
	working = working[offset:bitmap.shape[0]+offset, offset:bitmap.shape[1]+offset]

	return working #Return the array

                        
            

