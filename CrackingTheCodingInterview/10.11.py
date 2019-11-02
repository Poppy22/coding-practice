def get_index_of_maximum(array, left, middle, right):
	if array[left] >= array[middle] and array[left] >= array[right]:
		return left

	if array[middle] >= array[left] and array[middle] >= array[right]:
		return middle

	return right

def swap_middle(array, left,  middle, right):
	new_middle = get_index_of_maximum(array, left, middle, right)
	if new_middle == left:
		# swap array[left] with array[middle]
		array[left], array[middle] = array[middle], array[left]

	if new_middle == right:
		# swap array[right] with array[middle]
		array[right], array[middle] = array[middle], array[right]

def compute_array(array):
	if len(array) <= 2:
		return array
	left, middle, right = 0, 1, 2
	while right < len(array):
		swap_middle(array, left, middle, right)

		left += 2
		middle += 2
		right += 2

	if len(array) % 2 == 0:
		swap_middle(array, len(array) - 3, len(array) - 2, len(array) - 1)

	return array

def main():
	array = [13, 24, 72, 55, 17, 8, 63, 1]
	print(compute_array(array))

if __name__ == "__main__":
	main()



import operator
s = sorted(s, key = operator.itemgetter(1, 2))

