import numpy as np
'''
Implement a minimum edit distance algorithm and use your hand-computed
results to check your code.
'''


def sub_cost(c1, c2, cost):
	if c1 == c2:
		return 0
	return cost

# sub cost is 1
def minimum_edit_distance1(str1, str2):
	rows = len(str1)
	cols = len(str2)

	# initialize
	D = np.zeros(shape=(rows+1,cols+1)) # distance matrix

	for row in range(1, rows+1):
		D[row, 0] = row

	for col in range(1, cols+1):
			D[0, col] = col
	
	# fill matrix

	for row in range(1, rows+1):
		for col in range(1, cols+1):

			D[row, col] = min(
				D[row-1, col] + 1,
				D[row, col-1] + 1,
				D[row-1, col-1] + sub_cost(str1[row-1], str2[col-1], 1)
			)

	return int(D[rows, cols])

# sub cost is 2
def minimum_edit_distance2(str1, str2):
	rows = len(str1)
	cols = len(str2)

	# initialize
	D = np.zeros(shape=(rows+1,cols+1)) # distance matrix

	for row in range(1, rows+1):
		D[row, 0] = row

	for col in range(1, cols+1):
			D[0, col] = col
	
	# fill matrix

	for row in range(1, rows+1):
		for col in range(1, cols+1):

			D[row, col] = min(
				D[row-1, col] + 1,
				D[row, col-1] + 1,
				D[row-1, col-1] + sub_cost(str1[row-1], str2[col-1], 2)
			)

	return int(D[rows, cols])
