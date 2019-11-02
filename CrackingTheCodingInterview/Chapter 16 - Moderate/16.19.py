pond = [[0,2,1,0], [0,1,0,1], [1,1,0,1], [0,1,0,1]]

def compute_ponds_sizes_helper(line, column, current_size):
	if line < 0 or line >= len(pond):
		return current_size

	if column < 0 or column >= len(pond):
		return current_size

	if pond[line][column] == 0:
		current_size += 1
		pond[line][column] = -1
	else:
		return current_size

	# up, down, left, right, up-left, up-right, down-left, down-right
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
	for d in directions:
		current_size = compute_ponds_sizes_helper(line + d[0], column + d[1], current_size)

	return current_size


def compute_ponds_sizes():
	pond_sizes = []

	for i in range(len(pond)):
		for j in range(len(pond)):
			if pond[i][j] == 0:
				print(i, j)
				size = compute_ponds_sizes_helper(i, j, 0)
				pond_sizes.append(size)
	return pond_sizes


def main():
	print(compute_ponds_sizes())
	print(pond)


if __name__ == "__main__":
	main()
