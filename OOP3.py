# Python Inheritance

class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old.")
	def speak(self):
		print("idk what to say")

# so we define new class (child class) and then in brackts we put name of mother class, methods will be overwritten in childs' classes
class Cat(Pet):
	def __init__(self, name, age, color):
		super().__init__(name, age)
		# Pet.__init__(self, name, age)
		self.color = color
# but when we need to add more features (ex. color) just in child class we make __init__ method in child class and add just new features,
# old we get : super().__init__() that takes things from parent's class
	def speak(self):
		print("meow")
	def show(self):
		print(f"My name is {self.name}, I am {self.age} and I am {self.color}")

class Dog(Pet):
	def speak(self):
		print("bark")

class Fish(Pet):
	pass


p = Pet("Tim", 2)
p.show()
c = Cat("Mich", 3, "black")
c.show()
d = Dog("Ema", 10)
d.show()
d.speak()
c.speak()

f = Fish("Nemo", 1)
f.speak()