# 1st way

def reverse_string(string):
	return string[::-1]

s1 = "Ovo je najkraca recenica u svemiru!!"
s2 = "ovo je druga najkraca recenica na svetu"
s3 = 43523523523

print(reverse_string(s1))


# 2nd way

def reverse_string_loop(string):
	if string == str :
		rev_list = []
		for i in range(len(string)-1, -1, -1):
			rev_list.append(string[i])
		new_string = ''.join(rev_list)
		return new_string
	else:
		print("Uneta vrednost nije string")
	

print(reverse_string_loop(s1))
print(reverse_string_loop(s2))
print(reverse_string_loop(s3))
