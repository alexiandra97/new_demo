# Object orientated programming (python)

# when we have a lot of function we can organize them into class

class Math:
	#make unchanging method (static method)
	@staticmethod
	def add5(x):
		return x + 5

	@staticmethod
	def add10(x):
		return x + 10

	@staticmethod
	def add3(x):
		return x+3


# we don't have to have instance of the class
print(Math.add5(99))
print(Math.add10(4))
print(Math.add3(1))
print(Math.add(2))
