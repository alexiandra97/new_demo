import time

def callAndSumNums(numbers):
	for i in range(len(numbers)):
		print(numbers[i])

	for i in range(len(numbers)):
		for j in range(len(numbers)):
			print(f"There is sum of nums: {numbers[i]+numbers[j]} ")


callAndSumNums([1, 2, 3, 4, 5])
# https://www.bigocheatsheet.com/