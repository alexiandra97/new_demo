import time

stuff_list = ["nemo", "love", "sprint", "nemo", "nemo"]
all_chars = ["nemo", "dori", "crabs", "fishes", "sharks", "people", "kids", "snail", "turtles", "more turtles", "more more turtles"]
large = ["nemo" for i in range(100)]

def findNemo(array):
	t1 = time.time()
	for i in array:
		if i=='nemo':
			print('finding Nemo')
	t2 = time.time()
	print("time: t2-t1 is:", t2-t1)

print(large)
