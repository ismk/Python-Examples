lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

theclass = [lloyd,alice,tyler]

# Add your function below!

def average(lst):
	total = 0
	if (lst != 0):
		for  i in lst:
			total += i
	avg = total / len(lst)
	return avg

def get_average(student):
	avghw = average (student["homework"])
	avgquiz = average(student["quizzes"])
	avgtest = average(student["tests"])
	subtotal = (avghw*0.1) + (avgquiz*0.3) + (avgtest*0.6)

	return subtotal

def get_letter_grade(score):
	if(score >= 90):
		return "A"
	elif(score >=80):
		return "B"
	elif(score >=70):
		return "C"
	elif(score >=60):
		return "D"
	else:
		return "F"

def get_class_average(tclass):
	subtotalclass = 0.0
	for i in tclass:
		totclassavg = get_average(i)
		subtotalclass +=totclassavg
	finalclassvag = subtotalclass / len(tclass)
	return finalclassvag



classavg = get_class_average(theclass)
print (classavg)
print (get_letter_grade(classavg))
