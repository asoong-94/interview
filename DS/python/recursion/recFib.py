def fibonacci(n):
	"""
	0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
	fn = fn-1 + fn-2
	f0 = 0
	f1 = 1
	exponential run time, is terrible
	"""
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
	print fibonacci(5)
	print fibonacci(100)

