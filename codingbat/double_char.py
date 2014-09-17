def double_char(str):
	result = ''
	endresult = ''
	for i in range(len(str)):
		result = str[i]+str[i]
		endresult += result
	return (endresult)





print (double_char('The'))
print (double_char('AAbb'))
print (double_char('Hi-There'))