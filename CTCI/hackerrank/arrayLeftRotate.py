def array_left_rotation(a, n):
	for _ in range(n):
		a.append(a.pop(0))
	return a



if __name__ == '__main__':
	array1 = [1,2,3,4,5]
	print array1
	print array_left_rotation(array1, 2)

