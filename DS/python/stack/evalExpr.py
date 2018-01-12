import operator
import unittest 

OPENING = '('
CLOSING = ')'
OP = ["+", "-", "*", "/"]
NUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def evaluate(expr):
	stack = [] 
	for arg in expr:
		if arg == OPENING:
			stack.append(arg)
		elif arg is not OPENING and arg is not CLOSING:
			stack.append(arg)
		elif arg == CLOSING:
			# stack.append(arg)
			b = int(stack.pop())
			op = stack.pop()
			a = int(stack.pop())
			if op is "+":
				stack.pop()
				stack.append(operator.add(a, b))
			if op is"-":
				stack.pop()
				stack.append(operator.sub(a, b))
			if op is "*":
				stack.pop()
				stack.append(operator.mul(a, b))
			if op is "/":
				# print "divide"
				stack.pop()
				stack.append(operator.floordiv(a, b))

	print stack
	if len(stack) == 1:
		return stack[0]


class test_eval(unittest.TestCase):
	DATA = [
		["(1+1)", 2],
		["(2*4)", 8],
		["(5-1)", 4],
		["(8/2)", 4],
		["(2+(2*4))", 10],
		["((2*4)+2)", 10],
		["((2*4)-(2*2))", 4]
	]

	def test(self):
		for expr, res in self.DATA:
			_res = evaluate(expr)
			self.assertEqual(res, _res)

if __name__ == '__main__':
	expr1 = "(1+1)"
	expr2 = "(2*4)"
	expr4 = "(2+(2*4))"
	expr5 = "((2*4)+(2*2))"


	# print evaluate(expr1)
	# print evaluate(expr2)
	# print evaluate(expr4)
	# print evaluate(expr5)
	# print evaluate("(8/2)")
	unittest.main()





