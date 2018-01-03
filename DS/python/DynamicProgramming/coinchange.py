def coinchange(s, m, n):
	"""
	total number of solutions: in 2 sets 
	1. solution that contains the mth coin
	count(set, m-1, n)
	2. solution that does not contain the mth coin
	count(set, m, n-Sm)
	"""
	# n + 1 rows, table is constructed bottom up 
	# base case 0, n = 0
	table = [[0 for x in range(m)] for x in range(n + 1)]
	# fill entries for 0 value, 
	for i in range(m):
		table[0][i] = 1

	# fill in rest of table bottom up
	for i in range(1, n+1):
		for j in range(m):
			# count of solutions including S[j]
			x = table[i - s[j]][j] if i - s[j] >= 0 else 0
			# count of solutions excluding S[j]
			y = table[i][j-1] if j >= 1 else 0

			table[i][j] = x + y
	return table[n][m-1]


if __name__ == '__main__':
	coins = [1,2,3]
	m = len(coins)
	n = 4
	print coinchange(coins, m, n)