import operator 

OPERATORS = {
	'+' : operator.add,
	'-' : operator.sub,
	'*' : operator.mul, 
	'/' : operator.truediv
}

LEFT_PAREN = '('
RIGHT_PAREN = ')'

def build_parse_tree(expression):
	tree = {}
	stack = [tree]
	node = tree

	for token in expression:
		if token == LEFT_PAREN:
			# create left child and descend to it
			node['left'] = {}
			stack.append(node)
			node = node['left']
		elif token == RIGHT_PAREN:
			# return to parent
			node = stack.pop()
		elif token in OPERATORS.keys():
			# set val to operator, create right and descend
			node['val'] = token
			node['right'] = {}
			stack.append(node)
			node = node['right']
		else:
			# if token is an int
			node['val'] = int(token)
			parent = stack.pop()
			# go back to parent
			node = parent
	return tree


if __name__ == '__main__':
	expression = '(3+(4*5))'
	print build_parse_tree(expression)


