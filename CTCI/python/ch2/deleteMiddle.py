from linkedlist import UnorderedList

def deleteMiddle(node):
	"""
	modified my linked list implementation 
	to return the node, when adding to list 
	set next, to next next 
	"""
	node.value = node.next.value
	node.next = node.next.next

if __name__ == '__main__':
	"""
	delete 100 from list
	"""
	ll = UnorderedList()
	ll.add(1)
	ll.add(2)
	ll.add(3)
	ll.add(4)
	ll.add(5)
	middle = ll.add(100)
	ll.add(6)
	ll.add(7)
	ll.add(8)
	ll.add(9)
	ll.add(0)
	ll.printList()
	print "deleteMiddle"

	deleteMiddle(middle)
	ll.printList()
