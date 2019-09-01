class Stack:
	def __init__(self):
		self.stack = []

	def push(self, x):
		self.stack.append(x)

	def pop(self):
		if self.stack == []:
			return None
		return self.stack.pop()

	def top(self):
		if self.stack == []:
			return None
		return self.stack[len(self.stack) - 1]

	def print(self):
		for x in self.stack:
			print(x, end = " ")
		print()

	def size(self):
		return len(self.stack)

	def is_empty(self):
		return self.size() == 0

class SetOfStacks:
	def __init__(self, capacity):
		self.stack_list = [Stack()]
		self.capacity = capacity

	def push(self, x):
		last_stack = self.stack_list[len(self.stack_list) - 1]
		if last_stack.size() < self.capacity:
			last_stack.push(x)
		else:
			new_stack = Stack()
			new_stack.push(x)
			self.stack_list.append(new_stack)

	def pop(self):
		if self.is_empty():
			return None

		last_stack = self.stack_list[len(self.stack_list) - 1]
		if last_stack.is_empty():
			# delete it
			self.stack_list.pop()
			if self.is_empty():
				return None
			last_stack = self.stack_list[len(self.stack_list) - 1]

		return last_stack.pop()

	def top(self):
		if self.is_empty():
			return None

		last_stack = self.stack_list[len(self.stack_list) - 1]
		if last_stack.is_empty():
			if self.stack_list.size() == 1:
				return None
			last_stack = self.stack_list[len(self.stack_list) - 2]

		return last_stack.top()

	def popAt(self, index):
		if index >= self.size():
			return

		last_stack = self.stack_list[index - 1]
		if last_stack.is_empty():
			# delete it
			del self.stack_list[index - 1]
			return None

		return last_stack.pop()

	def print(self):
		for stack in self.stack_list:
			stack.print()

	def size(self):
		size = 0
		for stack in self.stack_list:
			size += stack.size()
		return size

	def is_empty(self):
		return self.stack_list == []


def main():
	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	stacks = SetOfStacks(4)
	for i in arr:
		stacks.push(i)

	stacks.push(10)
	stacks.print()

	print(stacks.top())
	print(stacks.pop())
	stacks.print()
	print(stacks.pop())
	stacks.print()
	print(stacks.pop())
	stacks.print()

	print(stacks.popAt(2))
	print(stacks.popAt(1))
	stacks.print()

	print(stacks.popAt(2))
	print(stacks.popAt(2))
	print(stacks.popAt(2))

if __name__ == "__main__":
	main()


