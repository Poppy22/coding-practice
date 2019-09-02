def check_replacement(string1, string2):
	# they have the same size so only one character
	# should be different
	different_char = False
	for i in range(len(string1)):
		if string1[i] != string2[i]:
			if different_char:
				# found two different
				return False

			# found one different
			different_char = True

	return True

def insert_once(string1, string2):
	# check if we can insert one element in string1
	# to make it equal to string2

	n = len(string2)
	did_insert = False
	i1, i2 = 0, 0
	while i2 < n:
		if string1[i1] != string2[i2]:
			if did_insert:
				return False

			did_insert = True
			i2 += 1
		else:
			i1 += 1
			i2 += 1

	return True

def is_one_edit_away(string1, string2):
	if len(string1) == len(string2):
		return check_replacement(string1, string2)
	elif len(string1) - 1 == len(string2):
		return insert_once(string1, string2)
	elif len(string2) - 1 == len(string1):
		return insert_once(string2, string1)
	return False

def main():
	string1 = input()
	string2 = input()
	print(is_one_edit_away(string1, string2))

if __name__ == "__main__":
	main()