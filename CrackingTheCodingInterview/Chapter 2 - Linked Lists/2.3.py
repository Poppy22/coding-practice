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

	def find_node_by_value(self, value):
		p = self
		while p:
			if p.value == value:
				return p
			p = p.next
		return None


def delete_middle_node(node):
	p = node
	while p.next:
		p.value = p.next.value
		q = p
		p = p.next

	q.next = None
	del p


def main():
	list_elems = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	root = LinkedNode.create_list(list_elems)
	node_to_delete = root.find_node_by_value(5)
	delete_middle_node(node_to_delete)
	root.print()

if __name__ == "__main__":
	main()

