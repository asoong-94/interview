def reverseStr(string):
	if len(string) == 1:
		return string 
	else:
		return string[-1] + reverseStr(string[:-1])


def palindrome(string):
	reverse = ""
	if len(string) == 1: 
		return True 
	else:
		if string == reverseStr(string):
			return True
	return False

if __name__ == '__main__':
	print palindrome("abcba")
	print palindrome("12321")
	print palindrome("12333")
