
class BinaryHeap(object):
	def __init__(self):
		self.items = [0]

	def __len__(self):
		return len(self.items) - 1

	def percolate_up(self):
		i = len(self)
		# while node i has a parent
		while i // 2 > 0:
			# if i is smaller than i's parent, switch 
			if self.items[i] < self.items[i // 2]:
				self.items[i//2], self.items[i] = self.items[i], self.items[i//2]
			i = i // 2

	def insert(self, k):
		"""
		check to percolate after every insertion
		"""
		self.items.append(k)
		self.percolate_up() 


	def min_child(self, i):
		if i * 2 + 1 > len(self):
			return i * 2

		if self.items[i * 2] < self.items[i * 2 + 1]:
			return i * 2

		return i * 2 + 1


	def percolate_down(self, i):
		while i * 2 < len(self):
			min = self.min_child(i)
			if self.items[i] > self.items[min]:
				self.items[i], self.items[min] = self.items[min], self.items[i]
			i = min

	def delete_min(self):
		"""
		return first thing in list 
		set last thing in array to first thing 
		pop off the last thing 
		percolate the new first thing down to appropriate place 
		"""
		return_val = self.items[1]
		self.items[1] = self.items[len(self)]
		self.items.pop()
		self.percolate_down(1)
		return return_val

	def build_heap(self, alist):
		i = len(alist) // 2
		self.items = [0] + alist
		while i > 0:
			self.percolate_down(i)
			print alist 
			i = i - 1

if __name__ == '__main__':
	heap = [9,5,6,2,4]
	h = BinaryHeap()
	


