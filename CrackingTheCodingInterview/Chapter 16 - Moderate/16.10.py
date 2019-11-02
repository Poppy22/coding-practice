def main():
	people = [(1, 5), (2, 5), (4, 7), (9, 10), (2, 6), (1, 10), (3, 7), (7, 8), (7, 9)]
	d = {}
	for i in range(1, 12):
		d[i] = 0

	for p in people:
		d[p[0]] += 1
		d[p[1] + 1] -= 1

	local_value = 0
	global_max = 0
	result = 0

	for key in d:
		local_value += d[key]
		if local_value > global_max:
			global_max = local_value
			result = key

	print(result)


if __name__ == "__main__":
	main()