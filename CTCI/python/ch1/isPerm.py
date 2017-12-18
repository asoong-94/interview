import unittest 

def perm_sort(str1, str2):
	"""
	compare sorted lists 
	O(logn)
	"""
	s1 = list(str1)
	s2 = list(str2)
	s1.sort(), s2.sort()
	return s1 == s2


class NoDupicatesTest(unittest.TestCase):
	TEST_DATA = [
		['abc', 'bca', True],
		['aaa', 'bca', False],
		['abc', 'bcb', False],
		['xyz', 'zyx', True]
	]

	def test(self):
		for _str1, _str2, _res in self.TEST_DATA:
			_res1 = perm_sort(_str1, _str2)
			self.assertEqual(_res1, _res)




if __name__ == '__main__':
	unittest.main()
	# print perm_sort("bca", "cba")