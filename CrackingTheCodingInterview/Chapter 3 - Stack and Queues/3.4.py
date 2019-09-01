# implement a queue using two stacks

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

	def size(self):
		return len(self)

	def is_empty(self):
		return len(self.stack) == 0

class MyQueue:
	def __init__(self):
		self.stack_new = Stack()
		self.stack_old = Stack()

	def enqueue(self, x):
		self.stack_new.push(x)

	def dequeue(self):
		if self.stack_old.is_empty():
			self.move_elements()
		return self.stack_old.pop()

	def peek(self):
		if self.stack_old.is_empty():
			self.move_elements()
		return self.stack_old.top()

	def move_elements(self):
		while not self.stack_new.is_empty():
			self.stack_old.push(self.stack_new.pop())

	def size(self):
		return self.stack_old.size() + self.stack_new.size()


def main():
	queue = MyQueue()
	arr = [2, 8, 1, 0, 5]
	for x in arr:
		queue.enqueue(x)

	print(queue.dequeue())
	print(queue.dequeue())
	print(queue.peek())
	print(queue.dequeue())
	print(queue.dequeue())
	print(queue.peek())
	print(queue.dequeue())
	print(queue.peek())
	print(queue.dequeue())

if __name__ == "__main__":
	main()
