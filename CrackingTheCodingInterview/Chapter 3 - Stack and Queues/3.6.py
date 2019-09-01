DOG = 'DOG'
CAT = 'CAT'

class AnimalShelter():
	def __init__(self):
		# dogs are in even positions, cat in odd positions
		self.animals = [None] * 2
		self.index = {}
		self.index[DOG] = [-2, -2] #(first, last)
		self.index[CAT] = [-1, -1]

	def enqueue(self, pet, ANIMAL_TYPE):
		self.animals[self.index[ANIMAL_TYPE][1] + 2] = pet
		self.index[ANIMAL_TYPE][1] += 2
		if self.index[ANIMAL_TYPE][0]  < 0:
			self.index[ANIMAL_TYPE][0] += 2
		self.make_space()

	def make_space(self):
		n = self.size()
		if not (self.animals[n - 1] is None and self.animals[n - 2] is None):
			self.animals.extend([None] * 2) # make more room

	def dequeue_any(self):
		if self.size() == 0:
			return None
		if self.animals[0] != None:
			# adopt a dog
			return self.dequeue(DOG)
		elif self.animals[1] != None:
			# adopt a cat
			return self.dequeue(CAT)

	def dequeue(self, ANIMAL_TYPE):
		if self.index[ANIMAL_TYPE][0] < 0:
			return None
		else:
			pet = self.animals[self.index[ANIMAL_TYPE][0]]
			self.animals[self.index[ANIMAL_TYPE][0]] = None
			if self.index[ANIMAL_TYPE][1] == self.index[ANIMAL_TYPE][0]:
				# last pet of this type
				self.index[ANIMAL_TYPE][1] -= 2
				self.index[ANIMAL_TYPE][0] -= 2
			else:
				self.index[ANIMAL_TYPE][0] += 2
			self.clean_queue()
			return pet

	def clean_queue(self):
		# check if the first two positions are None
		# and if yes, remove them
		if self.animals[0] is None and self.animals[1] is None:
			del self.animals[:2]
			for animal_key in self.index:
				self.index[animal_key][0] -= 2
				self.index[animal_key][1] -= 2

	def is_empty(self):
		return self.size() == 0

	def size(self):
		return len(self.animals)

	def print(self):
		for x in self.animals:
			print(x, end = " ")
		print()

def main():
	arr = ['CAT 1', 'CAT 2', 'DOG 1', 'CAT 3']
	pets = AnimalShelter()
	for i in arr:
		pets.enqueue(i, i.split()[0])
	pets.print()
	print(pets.dequeue_any())
	print(pets.dequeue_any())
	pets.print()
	print(pets.dequeue(DOG))
	print(pets.dequeue(CAT))
	pets.print()


if __name__ == "__main__":
	main()