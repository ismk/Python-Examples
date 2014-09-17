a = 'A1213pokl'
b = 'bAse730onE'
c = 'asasasasasasasaas'
d = 'QWERTYqwerty'
e = '123456123456'
f = 'QwErTy911poqqqq'

#---------------My Solution-----------------#
def checkio(password):
	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = lower.upper()
	boollower = False
	boolupper = False
	boolnum   = False
	if len(password) >= 10 :
		for i in password:
			if (i in lower): 
				boollower = True
			elif (i in upper):
				boolupper = True
			elif i.isdigit():
				boolnum = True
			else:
				return (False)
		if boollower and boolupper and boolnum:
			return (True)
		else:
			return (False)
	else:
		return ("Password not long enough")

print (checkio(f))



#---------------Best Solution-----------------#
def checkio(data):
    'Return True if password strong and False if not'
    num = False
    upper = False
    lower = False
    for i in range(len(data)):
        num = num or data[i].isnumeric()
        upper = upper or data[i].isupper()
        lower = lower or data[i].islower()
         
    return num and upper and lower and len(data)>=10
print (checkio(f))



def checkio(data):
    return (len(data) >= 10 and
            any([ch.isupper() for ch in data]) and
            any([ch.isdigit() for ch in data]) and
            any([ch.islower() for ch in data]))


# I used lookaheads (see here http://www.regular-expressions.info/lookaround.html) , the whole regex is wrapped in ^& indicating the start and the end, it starts with looking for any character zero or more times .* and then the parts you see in the parenthesis are lookaheads, it will match the given regex inside it, but won't make it part of the match, it's just an assertion whether the characters are found or not, so you see 3 assertions of that kind, one looking for digits, one for small letters and one for big letters. It ends with the {10,} meaning the whole string can be 10 or more characters long

import re
 
def checkio(data):
    'Return True if password strong and False if not'
    return bool(re.match(r'^.*(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{10,}$', data))

print (checkio(f))


def checkio(data):
    'Return True if password strong and False if not'
    if len(data) < 10 or data == data.lower() or data == data.upper() or sum(i.isdigit() for i in data) == 0 :
        return False
    return True



import re
def checkio(data):
    'Return True if password strong and False if not'
    return len(data) >= 10 and all(re.search(p, data) != None for p in ("[a-z]", "[A-Z]", "[0-9]"))