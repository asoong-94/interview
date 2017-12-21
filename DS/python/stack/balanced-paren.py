import unittest 



OPENING = '('
def is_balanced(parentheses):
	"""
	take in a group of parentheses, determine if valid or not. 
	use a stack to keep track of the parentheses.
	if '(' push, if ')' pop
	"""
	stack = []
	for p in parentheses:
		if p == OPENING:
			stack.append(p)
		else:
			try:
				stack.pop()
			except IndexError: # too many closing paren
				return False
	return len(stack) == 0 # if this fail, too many opening paren




class balanced_paren_test(unittest.TestCase):

	TEST_DATA = [
		('()()(())', True),
		('(()())(())', True),
		('((())()()', False)
	]

	def test(self):
		for _paren, _res in self.TEST_DATA:
			res = is_balanced(_paren)
			self.assertEqual(res, _res)



if __name__ == '__main__':
	unittest.main()



	