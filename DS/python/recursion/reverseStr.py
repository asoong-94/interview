def reverseStr(string):
	if len(string) == 1:
		return string 
	else:
		return string[-1] + reverseStr(string[:-1])

if __name__ == '__main__':
	print reverseStr("abcde")
	print reverseStr("123456789")