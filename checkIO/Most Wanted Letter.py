import string


a = "Hello World!"
b = "How do you do?"
c = "One"
d = "Heloowasssss????!?!?!??!???"
e = "HelEEEEEEEEEEEEEEEsssssss"



# def checkio(text):
# 	newlist = list(text.lower())
# 	count = {}
# 	for s in newlist:
# 		if s.isalpha():
# 			if s in count:
# 				count[s] += 1
# 			else:
# 				count[s] = 1
# 	print (count)

# def checkio(text):
#     text = text.lower()
#     return min([(-1 * text.count(ch), ch) for ch in string.ascii_lowercase])[1]

# print (checkio("Lorem ipsum dolor sit amet"))



def checkio(data):
    '''Function is returning the most frequent letter in the text'''
 
    low_data = data.lower()
    uniq_chars = sorted(set(low_data))
    n = 0
 
    for c in uniq_chars:
        if c.isalpha():
            if low_data.count(c) > n:
                letter = c
                n = low_data.count(c)
    return(letter)

print (checkio(a))