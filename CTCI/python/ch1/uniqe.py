import unittest 


def unique_set(str):
	"""
	return true or false
	if a string is all unique characters
	O(n) iterate through strings in array once
	dumb because set of a string will only take unique characters
	"""
	myset = set()
	for c in str:
		if c in myset:
			return False 
		else:
			myset.add(c)
	return True

def unique_set_2(str): 
	"""
	smarter because takes advantage of set construction with uniques
	O(1)
	"""
	return len(str) == len(set(str))

def unique_no_data_structures(str):
	"""
	string has a count variable in python 
	if a character's count is creater than 1, return false 
	O(n)
	"""
	for c in str:
		if str.count(c) > 1:
			return False 

	return True 




class NoDupicatesTest(unittest.TestCase):
	# two element tuples of input string and expected result
	TEST_DATA = [
		('a', True),
		('ab', True),
		('abc', True),
		('aaa', False),
		('bba', False),
		('abababaa', False),
	]

	def test(self):
		for _str, _res in self.TEST_DATA:
			_res1 = unique_set(_str)
			self.assertEqual(_res1, _res)

		for _str, _res in self.TEST_DATA:
			_res1 = unique_set_2(_str)
			self.assertEqual(_res1, _res)

		for _str, _res in self.TEST_DATA:
			_res1 = unique_no_data_structures(_str)
			self.assertEqual(_res1, _res)

if __name__ == '__main__':
	unittest.main()