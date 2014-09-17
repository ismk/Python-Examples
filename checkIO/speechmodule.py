

def checkio(number):
	finaloutput =''
	unit_number = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
				5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
	tens = {2: 'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 
		8:'eighty', 9:'ninety'}

	teens = {0:'ten', 1:'eleven', 2:'twelve', 3:'thirteen', 4:'fourteen', 5:'fifteen', 6:'sixteen', 7:'seventeen', 
		8:'eighteen', 9:'nineteen'}

	newnum = str(number)

	if len(newnum) == 3:
		firstdigit = int (newnum[0])
		seconddigit = int(newnum[1])
		thirddigit = int(newnum[2])
		finaloutput = str(unit_number[firstdigit])
		finaloutput += " hundred"
		if seconddigit == 0 and thirddigit == 0:
			pass
		else:
			finaloutput += " "
			if seconddigit == 0:
				finaloutput += str(unit_number[thirddigit])
			elif seconddigit == 1:
				if thirddigit == 0:
					finaloutput += "ten"
				else:
					finaloutput += str(teens[thirddigit])
			else:
				finaloutput += str(tens[seconddigit])
				if thirddigit > 0:
					finaloutput += " "
					finaloutput += str(unit_number[thirddigit])

	if len(newnum) == 2:
		firstdigit = int (newnum[0])
		seconddigit = int(newnum[1])
		if firstdigit == 1:
			finaloutput += str(teens[seconddigit])
		else:
			if seconddigit == 0:
				finaloutput += str(tens[firstdigit])
			else:
				finaloutput = str(tens[firstdigit])
				finaloutput += " "
				finaloutput += str((unit_number[seconddigit]))


	if len(newnum) == 1:
		firstdigit = int (newnum[0])
		finaloutput = str(unit_number[firstdigit])
	return	finaloutput



print (checkio(302))



# def checkio(i):
#     if i < 20:
#         result = 'zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')[i]
#     elif i < 100:
#         result = ',,twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')[i//10]
#         if i % 10:
#             result += ' ' + checkio(i % 10)
#     elif i < 1000:
#         result = checkio(i // 100) + ' hundred'
#         if i % 100:
#             result += ' ' + checkio(i % 100)
#     return result



one = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
ten = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 
    18:"eighteen", 19:"nineteen"}
twenty = {0:"", 1:"ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
hundred = {0:"", 1:"one hundred", 2:"two hundred", 3:"three hundred", 4:"four hundred", 5:"five hundred", 6:"six hundred", 
    7:"seven hundred", 8:"eight hundred", 9:"nine hundred"}
     
numbers = [
    one,
    twenty,
    hundred
]
 
def checkio(input):
    input = str(input)
    result = ""
 
    length = len(input)
 
    if(length == 2 and input[0] == "1"):
        return ten[int(input)]
 
    current = length-1
    for i in range(length):
        if(current == 1 and input[i] == "1"):
            result += ten[int(input[current:])]
            break
        result += numbers[current][int(input[i])] + " "
        current -= 1
 
    split_result = result.split(" ")
    new_result = ""
    for el in split_result:
        if(el != ""):
            new_result += el+" "
 
    return new_result.strip()

print (checkio(1))