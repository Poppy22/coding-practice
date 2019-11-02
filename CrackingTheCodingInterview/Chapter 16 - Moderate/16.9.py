# Implement -, *, / using just +

def negate(a):
	neg_a = 0
	new_sign = -1
	if a < 0:
		new_sign = 1
	value = new_sign

	while a != 0:
		neg_a += value
		a += value
		value += value

		# reset the delta value
		if new_sign == -1 and a + value < 0:
			value = new_sign

		if new_sign == 1 and a + value > 0:
			value = new_sign

	return neg_a


def difference(a, b):
	return a + negate(b)


def multiply(a, b):
	if a == 0 or b == 0:
		return 0

	result = 0
	if a < 0:
		a = negate(a)
		if b < 0:
			b = negate(b)
			sign = 1
		else:
			sign = -1
	else:
		if b < 0:
			b = negate(b)
			sign = -1
		else:
			sign = 1

	if a > b:
		a, b = b, a

	# a smaller than b
	for i in range(a):
		result += b

	if sign == -1:
		return negate(result)
	return result

def divide(a, b):
	# Integer division, result is an integer
	# a / b = x => a = b * x

	# I want to find the largest x such that b * x <= a

	if b == 0:
		return None
	if a == 0:
		return 0

	if a < 0:
		a = negate(a)
		if b < 0:
			b = negate(b)
			sign = 1
		else:
			sign = -1
	else:
		if b < 0:
			b = negate(b)
			sign = -1
		else:
			sign = 1
		
	x = 0
	prev_x = 0
	while multiply(b, x) <= a:
		prev_x = x
		x += 1

	if sign == -1:
		return negate(prev_x)
	return prev_x

def main():
	a = int(input())
	b = int(input())
	print(a, ' - ', b, ' = ', difference(a, b))
	print(a, ' * ', b, ' = ', multiply(a, b))
	print(a, ' / ', b, ' = ', divide(a, b))


if __name__ == "__main__":
	main()