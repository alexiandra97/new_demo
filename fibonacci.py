def fibonacciiter(n):
	lista=[0,1]
	f=0
	for i in range(1,n):
		f = lista[i]+lista[i-1]
		lista.append(f)
	for i in lista:
		if lista[n]==i:
			return i
			
def fibonaccieiter2(n):
	list2=[0,1]
	for i in range(2,n+1):
		list2.append(list2[i-2]+list2[i-1])
	return list2[n]

def fibonaccirecursive(n):
	if n<2:
		return n
	return fibonaccirecursive(n-1)+fibonaccirecursive(n-2)
	#O(2^n)
	

print(fibonaccieiter2(19))
print(fibonacciiter(19))
print(fibonaccirecursive(19))
