class Node(object):
	def __init__(self, val):
		self.val = val 
		self.left = None
		self.right = None


	def insert_left(self, child):
		if self.left is None:
			self.left = child
		else:
			child.left = self.left
			self.left = child

	def insert_right(self, child):
		if self.right is None:
			self.right = child
		else:
			child.right = self.right
			self.right = child

def preorder(tree):
	"""
	recursive
	parent, then left, then right
	"""
	print tree.val
	if tree.left:
		preorder(tree.left)
	if tree.right:
		preorder(tree.right)

def postorder(tree):
	"""
	recursive
	look left, then look right, then parent
	"""
	if tree:
		postorder(tree.left)
		postorder(tree.right)
		print tree.val

def inorder(tree):
	"""
	recursive
	look left, then parent, then look right
	"""
	if tree:
		inorder(tree.left)
		print tree.val
		inorder(tree.right)

if __name__ == '__main__':
	root = Node('a')
	
	root.insert_left(Node('b'))
	root.insert_right(Node('c'))
	preorder(root)
	print "---"
	postorder(root)
	print "---"
	inorder(root)




