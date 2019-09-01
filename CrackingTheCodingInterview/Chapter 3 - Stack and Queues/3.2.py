class Stack():
	def __init__(self):
		self.stack = []
		self.min_stack = []

	def push(self, x):
		self.stack.append(x)
		if self.min_stack == [] or x < self.min_stack[len(self.min_stack) - 1]:
			self.min_stack.append(x)

	def pop(self):
		n = len(self.stack) - 1
		x = self.stack[n]
		del self.stack[n]
		if self.min_stack[len(self.min_stack) - 1] == x:
			self.min_stack.pop()
		return x

	def top(self):
		if self.stack == []:
			return None
		return self.stack[len(self.stack) - 1]

	def min(self):
		if self.min_stack == []:
			return None
		return self.min_stack[len(self.min_stack) - 1]

	def print_stack(self):
		for x in self.stack:
			print(x, end = " ")

def main():
	stack = Stack()
	arr = [2, 8, 1, 0, 5]
	for x in arr:
		stack.push(x)
		print('Min elem:' + str(stack.min()))

	for i in range(len(arr)):
		print('Top elem:' + str(stack.pop()))
		print('Min elem:' + str(stack.min()))

if __name__ == "__main__":
	main()