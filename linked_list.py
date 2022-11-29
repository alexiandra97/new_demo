obj1 = {"a": True}
obj2 = obj1
del obj1
# print(1, obj1)
print(2, obj2)
# Python is garbage collected language. So we delete obj1 but reference stays

# 10 --> 15 --> 16

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			self.tail = self.head
		else:
			self.tail.next = new_node
			self.tail = new_node

	def printl(self):
		temp = self.head
		while temp != None:
			print(temp.data , end = ' ')
			temp = temp.next
			print()
			#print('Length = '+str(self.length))


linkedList = LinkedList()
linkedList.append(2)
linkedList.append(3)
linkedList.append(10)
print(linkedList.printl())