'''

suitcase = []

suitcase.append("sunglasses")
suitcase.append("bag")
suitcase.insert(0, "hello")

temp = suitcase[0]

temp = temp[1:]

suitcase.insert(0,temp)

print (suitcase)

x = [1,2,3]

x.extend([4])

print (x)

'''




def fizz_count(x):
	count = 0
	for i in x:
		if (i == "fizz"):
			count = count + 1
	return count   

a = ["fizz","gizz","fizz"]

print (fizz_count(a))