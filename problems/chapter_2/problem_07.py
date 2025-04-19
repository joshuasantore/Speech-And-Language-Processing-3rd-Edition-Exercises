import numpy as np
'''
Augment the minimum edit distance algorithm to output an alignment; you
will need to store pointers and add a stage to compute the backtrace.
'''

def sub_cost(c1, c2, cost):
	if c1 == c2:
		return 0
	return cost

def alignment(str1, str2):

	rows = len(str1)
	cols = len(str2)

	# one array for the edit distance, one array for the pointers
	D = np.zeros((rows+1, cols+1), dtype=int)
	P = np.zeros((rows+1, cols+1), dtype=str)

	# initialize
	for row in range(1, rows+1):
		D[row][0] = D[row-1][0] + 1
		P[row][0] = 'd'

	for col in range(1, cols+1):
		D[0][col] = D[0][col-1] + 1
		P[0][col] = 'i'

	# forward march
	for row in range(1, rows+1):
		for col in range(1, cols+1):
			minimum = min(
				D[row-1][col] + 1,
				D[row][col-1] + 1,
				D[row-1][col-1] + sub_cost(str1[row-1], str2[col-1], 2)
			)
			D[row][col] = minimum
			if minimum == D[row-1][col-1] + sub_cost(str1[row-1], str2[col-1], 2):
				P[row][col] = 's'
			elif minimum == D[row][col-1] + 1:
				P[row][col] = 'i'
			else:
				P[row][col] = 'd'
			
	# backtrace
	operations = []
	pointer = P[rows][cols]
	position = [rows, cols]
	while pointer != '':
		operations.append(str(pointer))
		match pointer:
			case 'd':
				position = [position[0]-1, position[1]]
			case 'i':
				position = [position[0], position[1]-1]
			case 's':
				position = [position[0]-1, position[1]-1]
		pointer = P[position[0]][position[1]]
	

	operations.reverse()

	# Structuring the alignment for easy printing
	align1 = []
	align2 = []
	p1 = 0
	p2 = 0
	for i in range(len(operations)):
		if operations[i] == 'd':
			align2.append('*')
			align1.append(str1[p1])
			p1 += 1
		elif operations[i] == 'i':
			align1.append("*")
			align2.append(str2[p2])
			p2 += 1
		else:
			align1.append(str1[p1])
			p1+=1
			align2.append(str2[p2])
			p2+=1

	# dont show self substitution as substitution at all
	for i in range(len(operations)):
		if operations[i] == 's' and align1[i] == align2[i]:
			operations[i] = '-'


	# output

	print(" ".join(align1))
	print(" ".join(operations))
	print(" ".join(align2))



