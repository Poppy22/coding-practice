def decode_string(n, encoded):
	if n <= 2:
		return encoded

	decoded = [''] * n

	# first add the middle or the two middle elements
	if n % 2 == 0:
		decoded[n // 2 - 1] = encoded[0]
		decoded[n // 2] = encoded[1]
		start = 2 # last for encoded
		left = n // 2 - 2
		right = n // 2 + 1
	else:
		decoded[n // 2] = encoded[0]
		start = 1 # last for encoded
		left = n // 2 - 1
		right = n // 2 + 1

	# there is an even number of letters left in encoded, starting from 'start'
	# I will add one of them to the left of middle, the next one to the right
	# and so on

	while start < n - 1:
		decoded[left] = encoded[start]
		decoded[right] = encoded[start + 1]
		left -= 1
		right += 1
		start += 2

	return ('').join(decoded)


n = int(input())
encoded = input()
print(decode_string(n, encoded))

