def fib(n):
	# declare table
	table = [0] * (n + 1)
	table[1] = 1

	for i in xrange(2, n+1):
		table[i] = table[i - 1] + table[i - 2]
	return table[n]

if __name__ == '__main__':
	print fib(10)
	print fib(5)
	print fib(8)
