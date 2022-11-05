# Object orientated programming (python)

class Student:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def get_grade(self):
		return self.grade


class Course:
	def __init__(self, name, max_students):
		self.name = name 
		self.max_students = max_students
		self.students = []

	def add_students(self, student):
		if len(self.students) < self.max_students:
			self.students.append(student)
			return True
		else:
			return False
	def get_average_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()
		return value/len(self.students)


s1 = Student("Aleks" , 25, 70)
s2 = Student("Andra", 20, 80)
s3 = Student("Garry", 19, 75)

course = Course("Maths", 2)
course.add_students(s1)
course.add_students(s2)
course.add_students(s3)
print(course.students[1].name)
print(course.get_average_grade())