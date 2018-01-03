FibArray = [0, 1]

def fibonacci(n):
	"""
	0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ..
	fn = fn-1 + fn-2
	f0 = 0
	f1 = 1
	use dynamic programming, to record the work already done
	time O(n)
	space O(n)
	"""
	if n <= len(FibArray):
		return FibArray[n - 1]
	else:
		temp = fibonacci(n-1) + fibonacci(n-2)
		FibArray.append(temp)
		return temp

if __name__ == '__main__':
	print fibonacci(100)
