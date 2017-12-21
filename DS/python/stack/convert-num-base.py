import unittest

def convert_to_binary(decimal_number):
	"""
	use the divide by 2 algorithm 
	convert decimal to binary 
	"""
	stack = []

	while decimal_number > 0:
		remainder = decimal_number % 2
		stack.append(remainder)
		decimal_number = decimal_number // 2

	binary_digits = []
	while stack:
		binary_digits.append(str(stack.pop()))

	return ''.join(binary_digits)


NUMBERS = '0123456789abcdef'
def convert_to_base(decimal_number, base):
	stack = []

	while decimal_number > 0:
		remainder = decimal_number % base
		stack.append(remainder)
		decimal_number = decimal_number // base

	digits = []
	while stack:
		digits.append(NUMBERS[stack.pop()])

	return ''.join(digits)



class convert_num_test(unittest.TestCase):
	BINARY_TEST_DATA = [
		[32, '100000'],
		[123123, '11110000011110011'],
		[4987234, '10011000001100101100010'],
		[12, '1100']
	]

	BASE_TEST_DATA = [
		[25, 2, '11001'],
		[25, 16, '19']
	]


	def test(self):
		for _in, _out in self.BINARY_TEST_DATA:
			res = convert_to_binary(_in)
			self.assertEqual(res, _out)

		for _in, _base, _out in self.BASE_TEST_DATA:
			res2 = convert_to_base(_in, _base)
			self.assertEqual(res2, _out)



if __name__ == '__main__':
	unittest.main()
