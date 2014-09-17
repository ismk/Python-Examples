string = "75Number9"
numArr = []
newstr = list(string)
i = (len(newstr)-2)
while i > 0:
	if newstr[i].isdigit() and newstr[i+1].isdigit():
		print newstr[i]
		print newstr[i+1]	
		numArr.append(int(newstr[i]+newstr[i+1]))
		i += 1
	elif newstr[i].isdigit():
		numArr.append(int(newstr[i]))
	i -= 1
print(numArr)
total = sum(numArr)
print (total)