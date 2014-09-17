def cat_dog(str):
	ccounter = 0
	dcounter = 0
	for i in range(len(str)-2):
		if str[i:i+3] == "cat":
			ccounter += 1
		elif str[i:i+3] == "dog":
			dcounter += 1

	return ccounter == dcounter



print (cat_dog('catdog'))
print (cat_dog('catcat'))
print (cat_dog('1cat1cadodog'))


word = "this is a word"
print (word[0:9])