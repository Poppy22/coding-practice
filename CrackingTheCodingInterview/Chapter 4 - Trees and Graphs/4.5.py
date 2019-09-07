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
		stack = [self.root]

		while len(stack):
			node = stack.pop()
			print(node.value)

			if node.right != None:
				stack.append(node.right)
			if node.left != None:
				stack.append(node.left)

	def bfs(self):
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
		return self.__compute_height_helper(self.root)


	def checked_balance(self):
		return self.__checked_balance(self.root)


	def __compute_height_helper(self, node):
		pass


	def __checked_balance(self, node):
		pass


	def __get_minimum(self, node):
		pass


	def __get_maximum(self, node):
		pass


	

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

if __name__ == "__main__":
	main()