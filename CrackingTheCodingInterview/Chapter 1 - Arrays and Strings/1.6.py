def compress(string):
	result = ''
	i = 0
	while i < len(string) - 1:
		count = 1
		character = string[i]
		while i + 1 < len(string) and character == string[i + 1]:
			count += 1
			i += 1
		result += (character + str(count))
		i += 1

	if i < len(string):
		result += (string[i] + '1')
	print(result)

	if len(result) < len(string):
		return result
	return string # unchanged

def main():
	string = "aaabbcccccddddd"
	print(compress(string))

if __name__ == "__main__":
	main()