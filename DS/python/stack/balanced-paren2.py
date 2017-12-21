import unittest 

PAIRINGS = {
	'(' : ')',
	'{' : '}',
	'[' : ']'
	}

def is_balanced(parentheses):
	"""
	same problem as balanced-paren.py but accounting for different 
	"""
	stack = []
	for p in parentheses:
		if p in PAIRINGS.keys():
			stack.append(p)
			continue
		try:
			expected_opening = stack.pop()
		except IndexError:
			return False 
		if p != PAIRINGS[expected_opening]: # if ( the next thing has to be )
			return False
	return len(stack) == 0



class balanced_paren_test(unittest.TestCase):

	TEST_DATA = [
		('{{([][])}()}', True),
		('{[])', False),
		('((()))', True)
	]

	def test(self):
		for _paren, _res in self.TEST_DATA:
			res = is_balanced(_paren)
			self.assertEqual(res, _res)



if __name__ == '__main__':
	unittest.main()

