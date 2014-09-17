def string_match(a, b):
	count = 0
	if len(a) > len(b):
		length = len(a)
	else:
		length = len(b)
	for i in range(length-2):
		if a[i] == b[i] and a[i+1] == b[i+1]:
			count += 1
	return count

print (string_match('xxcaazz', 'xxbaaz'))
