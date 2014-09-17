def front_back(str):
	if len(str)<2:
		return	str
	else:
		frstchar = str[0]
		lastchar = str[len(str)-1]
		newstr = lastchar + str[1:len(str)-1] + frstchar 
		return newstr

print (front_back("START"))