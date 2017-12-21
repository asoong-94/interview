import unittest

def compress(s):
	compressed = []
	count = 1
	current = ''
	for i in range(len(s) - 1):
		if s[i] == s[i + 1]:
			count += 1
			current = s[i]
		else:
			compressed.append(current)
			compressed.append(str(count))
			count = 1
			current = s[i + 1]
	return "".join(compressed)

def compress2(s):
	compressed = []
	count = 0

	for i in range(len(s)):
		if i != 0 and s[i] != s[i - 1]:
			compressed.append(s[i - 1])
			compressed.append(str(count))
			count = 0
		count += 1

	compressed.append(s[-1])
	compressed.append(str(count))

	return ''.join(compressed)

class testCompress(unittest.TestCase):
	TEST_DATA = [
 		('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'a1b1c1d1e1f1')
	]

	def test(self):
		for _in, _res in self.TEST_DATA:
			res = compress2(_in)
			self.assertEqual(res, _res)



if __name__ == '__main__':
	unittest.main()