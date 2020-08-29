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


	def count_nodes(self):
		return self.__count_nodes_helper(self.root)

	def __count_nodes_helper(self, node):
		# in order traversal where we keep track of the number of nodes
		count = 1
		if node.left:
			count += self.__count_nodes_helper(node.left)
		if node.right:
			count += self.__count_nodes_helper(node.right)

		return count

	def count_smaller_than(self, x):
		# find the node with the value x and then count
		# the number of nodes in that subtree
		start_node = self.find_node(self.root, x)
		if not start_node:
			return 0

		return self.__count_nodes_helper(start_node)

	def count_leaves(self):
		return self.__count_leaves_helper(self.root)


	def __count_leaves_helper(self, node):
		if not node.left and not node.right:
			count = 1
		else:
			count = 0
		if node.left:
			count += self.__count_leaves_helper(node.left)
		if node.right:
			count += self.__count_leaves_helper(node.right)

		return count

		# or:
		# if not node:
		# 	return 0
		# if not node.left and not node.right:
		# 	return 1
		# return self.__count_leaves_helper(node.left) + self.__count_leaves_helper(node.right)

	def find_node(self, node, x):
		if node.value == x:
			return node
		if node.left and node.value > x:
			return self.find_node(node.left, x)
		if node.right and node.value < x:
			return self.find_node(node.right, x)
		return None

	def check_equal(self, tree):
		return self.__check_equal_helper(self.root, tree.root)


	def __check_equal_helper(self, root1, root2):
		if not root1 and not root2:
			return 1
		elif root1 and not root2:
			return 0
		elif not root1 and root2:
			return 0
		elif root1.value == root2.value and self.__check_equal_helper(root1.left, root2.left) and self.__check_equal_helper(root1.right, root2.right):
			return 1
		return 0


	def depth_node(self, x):
		return self.__depth_node_helper(self.root, x, 0)


	def __depth_node_helper(self, node, x, level):
		if node.value == x:
			return level
		if node.left and node.value > x:
			return self.__depth_node_helper(node.left, x, level + 1)
		if node.right and node.value < x:
			return self.__depth_node_helper(node.right, x, level + 1)
		return -1


def main():
	bt = BinaryTree(10)
	bt.insert(5)
	bt.insert(9)
	bt.insert(13)
	bt.insert(20)
	bt.insert(15)
	bt.insert(2)

	print("Number of nodes:" + str(bt.count_nodes()))
	print("Number of nodes smaller than: " + str(bt.count_smaller_than(5)))
	print("Number of leaves: " + str(bt.count_leaves()))
	print("Depth level: " + str(bt.depth_node(15)))

	bt2 = BinaryTree(10)
	bt2.insert(5)
	bt2.insert(9)
	bt2.insert(13)
	bt2.insert(20)
	bt2.insert(15)
	bt2.insert(2)

	print("Equal:", bt.check_equal(bt2))

if __name__ == "__main__":
	main()