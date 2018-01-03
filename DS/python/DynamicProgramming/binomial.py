def recursiveBinomial(n, k):
	"""   
    BASE CASE: C(n, 0) = C(n, n) = 1
	RECURSIVE CALL: C(n, k) = C(n-1, k-1) + C(n-1, k)
	"""
	if k == 0 or k == n:
		return 1
	else:
		return recursiveBinomial(n - 1, k - 1) + recursiveBinomial(n - 1, k)

def DPBinomial(n, k):
	C = [[0 for x in range(k+1)] for x in range(n+1)]
	for i in range(n+1):
		for j in range(min(i, k) + 1):
			# base case 
			if j == 0 or j == i:
				C[i][j] = 1
			else:
				# use previously calculated numbers 
				C[i][j] = C[i-1][j-1] + C[i-1][j]
	return C[n][k]

def DPBinomial2(n, k):
	# Declaring an empty array
    C = [0 for i in xrange(k+1)]
    C[0] = 1 #since nC0 is 1
 
    for i in range(1,n+1):
 
        # Compute next row of pascal triangle using
        # the previous row
        j = min(i ,k)
        while (j>0):
            C[j] = C[j] + C[j-1]
            j -= 1
 
    return C[k]

if __name__ == '__main__':
	n = 5 # n rows
	k = 2 # k columns

	# print recursiveBinomial(n, k)
	print DPBinomial(n, k)
	print DPBinomial2(n, k)







