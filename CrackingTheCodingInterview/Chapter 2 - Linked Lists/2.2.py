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

def find_kth_to_last(root, k):
	if not root:
		return None

	first, last = root, root
	# move the first pointer with kth elements in front of last pointer

	i = 0
	while last and i != k:
		i += 1
		last = last.next

	if not last:
		return None

	while last.next:
		first = first.next
		last = last.next

	return first.value

def main():
	list_elems = [1, 2, 3, 4, 5]
	k = int(input())
	root = LinkedNode.create_list(list_elems)
	print(find_kth_to_last(root, k))

if __name__ == "__main__":
	main()