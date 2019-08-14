# Solution I: one passion - O(n), O(1) space

n = int(input())
line = input().split()

# min_1 < min_2
# max_1 > max_2
min_1 = min_2 = max_1 = max_2 = int(line[0])

for number in line:
	if int(number) <= min_1:
		min_2 = min_1
		min_1 = int(number)
	elif int(number) < min_2:
		min_2 = int(number)

	if int(number) >= max_1:
		max_2 = max_1
		max_1 = int(number)
	elif int(number) > max_2:
		max_2 = int(number)

# If I delete max_1
result_1 = max_2 - min_1

# If I delete min_1
result_2 = max_1 - min_2

print(min(result_1, result_2))


###################################################################
# Solution II: (sorting) - O(nlogn) time, O(n) space
n = int(input())
line = input().split()

array = []
for number in line:
	array.append(int(number))

array.sort()

if len(array) == 1 or len(array) == 2:
	print(min(array[0], array[1]))
elif len(array) == 3:
	print(min(array[1] - array[0], array[2] - array[1]))
else:
	min_1 = array[0]
	min_2 = array[1]
	max_1 = array[n - 1]
	max_2 = array[n - 2]
	print(min(max_2 - min_1, max_1 - min_2))