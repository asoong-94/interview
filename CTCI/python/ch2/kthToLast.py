from linkedlist import UnorderedList


def kth_to_last(ll, k):
	current = ll.head
	for i in range(k):
		current = current.next

	return current.value

if __name__ == '__main__':
	ll = UnorderedList()
	ll.add(1)
	ll.add(2)
	ll.add(3)
	ll.add(4)
	ll.add(5)
	ll.add(6)
	ll.add(7)
	ll.add(8)
	ll.add(9)
	ll.add(0)
	ll.printList()
	print "kth to last"
	print kth_to_last(ll, 3)
