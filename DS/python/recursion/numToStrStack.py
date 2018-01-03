from stack import Stack

resStack = Stack()

def numToStr(n, base):
	bases = "0123456789ABCDEF"
	while n > 0:
		if n < base:
			resStack.push(bases[n])
		else:
			resStack.push(bases[n%base])
		n // base
	res = ""
	while resStack:
		res = res + str(resStack.pop())
	return res

if __name__ == '__main__':
	print numToStr(8,2)