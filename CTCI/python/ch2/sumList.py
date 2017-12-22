from linkedlist import UnorderedList

def sumlist(ll1, ll2):
	ll = UnorderedList()
	carry = 0

	n1 = ll1.head
	n2 = ll2.head

	while n1 or n2:
		result = carry
		if n1:
			result += n1.value
			n1 = n1.next

		if n2:
			result += n2.value
			n2 = n2.next

		singles = result % 10
		ll.add(singles)
		carry = result // 10

	if carry is not 0:
		ll.add(carry)

	return ll


if __name__ == '__main__':
	ll1 = UnorderedList()
	ll2 = UnorderedList()

	ll1.add(7)
	ll1.add(1)
	ll1.add(6)
	ll1.printList()
	print "+"
	ll2.add(5)
	ll2.add(9)
	ll2.add(2)
	ll2.printList()

	ll = UnorderedList()
	ll = sumlist(ll1 ,ll2)
	print "="
	ll.printList()

