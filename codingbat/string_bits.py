def string_bits(str):
	n = 0
	result = ''
	for i in range(len(str)):
		while n < (len(str)):
			result += str[n]
			n += 2
	return result

print (string_bits("hxaxpxpxy"))