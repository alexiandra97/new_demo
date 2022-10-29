import time

large1 = ['nemo' for i in range(100)]
large2 = ['nemo' for i in range(1000)]

def findNemo(array1, array2):
	t0 = time.time()
	for i in range(0,len(array1)):
		if array1[i] == 'nemo':
			print("found nemo")
	t1 = time.time()
	print(f'It tooks: {t1-t0}')

	t0 = time.time()
	for i in range(0, len(array2)):
		if array2[i] =='nemo':
			print("found nemo")
	t1=time.time()
	print(f"It tooks: {t1-t0}")

findNemo(large1, large2)

# O(m+n) - because we have 2 inputs