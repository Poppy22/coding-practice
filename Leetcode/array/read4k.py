def read4k(file):
	n = 4
	if len(file) < 4:
		n = len(file)
	result = file[:n]
	del file[:n]
	return result

def getnk(buff, n):
	result = buff[:n]
	del buff[:n]
	return result

def read(buff, file, n):
	if len(buff) >= n:
		return getnk(buff, n)

	count = len(buff)
	while count < n:
		buff.extend(read4k(file))
		count += 4

	return getnk(buff, n)


def main():
	file = list("123456789abcdefghijklmnopqrstuvwxyz")
	buff = []
	print(read(buff, file, 2))
	print(read(buff, file, 4))
	print(read(buff, file, 10))
	print(read(buff, file, 3))
	print(buff)
	print(file)

if __name__ == "__main__":
	main()