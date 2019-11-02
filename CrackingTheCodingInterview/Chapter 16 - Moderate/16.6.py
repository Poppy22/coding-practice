import sys

def compute_difference(A, B):
	if len(A) == 0 or len(B) == 0:
		return -1

	min_diff = sys.maxsize
	i = 0
	j = 0

	while i < len(A) and j < len(B):
		diff = A[i] - B[j]
		if min_diff > diff and diff >= 0:
			min_diff = diff
		if A[i] < B[j]:
			i += 1
		else:
			j += 1

	return min_diff


def main():
	A = [1, 9, 5, 6, 12, 10]
	B = [4, 3, 100]
	A.sort()
	B.sort()
	print(compute_difference(A, B))

if __name__ == "__main__":
	main()