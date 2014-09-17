counter = 0
usrstr = input("Enter a string\n")
thechar = input("Enter the character you want to see the number of times it has been repeated in that sentence\n")

for i in range(0,len(usrstr)):
	if (usrstr[i] == thechar):
		counter = counter+1

print("The number of "+thechar+" is "+str(counter))
