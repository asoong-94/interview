def reverseStr(string):
	if len(string) == 1:
		return string 
	else:
		return string[-1] + reverseStr(string[:-1])

print reverseStr("abcde")