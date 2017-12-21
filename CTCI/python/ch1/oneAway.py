import unittest


def samelength(s1, s2):
	foundDiff = False
	data = zip(s1, s2)
	for d in data:
		if d[0] != d[1]:
			if foundDiff == False:
				foundDiff = True
			else:
				return False
		else:
			continue

	return True

def diffByInsert(s1, s2):
	i, j = 0, 0
	foundDiff = False
	while i < len(s1) and j < len(s2):
		if s1[i] != s2[j]:
			if foundDiff:
				return False
			foundDiff = True
			j += 1
		else:
			i += 1 
			j += 1
	return True

def oneAway(s1, s2):
	"""
	give 2 strings, determine if one edit away 
	pale, ple -> true
	pales, pale -> true
	pale, bale -> true
	pale, bake -> false
	"""
	
	# case 1: strings are same length
	if len(s1) == len(s2):
		return samelength(s1, s2)
	elif len(s1) + 1 == len(s2):
		diffByInsert(s1, s2)
	elif len(s1) - 1 == len(s2):
		diffByInsert(s2, s1)



class oneAwayTest(unittest.TestCase):

	def test_one_away(self):
        	for [_s1, _s2, _res] in self.TEST_DATA:
        		res = oneAway(_s1, _s2)
        		self.AssertEqual(res, _res)

	TEST_DATA = [
		('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
		]




if __name__ == '__main__':
	unittest.main()


