def array_left_rotation(a, n):
	"""
	rotate array a to left n times
	"""
	for _ in range(n):
		a.append(a.pop(0))
	return a


def array_right_rotation(a, n):
	"""
	rotate array a to right n times
	"""
	for _ in range(n):
		a.insert(0, a.pop())
	return a

if __name__ == '__main__':
	array1 = [1,2,3,4,5]
	print array_left_rotation(array1, 2)
	print array_right_rotation(array1, 2)

