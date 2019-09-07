def main():
	N = int(input("Number of nodes\n"))
	M = int(input("Number of edges\n"))
	edges = []
	road_matrix = [[0] * (N + 1) for _ in range(N + 1)]

	while M > 0:
		edge = input()
		x, y = int(edge.split()[0]), int(edge.split()[1])
		edges.append((x, y))
		road_matrix[x][y] = 1
		M -= 1

	for e in edges:
		x, y = e[0], e[1]
		for y_neighbour in road_matrix[y]:
			if y_neighbour == 1:
				road_matrix[x][y_neighbour] = 1

	for line in road_matrix:
		print(line)


if __name__ == "__main__":
	main()