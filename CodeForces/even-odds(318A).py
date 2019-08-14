def build_kth_even_number(k, n):
	if n % 2 == 1:
		k -= 1
	return 2 * k

def build_kth_odd_number(k):
	return 2 * k - 1

line = input().split()
n = int(line[0])
k = int(line[1])

if k <= n // 2 or (n % 2 == 1 and k <= n // 2 + 1):
	print(build_kth_odd_number(k))
else:
	print(build_kth_even_number(k - n // 2, n))

