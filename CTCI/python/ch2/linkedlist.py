class Node:
	def __init__(self, initdata):
		self.value = initdata
		self.next = None

	def value(self):
		return self.value

	def next(self):
		return self.next

	def setValue(self, new):
		self.value = new

	def setNext(self, newNext):
		self.next = newNext

class UnorderedList:
	def __init__(self):
		# init to nothing 
		self.head = None

	def isEmpty(self):
		# list is empty if head is None again
		return self.head == None

	def add(self, item):
		temp = Node(item)
		# temp point to whatever head is pointing to 
		temp.setNext(self.head)
		# temp is the new head
		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.next()

		return count


	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.value() == item:
				found = True 
			else:
				current = current.next()

		return found


	def remove(self, item):
		current = self.head
		prev = None
		found = False
		# iterate till found item
		while not found:
			if current.value() == item:
				found = True
			else:
				prev = current
				current = current.next()

		# set prev to next to skip over the found element
		if prev == None:
			self.head = current.next()
		else:
			prev.setNext(current.next())

	def printList(self):
		current = self.head
		while current is not None:
			print current.value
			current = current.next




if __name__ == '__main__':
	ll = UnorderedList()
	ll.add(12)
	ll.add(23)
	ll.add(34)
	ll.add(54)
	ll.add(98)
	ll.printList()










