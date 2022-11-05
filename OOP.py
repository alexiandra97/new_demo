# Object orientated programming (python)

print(type("Word"))

x = 3
print(type(x))

def hello():
	print("hello")

print(type(hello))

print("Word".upper())
# methods are connected with certain objects
# print(x.upper()) - It can't work! Because class 'int' doesn't have method '.upper()'

# Make a class

class Dog:
	# create special method that'll be called everytime when we instance class
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def set_age(self, age):
		self.age = age
	
	def bark(self):
		print("bark")
	
	def meow(self):
		return "meow"
	
	def add_one(self, x):
		return x + 1

# Instatiating 
d = Dog("John", 5) 
print(type(d))
d.bark()
print(d.meow())
print(d.add_one(9))


dog1 = Dog("Aleks", 7)
print(dog1.name)
print(dog1.get_name())
print(dog1.get_age())

dog1.set_age(10)
print(dog1.get_age())