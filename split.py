sent = "Here I am in Friday, come please"
another = "Rorararar daf fafq asf "

print(sent.split()[:1])
print(another.split()[:1])

list1= []

for i in range(10):
	if i % 2 == 0:
		list1.append(2)
	else:
		list1.append(1)


print(list1)

count1=0
count2=0
for i in range(len(list1)):
	if list1[i]==1:
		count1=count1+1
	else:
		count2=count2+1

print(count1)
print(count2)