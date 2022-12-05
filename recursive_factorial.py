def rec_fact(number):
	if number==2:
		return 2
	return number*rec_fact(number-1)


def iter_fact(number):
	fact =1
	for i in range(number,1,-1):
		fact = fact*i 
	return fact


print(iter_fact(50))
print(rec_fact(50))