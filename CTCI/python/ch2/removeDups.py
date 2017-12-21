from linkedlist import UnorderedList

def removeDups(ll):
	"""
	add seen elements to a set
	if not in set, add
	if in set skip to curr.next.next
	"""
	if ll.head is None: 
		return 

	current = ll.head
	seen = set([current.value])
	while current.next:
		if current.next.value in seen:
			current.next = current.next.next
		else:
			seen.add(current.next.value)
			current = current.next
	return ll


def removeDups2(ll):
	"""
	tried to do in place, not working rn
	"""
	if ll.head is None:
		return 

	current == ll.head
	while current:
		runner = current
		while runner.next:
			# if next is the same as current, then skip it
			if runner.next.value == current.value:
				runner.next = runner.next.next
			else:
				runner = runner.next
		current = current.next

	return ll

if __name__ == '__main__':
	ll = UnorderedList()
	ll.add(1)
	ll.add(2)
	ll.add(2)
	ll.add(3)
	ll.add(3)
	ll.add(3)
	ll.add(4)
	ll.add(4)
	ll.add(4)
	ll.add(4)
	ll.printList()
	ll = removeDups(ll)
	print "after removeDups"
	ll.printList()





