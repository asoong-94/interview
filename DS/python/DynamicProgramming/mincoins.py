def mincoins(coins, total):
	"""
	T to keep track of min number of coins to get to the ith value in T
	R to determine which coin was last used to get to that value
	T[i] = min(T[i], T[i - coins[j]])
	Total at i = T without picking jth coin OR T with picking jth coin
	"""
	cols = total + 1
	T = [0 if idx == 0 else float("inf") for idx in range(cols)]
	R = [-1 for x in range(cols)]

	# for each coin
	for j in range(len(coins)):
		# for each value from 1 to total 
		for i in range(1, cols):
			# if ith value can be fulfilled by a coin
			if i >= coins[j]:
				# compare the min value
				if T[i] > 1 + T[i - coins[j]]:
					# T[i] = min(T[i], T[i - coins[j]])
					T[i] = 1 + T[i - coins[j]]
					# assign R[i] to jth coin in coins
					R[i] = j

	# print out Totals array
	print "T: " + str(T)
	# print out Coins array 
	print "R: " + str(R)

	print_coins(R, coins)
	return T[total - 1]

def print_coins(R, coins):
	"""
	print the coins used to achieve the total value 
	"""
	start = len(R) - 1

	while start != 0:
		coin = coins[R[start]]
		print "coin: %d " % coin
		start = start - coin

if __name__ == '__main__':
	coins = [7,2,3,6]
	total = 22
	print "coins used: " + str(coins)
	print mincoins(coins, total)
