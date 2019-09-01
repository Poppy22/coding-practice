def get_rotations(string):
	result = string
	for i in range(1, len(string)):
		first_half = string[:i]
		second_half = string[i:]
		result += (second_half + first_half)

	return result

def main():
	s1 = "waterbottle"
	s2 = "erbottlewat"

	if len(s1) != len(s2):
		print(False)
		return
		
	rotation_string = get_rotations(s1)
	print(s2 in rotation_string)

if __name__ == "__main__":
	main()