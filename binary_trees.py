class Node:
	def __init__(self,value):
		self.left = None
		self.right = None
		self.value = value


class BinarySearchTree:
	def __init__(self):
		self.root=None;


	def insert(self,value):
		new_node = Node(value)
		if self.root == None:
			self.root = new_node
		else:
			current_node = self.root
			while True:
				if value < current_node.value:
					# Left side (less)
					if current_node.left==None:
						current_node.left= new_node
						return self
					else:
						current_node=current_node.left
				else:
					# Right side (greater)
					if current_node.right==None:
						current_node.right=new_node
						return self
					else:
						current_node=current_node.right

	def lookup(self, value):
		current_node = self.root
		while True:
			if current_node== None:
				return False
			if current_node.value == value:
				return True
			elif value <current_node.value:
				current_node = current_node.left
			else:
				current_node.right


	def print_tree(self):
		if self.root != None:
			self.print(self.root)
		


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(6)
tree.insert(170)
tree.insert(15)
print(tree)

tree.lookup(20)
tree.print_tree()