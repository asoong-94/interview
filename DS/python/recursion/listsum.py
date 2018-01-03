def listsum(numList):
	"""
	listsum(numlist) = numlist[0] + listsum(rest(numlist))
	"""

	if len(numList) == 1:
		return numList[0]
	else:
		# numlist[1:] is the rest of the list
		return numList[0] + listsum(numList[1:])


if __name__ == '__main__':
	l = [1,2,3,4,5]
	print listsum(l)