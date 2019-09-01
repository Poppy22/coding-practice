def zero_lines(matrix, lines, N, M):
	for i in range(N):
		if lines[i]:
			for j in range(M):
				matrix[i][j] = 0

def zero_columns(matrix, columns, N, M):
	for j in range(M):
		if columns[j]:
			for i in range(N):
				matrix[i][j] = 0

def search_for_zeroes(matrix, N, M):
	lines = [False] * N
	columns = [False] * M

	for i in range(N):
		for j in range(M):
			if matrix[i][j] == 0:
				lines[i] = True
				columns[j] = True

	return lines, columns

def print_matrix(matrix):
	for line in matrix:
		for e in line:
			print(e, end = " ")
		print()

def main():
	matrix = [[1, 2, 0], [4, 6, 5], [7, 8, 9], [0, 11, 12]]
	N = len(matrix) # number of lines
	M = len(matrix[0]) # number of columns

	print_matrix(matrix)
	
	lines, columns = search_for_zeroes(matrix, N, M)
	print(lines)
	print(columns)
	zero_lines(matrix, lines, N, M)
	zero_columns(matrix, columns, N, M)

	print_matrix(matrix)


if __name__ == "__main__":
	main()