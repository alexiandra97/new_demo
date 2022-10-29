import math



boxes = [1, 2, 3, 4, 5]
print(boxes[0])

def logAllpairs(array):
	for i in range(1, len(array)):
		for j in range(1, len(array)):
			print(math.log(array[j], array[i]))
			

#boxes2=[]

#for i in boxes:
#	a = math.log(i, i+1)
#	boxes2.append(a)

#print(boxes2)

logAllpairs(boxes)


# It's O(n^2), if we had had 2 inputs it would be O(n*m)