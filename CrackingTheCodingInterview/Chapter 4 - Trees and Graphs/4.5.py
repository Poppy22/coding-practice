class Node:
	def __init__(self, x, p):
		self.value = x
		self.left = None
		self.right = None
		self.parent = p

class BinaryTree:
	def __init__(self, x):
		self.root = Node(x, None)

	def insert(self, value):
		self.__insert_helper(self.root, value)


	def __insert_helper(self, current_node, value):
		if value > current_node.value:
			if current_node.right == None:
				# append as right child
				new_node = Node(value, current_node)
				current_node.right = new_node
				return
			self.__insert_helper(current_node.right, value)
		else:
			if current_node.left == None:
				# append as left child
				new_node = Node(value, current_node)
				current_node.left = new_node
				return
			self.__insert_helper(current_node.left, value)


	def in_order_traversal(self):
		self.__in_order_traversal_helper(self.root)


	def pre_order_traversal(self):
		self.__pre_order_traversal_helper(self.root)


	def post_order_traversal(self):
		self.__post_order_traversal_helper(self.root)


	def __in_order_traversal_helper(self, node):
		if node == None:
			return
		self.__in_order_traversal_helper(node.left)
		print(node.value)
		self.__in_order_traversal_helper(node.right)


	def __pre_order_traversal_helper(self, node):
		if node == None:
			return
		print(node.value)
		self.__pre_order_traversal_helper(node.left)
		self.__pre_order_traversal_helper(node.right)


	def __post_order_traversal_helper(self, node):
		if node == None:
			return
		self.__post_order_traversal_helper(node.right)
		print(node.value)
		self.__post_order_traversal_helper(node.left)


	def dfs(self):
		if self.root == None:
			return

		stack = [self.root]

		while len(stack):
			node = stack.pop()
			print(node.value)

			if node.right != None:
				stack.append(node.right)
			if node.left != None:
				stack.append(node.left)

	def bfs(self):
		if self.root == None:
			return

		q = [self.root]

		while len(q):
			node = q[0]
			print(node.value)
			del q[0]
			if node.left != None:
				q.append(node.left)
			if node.right != None:
				q.append(node.right)

	def check_binary_search_tree(self):
		# if the values are sorted when doing a in order traversal
		# then it's a binary search tree, OR:
		if self.root == None:
			return True
		return self.__check_binary_search_tree_helper(self.root)


	def __check_binary_search_tree_helper(self, node):
		if node.left != None:
			if node.left.value > node.value:
				return False
			self.__check_binary_search_tree_helper(node.left)
		if node.right != None:
			if node.right.value < node.value:
				return False
			self.__check_binary_search_tree_helper(node.right)
		return True


	def compute_height(self):
		if self.root == None:
			return 0
		return self.__compute_height_helper(self.root)


	def checked_balance(self):
		if self.root == None:
			return True
		return self.__checked_balance(self.root)


	def __compute_height_helper(self, node):
		if node == None:
			return 0
		return 1 + max(self.__compute_height_helper(node.left), self.__compute_height_helper(node.right))


	def __checked_balance(self, node):
		# for every node check if |h(left) - h(right)| <= 1
		h_right = self.__compute_height_helper(node.right)
		h_left = self.__compute_height_helper(node.left)

		if abs(h_right - h_left) > 1:
			return False

		if node.left != None and node.right != None:
			return self.__checked_balance(node.left) and self.__checked_balance(node.right)
		if node.left != None:
			return not (node.left.left or node.left.right)
		if node.right != None:
			return not (node.right.left or node.right.right)
		return True


	def predecessor(self, value):
		if self.root == None:
			return None

		node = self.__find_node_by_value(value, self.root)
		if node == None:
			return None

		if node.left:
			return self.__get_maximum(node.left)

		pre = None
		start = self.root
		while start != node:
			if node.value > start.value:
				pre = start.value # closest node for which the current node is a right child
				start = start.right
			else:
				start = start.left

		return pre


	def successor(self, value):
		if self.root == None:
			return None

		node = self.__find_node_by_value(value, self.root)
		if node == None:
			return None

		if node.right:
			return self.__get_minimum(node.right)

		succ = None
		start = self.root
		while start != node:
			if node.value < start.value:
				succ = start.value # closest node for which the current node is a left child
				start = start.left
			else:
				start = start.right

		return succ


	def __find_node_by_value(self, value, node):
		if node.value == value:
			return node
		if value < node.value and node.left != None:
			return self.__find_node_by_value(value, node.left)
		elif value > node.value and node.right != None:
			return self.__find_node_by_value(value, node.right)
		return None


	def __get_minimum(self, node):
		if self.root == None:
			return None

		if node.left == None:
			return node.value

		return self.__get_minimum(node.left)


	def __get_maximum(self, node):
		if self.root == None:
			return None

		if node.right == None:
			return node.value

		return self.__get_maximum(node.right)


def main():
	bt = BinaryTree(10)
	bt.insert(5)
	bt.insert(9)
	bt.insert(13)
	bt.insert(20)
	bt.insert(15)
	bt.insert(2)

	bt.in_order_traversal()
	print("___________________")
	print(bt.check_binary_search_tree())
	print("___________________")
	bt.dfs()
	print("___________________")
	bt.bfs()
	print("___________________")
	print(bt.compute_height())
	print(bt.checked_balance())
	print(bt.predecessor(10))
	print(bt.successor(5))

if __name__ == "__main__":
	main()