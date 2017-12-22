class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None




def sumList(l1, l2):
	carry = 0
	root = ll = ListNode(0)

	while l1 or l2:
		result = carry
		if l1:
			result += l1.val
			l1 = l1.next
		if l2:
			result += l2.val
			l2 = l2.next

		singledigit = result % 10 
		carry = result // 10 
		ll.next = ListNode(singledigit)
		ll = ll.next

	if carry is not 0:
		ll.next = ListNode(carry)

	return root.next		


if __name__ == '__main__':
	root = ll = ListNode(2)
	ll.next = ListNode(4)
	ll = ll.next
	ll.next = ListNode(3)

	root1 = ll1 = ListNode(5)
	ll1.next = ListNode(6)
	ll1 = ll1.next
	ll1.next = ListNode(4)

	ans = sumList(root, root1)
	while ans:
		print ans.val
		ans = ans.next



