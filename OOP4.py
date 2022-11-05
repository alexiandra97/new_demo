# Object orientated programming (python)

class Person:
	# This is class atribute becuse it doen't have "self"
	number_of_people = 0

	def __init__(self, name):
		self.name = name
		Person.number_of_people+=1
# we can add it into __init__ and use like counter

		
# Deffine class method:
# add decorator to know it is class method
	@classmethod
	def number_of_people(cls):
		return cls.number_of_people



p1 = Person("Tommy")
print(Person.number_of_people)
p2 = Person("Aleks")
print(Person.number_of_people)


#print(Person.number_of_people)
#Person.number_of_people = 8
