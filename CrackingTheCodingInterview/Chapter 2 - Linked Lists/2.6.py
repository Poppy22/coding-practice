class LinkedNode:
	def __init__(self, value):
		self.value = value
		self.next = None

	def add(self, value):
		new_node = LinkedNode(value)
		self.next = new_node
		return new_node

	def print(self):
		p = self
		while p != None:
			print(str(p.value) + " -> ", end = " ")
			p = p.next
		print()

	def create_list(list_elems):
		root = LinkedNode(list_elems[0])
		last_node = root
		for i in range(1, len(list_elems)):
			last_node = last_node.add(list_elems[i])
		return root

def is_palindrome(root):
	stack = []
	slow, fast = root, root
	odd = False

	while fast:
		stack.append(slow.value)
		slow = slow.next
		fast = fast.next
		if fast:
			fast = fast.next
		else:
			odd = True

	if odd:
		stack.pop()

	while slow:
		if slow.value != stack.pop():
			return False
		slow = slow.next

	return True


def main():
	list_elems = [1, 2, 4, 4, 2, 1]

	root = LinkedNode.create_list(list_elems)
	print(is_palindrome(root))

if __name__ == "__main__":
	main()