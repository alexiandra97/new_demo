#array = [{"tweet":'hi', "date": 2012},{"tweet":'my', "date": 2013},{"tweet": 'now', "date": 2014},{"tweet": 'wait', "date": 2015}]

#print(len('dsdasffjjjjjSfs'))

#print(array[0].values())
import time
array1 = ['x', 'z', 'd']
array2 = ['w', 'd' , 'r']


t00 =  time.time()
def isSame(array1, array2):
	for i in range(len(array1)):
		for j in range(len(array2)):
			if array1[i]==array2[j]:
				print("True")
isSame(array1,array2)

t01 = time.time()
t1 = t01 - t00
print(t1)
# O(n*m) so slowly
# But it has O(1) space complexity

# Another solution: we have to array1 convert to an object/dictionary
# and then check if it is in array2

def anotherSolution(array1, array2):
	arrDict = dict()
	for i in range(len(array1)):
		arrDict[array1[i]] = True
	for i in range(len(array2)):
		if array2[i] in arrDict:
			return True
	return False

print(anotherSolution(array1, array2))   

# O(a+b) => because we have two inputs!
# O(a) - space complexity
# Prevent error made by inputs
# This code can't work if input contains list into array, or we use just one array

def thirdSolution(array1, array2):
    try:
        dictionary = dict()
        for i in range(len(array1)):
            if array1[i] not in dictionary:
                dictionary[array1[i]] = True

        for i in range(len(array2)):
            if array2[i] in dictionary:
                return True
        return False

    except TypeError:
        print("Exactly two arrays required.")

print(thirdSolution(array1))
		