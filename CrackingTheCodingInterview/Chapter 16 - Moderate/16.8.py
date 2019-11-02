
one_digit_numbers = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
two_digit_numbers = ["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
more_digit_numbers = ["", "", "thousand", "million", "billion", "trillion"]

def split_number(n):
	number_of_chunks = 0
	chunks = []
	s = []
	while n > 999:
		number_of_chunks += 1
		s = []
		for i in range(3):
			s.append(str(n % 10))
			n = n // 10
		s.reverse()
		chunks.append(''.join(s))

	if n > 0:
		chunks.append(str(n))

	return chunks


def transform_chunk(n, number_type):
	result = []
	print(n)
	if len(n) == 3:
		if n[0] != '0':
			result.append(one_digit_numbers[int(n[0])])
			result.append('hundred')

		result.append(two_digit_numbers[int(n[1])])
		result.append(one_digit_numbers[int(n[2])])

	if len(n) == 2:
		if n[0] != '0':
			result.append(two_digit_numbers[int(n[0])])
			result.append(one_digit_numbers[int(n[1])])

	if len(n) == 1:
		result.append(one_digit_numbers[int(n[0])])
	result.append(number_type)
	return ' '.join(result)


def compute_string(n):
	chunks = split_number(n)
	spelling = []
	size = len(chunks)

	for i in range(len(chunks), -1, -1):
		number_type = more_digit_numbers[size]
		partial_number = transform_chunk(chunks[i], number_type)
		spelling.append(partial_number)
		size -= 1

	return ' '.join(spelling)


def main():
	n = int(input())
	print(compute_string(n))

if __name__ == "__main__":
	main()