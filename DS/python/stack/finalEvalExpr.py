import operator
import unittest 

OPENING = '('
CLOSING = ')'
OP = ["+", "-", "*", "/"]
NUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def evaluate(expr):
	expr = "".join(expr.split(" "))
	stack = []
	numBuff = []
	for arg in expr:
		print "curr char: " + str(arg)
		if arg == OPENING:
			stack.append(arg)
			print "stack: " + str(stack)

		elif arg in NUM:
			numBuff.append(arg)
			print "stack: " + str(stack)

		elif arg in OP:
			if len(numBuff) != 0:
				stack.append("".join(numBuff))
				print "stack: " + str(stack)

			numBuff = []
			stack.append(arg)
			print "stack: " + str(stack)

		elif arg == CLOSING:
			if len(numBuff) != 0:
				stack.append("".join(numBuff))
				print "stack: " + str(stack)

			numBuff = []

			b = int(stack.pop())
			op = stack.pop()
			if op == '-' and op in OP:
				print "HEREEE"
				print "op:" + op
				print "b:" + str(b)
				stack.pop()
				stack.append(int(op+str(b)))
				print "stack: " + str(stack)
			elif op in OP:
				a = int(stack.pop())
				stack.pop()
				if op is "+":
					stack.append(operator.add(a, b))
					print "stack: " + str(stack)

				if op is"-":
					stack.append(operator.sub(a, b))
					print "stack: " + str(stack)

				if op is "*":
					stack.append(operator.mul(a, b))
					print "stack: " + str(stack)

				if op is "/":
					stack.append(operator.floordiv(a, b))
					print "stack: " + str(stack)



			else:
				stack.append(b)
				print "stack: " + str(stack)


	return stack[0]


class test_eval(unittest.TestCase):
	DATA = [
		["(1+1)", 2],
		["(2)", 2],
		["(2*4)", 8],
		# ["(5-1)", 4],
		# ["(100/2)", 50],
		# ["(2+(2*4))", 10],
		# ["((2*4)+2)", 10],
		# ["((2*4)-(2*2))", 4],
		# ["((3 + (4 / 2)) * (5 + 6))", 55],
		# ["((2) + 3)", 5],
		# ["(-2)", -2]

	]

	def test(self):
		for expr, res in self.DATA:
			_res = evaluate(expr)
			self.assertEqual(res, _res)

if __name__ == '__main__':
	expr1 = "(1+1)"
	expr2 = "(2*4)"
	expr4 = "(2+(2*4))"
	expr5 = "((2*4)+((2*2))"
	expr6 = "((3+(4/2))*(5+6))"

	# print evaluate(expr1)
	# print evaluate(expr2)
	# print evaluate(expr4)
	# print evaluate(expr5)
	# print evaluate("(8/2)")
	# print evaluate(expr6)
	unittest.main()





