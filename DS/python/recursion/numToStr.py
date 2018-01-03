def numToStr(number, base):
	"""
	tostr(769) --> 769 // 10, remainder + 9
	tostr(76)  --> 76 // 10, remainder + 6
	tostr(7)   --> 7 // 10, remainder + 7
	"""
	bases = '0123456789ABCDEF'
	if number < base:
		return bases[number]
	else:
		return numToStr(number//base, base) + bases[number%base]

print(numToStr(1234,10))
