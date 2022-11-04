# Make function to merge 2 arrays

array1 = [0, 3, 4, 31]
array2 = [4, 6, 30]

# 1st way

def merge_func(arr1, arr2):
	arr1.extend(arr2)
	arr1.sort()
	return arr1


print(merge_func(array1,array2))

# 2nd way

array3 = [0, 3, 4, 31, 7]
array4 = [6, 30, 15, 22]

def merge_func2(arr1, arr2):
	new_arr = arr1 + arr2
	new_arr.sort()
	return new_arr

print(merge_func2(array3, array4))

# 3rd way (interview way) - arrays have to be sorted

array7 = [1, 2 , 3, 3, 5, 24, 35]
array8 = [2, 4, 5, 21, 26, 29]

def merge_loop_func(arr1, arr2):
	if len(arr1)==0 or len(arr2)==0:
		return arr1 + arr2
	mylist=[]
	i=0
	j=0
	while i<len(arr1) and j<len(arr2):

		if arr1[i]<=arr2[j]:
			mylist.append(arr1[i])
			i+=1

		elif arr2[j]<arr1[i]:
			mylist.append(arr2[j])
			j+=1

	return mylist+arr1[i:]+arr2[j:]
## OVO + se dodaje da bi rasporedilo sve preostale elementeeee!!!!
print(merge_loop_func(array7, array8))



