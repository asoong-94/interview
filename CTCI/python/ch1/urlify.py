import unittest 


def urlify(str):
	"""
	replace all the ' ' with %20 in a string
	split the string on spaces, into list
	join the list on %20
	"""
	return "%20".join(str.split(" "))


class urlifyTest(unittest.TestCase):

	TEST_DATA = [
		("abc def ghi", "abc%20def%20ghi"),
		("xyz wrx tuv", "xyz%20wrx%20tuv")
	]

	def test(self):
		for s1, s2 in self.TEST_DATA:
			res1 = urlify(s1)
			self.assertEqual(res1, s2)


if __name__ == '__main__':
	unittest.main()
