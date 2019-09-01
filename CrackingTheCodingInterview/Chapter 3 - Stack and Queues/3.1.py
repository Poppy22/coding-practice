class ThreeStacks:
	def __init__(self):
		self.stack = [None] * 3
		self.last = [-3, -2, -1]

	def push(self, x, stack_no):
		self.stack[self.last[stack_no - 1] + 3] = x
		self.last[stack_no - 1] += 3
		n = len(self.stack)
		if not(self.stack[n - 1] is None and self.stack[n - 2] is None and self.stack[n - 3] is None):
			self.stack.extend([None] * 3) # make more room

	def pop(self, stack_no):
		if self.last[stack_no - 1] < 0:
			return None
		x = self.stack[self.last[stack_no - 1]]
		self.stack[self.last[stack_no - 1]] = None
		self.last[stack_no - 1] -= 3
		self.clean_stack()
		return x

	def top(self, stack_no):
		if self.last[stack_no - 1] < 0:
			return None
		x = self.stack[self.last[stack_no - 1]]
		return x

	def clean_stack(self):
		# remove items from memory if possible
		# remove 3 None elements at a time, at the end of the stack
		n = len(self.stack)
		while self.stack[n - 1] is None and self.stack[n - 2] is None and self.stack[n - 3] is None:
			del self.stack[n - 3:]
			n = len(self.stack)
		self.stack.extend([None] * 3) # make more room

	def print_stack(self, stack_no):
		i = stack_no - 1
		while i < len(self.stack):
			print(self.stack[i], end = " ")
			i += 3
		print()

def main():
	stack = ThreeStacks()

	# push test
	for i in range(5):
		stack.push(1, 1)
		stack.push(2, 2)
		stack.push(3, 3)
	for i in range(3):
		stack.push(2, 2)
	for i in range(2):
		stack.push(3, 3)

	stack.print_stack(1)
	stack.print_stack(2)
	stack.print_stack(3)

	# pop test
	for i in range(5):
		stack.pop(1)
		stack.pop(2)
		stack.pop(3)

	print(stack.pop(1)) # should be None
	stack.print_stack(1)
	stack.print_stack(2)
	stack.print_stack(3)

if __name__ == "__main__":
	main()
