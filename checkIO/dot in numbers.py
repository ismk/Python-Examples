a = '123456'
b = '333'
c = '9999999'
d = '123456 567890'
e = 'price is 5799'
f = 'he was born in 1966th'

# ordrinalist = ["0th", "1st", "2nd", "3rd", "4th", "5th", "6th", "8th", "9th"]
# print (ordrinalist)
# tobedotted = str(f)

# print (tobedotted)

# if tobedotted in ordrinalist:
# 	print (True)
# else:
# 	print (False)


num = ''
astr = str(a)


if(len(astr) > 3):
    index = 3
    astr[:index] + '.' + astr[index:]
