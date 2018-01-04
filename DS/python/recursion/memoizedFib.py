def fib(n, lookup):
	"""
	similar to recursion
	store results into lookup table before computing solutions
	if solution is not in lookup, then calculate
	if in then just return it
	"""
	# base case 
	if n == 1 or n == 0:
		lookup[n] = n

	# if value is not calculated in lookup then calculate
	if lookup[n] is None:
		lookup[n] = fib(n - 1, lookup) + fib(n-2, lookup)

	return lookup[n]

if __name__ == '__main__':
	lookup = [None for x in xrange(0, 100)]
	n = 8
	print fib(n, lookup)