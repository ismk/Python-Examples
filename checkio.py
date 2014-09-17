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