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

def add_numbers(root_1, root_2):
	carry = 0
	p = None
	result = root_1

	while root_1 and root_2:
		s = root_1.value + root_2.value + carry
		carry = s // 10
		root_1.value = s % 10
		p = root_1
		root_1 = root_1.next
		root_2 = root_2.next

	while root_1 and carry:
		s = root_1.value + carry
		carry = s // 10
		root_1.value = s % 10
		p = root_1
		root_1 = root_1.next

	p.next = root_2

	while root_2 and carry:
		s = root_2.value + carry
		carry = s // 10
		root_2.value = s % 10
		p = root_2
		root_2 = root_2.next

	if carry:
		new_digit = LinkedNode(carry)
		p.next = new_digit

	return result


def main():
	number_1 = [1, 1]
	number_2 = [9, 9, 9]

	list_1 = LinkedNode.create_list(number_1)
	list_2 = LinkedNode.create_list(number_2)

	result = add_numbers(list_1, list_2)
	result.print()

if __name__ == "__main__":
	main()