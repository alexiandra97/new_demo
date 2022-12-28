

def reverse_string(string):
	if len(string)<2:
		return string
	return reverse_string(string[string-1])

print(reverse_string('This is special day'))