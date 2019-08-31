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

def remove_duplicates_1(root):
	# Time: O(n) -> going once through the list
	# Space: O(n) -> using a dictionary to keep fast track of the previous added elements
	freq = {}
	p = root
	while p:
		if p.value not in freq.keys():
			freq[p.value] = 1
			q = p
			p = p.next
		else:
			# remove it from the list
			q.next = p.next
			del p
			p = q.next


def remove_duplicates_2(root):
	# Time: O(n^2) -> searching for duplicates for each element
	# Space: O(1) -> no additional memory needed
	p = root
	while p:
		v = p.value
		q = p.next
		q_parent = p

		while q:
			if v == q.value:
				# remove duplicate
				q_parent.next = q.next
				del q
				q = q_parent.next
			else:
				q_parent = q
				q = q.next

		p = p.next


def main():
	list_elems = [1, 10, 5, 5, 7, 1, 2, 3, 10, 5, 1, 3, 4, 10, 1]

	root = LinkedNode(list_elems[0])
	last_node = root
	for i in range(1, len(list_elems)):
		last_node = last_node.add(list_elems[i])

	remove_duplicates_2(root)
	root.print()

if __name__ == "__main__":
	main()
