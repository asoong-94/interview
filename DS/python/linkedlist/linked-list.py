class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, new):
		self.data = new

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
			current = current.getNext()

		return count


	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True 
			else:
				current = current.getNext()

		return found


	def remove(self, item):
		current = self.head
		prev = None
		found = False
		# iterate till found item
		while not found:
			if current.getData() == item:
				found = True
			else:
				prev = current
				current = current.getNext()

		# set prev to next to skip over the found element
		if prev == None:
			self.head = current.getNext()
		else:
			prev.setNext(current.getNext())


if __name__ == '__main__':
	ll = UnorderedList()
	ll.add(12)
	ll.add(23)
	ll.add(34)
	ll.add(54)
	ll.add(98)
	print ll.search(34)










