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

def compute_partition(root, p):
	first_left = first_right = last_left = last_right = None
	while root:
		if root.value < p:
			if not first_left:
				first_left = last_left = root
			else:
				last_left.next = root
				last_left = root

		else:
			if not first_right:
				first_right = last_right = root
			else:
				last_right.next = root
				last_right = root

		root = root.next

	if last_right:
		last_right.next = None
	else:
		last_left.next = None

	if last_left:
		last_left.next = first_right
	else:
		first_left = first_right

	return first_left

def main():
	list_elems = [10, 3, 5, 8, 5, 2, 1]
	partition = int(input())

	root = LinkedNode.create_list(list_elems)
	root = compute_partition(root, partition)
	root.print()

if __name__ == "__main__":
	main()