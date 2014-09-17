'''

prices = {"banana":4, "apple":2, "orange":1.5, "pear":3}

prices["Watermelon"] = "5"

print (prices)

#---------------------------------------------------------------------------------

n = [1, 3, 5,5,3,2,5,8,6,4,2,1,4,6,8]
# Remove the first item in the list here
print (n)
n.remove(5)
print (n)
del(n[0])
print (n)
n.pop(1)

print (n)

#---------------------------------------------------------------------------------

def add_funct(*args):
	return sum(args)

print (add_funct(123,4531,234,451,234435,123,435,234,45,123))

#---------------------------------------------------------------------------------

'''

n = "Hello"
# Your function here!
def string_function(s):
    return s + ' World!'


print (string_function(n))

'''

#---------------------------------------------------------------------------------

def list_function(x):
    return x

n = [3, 5, 7]
print (list_function(n))

#---------------------------------------------------------------------------------

def list_function(x):
    x[1] = x[1] +3
    return x

n = [3, 5, 7]
print (list_function(n))

#---------------------------------------------------------------------------------

n = [3, 5, 7]

for i in range(0, len(n)):
    print (n[i])

#---------------------------------------------------------------------------------

def print_list(x):
    for i in range(0, len(x)):
    	print (x[i])

print_list(n)


n = [3, 5, 7]


# Don't forget to return your new list!

def double_list(x):
	for i in range(0, len(x)):
		x[i] = x[i] * 2
	return x


print (double_list(n))



def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print (my_function([1,2,3])) # Add your range between the parentheses!


def funct(*args):
	for i in range(0,5):
		print (args)

funct(1,2,3)

#---------------------------------------------------------------------------------

n = [3, 5, 7]

count = n[0] + n[1] + n[2]

print (count)

print (sum(n))

def total(x):
	lstsum = 0
	for i in range(0,len(x)):
		lstsum += x[i]
	return lstsum
print (total(n))

#---------------------------------------------------------------------------------

n = ["Michael", "Lieberman"]
# Add your function here

def join_strings(x):
	totalstr = ""
	for i in range(0,len(x)):
		totalstr += x[i]
	return totalstr


print (join_strings(n))

#---------------------------------------------------------------------------------

m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
print (m+n)


def join_list(x,y):
	z =[]
	for i in range(0,len(x)):
		z= x + y
	return z

print (join_list(m,n))


#---------------------------------------------------------------------------------

m = [1,2,3]
n = [4,5,6]
o = [7,8,9]

def join_lists(*args):
    s = []
    for i in args:
        s += i
    return s

print (join_lists(m,n,o))   # [1, 2, 3, 4, 5, 6, 7, 8, 9] This is concatenating.

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(x):
    z = []
    for i in range(len(x)):
        z += x[i]
    return z



print (flatten(n))

#---------------------------------------------------------------------------------

from random import randrange

random_number = randrange(1, 10)
print(random_number)

count = 0
# Start your game!
guess = int(input("Enter a guess:"))

while(guess != random_number):
    guess = int(input("Nope Enter again\n"))
    if(count == 0):
        print("Sorry you lose")
        break
    count += 1
    print (count)
else:
    print("You Win")


#---------------------------------------------------------------------------------

hobbies = []

# Add your code below!

for i in range(3):
    hobby = input("Tell me a hobby of yours")
    hobbies.append(hobby)

print (hobbies)

#---------------------------------------------------------------------------------

xyz = 498.500

def is_int(x):
	if isinstance(x,int):
		return True
	else:
		newint = str(x)
		print (newint)
		print (newint[-1])
		if (newint[-1] == "0"):
			return True
		else:
			return False
print (is_int(xyz))

#---------------------------------------------------------------------------------

def digit_sum(n):
	if((not(isinstance(n,int))) or (n < 0)):
		print ("Can't be negative or a float type")
	else:
		nn = str(n)
		sum=0
		for i in nn:
			sum += int(i)
		return sum

x = 1234

print (digit_sum(x))

#---------------------------------------------------------------------------------

def factorial(x):
	if((not(isinstance(x,int))) or (x < 0)):
		print ("Can't be negative or a float type")
	else:
		nn = str(x)
		total=1
		for i in range(0,x):
			total *= int(x)
			x -=1
			print (x)
		return total

print (factorial(10))

#---------------------------------------------------------------------------------

def prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2,x):
        	print (i)
        	if x % i == 0:
        		return False
    return True


print (prime(21))

#---------------------------------------------------------------------------------

def reverse(text):
	st1 = []
	st1 = list(text)
	st2 = []
	st3 = []
	for i in range(0,(len(st1))):
		st2 = st1.pop(len(st1)-1)
		st3.append(st2)
	st4 = ''.join(st3)
	return st4

print (reverse("hello"))

#---------------------------------------------------------------------------------

str1  = "hey there you"

vowels = "aeiou"

result =""

for i in str1:
	if i not in vowels:
		result +=i
print (result)



score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

word = "helix"


def scrabble_score(word):
	wrdlw = word.lower()
	x=0
	for i in wrdlw:
		if i in score:
			x += score[i]
	return x

print (scrabble_score(word))


#---------------------------------------------------------------------------------



def censor(text,word):

	newword = ""
	for x in word:
		newword += "*"

	newlst = text.split()
	finallst = ""

	for i in newlst:
		if word in i:
			i = newword
		finallst += i

	return " ".join(finallst)

text = "i dont know where i will get this tool"
word = "tool"

#print (censor(text,word))


def censor(text, word):
           return text.replace(word, ("*"*len(word)))

print (censor(text,word))

#---------------------------------------------------------------------------------

mylist = [1,1,2,23,4,1,21,23,34,453,1,213,342,4534,23]

myint = 1

def count(alist,aint):
	total = 0
	for i in alist:
		if i == aint:
			total += 1
	return total

print (count(mylist,myint))


#---------------------------------------------------------------------------------

thelist = [1,2,3,4,5,6,7,8,9,10]

def purify(thelist):
	finallist = []
	for i in thelist:
			if i % 2 == 0:

				finallist.append(i)
	return finallist

print (purify(thelist))

#---------------------------------------------------------------------------------


def product(args):
	total = 1
	for i in args:
		total *= i
	return total

print (product([1,4,5,5]))


#---------------------------------------------------------------------------------


def remove_duplicates(thelist):
	newlist = []
	for i in thelist:
		if i not in newlist:
			 newlist.append(i)
	return newlist

print (remove_duplicates([1,1,1,2,2,2,2]))

a = [1,2,3,4]
b = [2,3,7]

print (any(True for x in a if x in b))

#---------------------------------------------------------------------------------



def median(thelist):
	finallist = sorted(thelist)
	print (finallist)

	if len(finallist) % 2 == 0:
		i = int((len(finallist) / 2))
		x1 = finallist[i]
		x2 = finallist[i-1]
		print (x1,x2)
		finalx = (x1+x2) / 2.0
		return finalx
	else:
		n = int((len(finallist)-1) / 2)
		return finallist[n]


a = [1, 34, 1, 6, 8, 0]

print (median(a))

def median(lst):
    s = sorted(lst)
    l = int (len(lst)/2)
    if len(lst)%2 == 0:
        return (s[l] + s[l-1])/2.0
    else:
        return s[l]

print (median(a))

#---------------------------------------------------------------------------------




import math

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print (grade)

def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

def grades_variance(scores,average):
	variance = 0
	for i in range(len(scores)):
		temp = (average - scores[i]) ** 2
		variance += temp
	fv = variance / len(scores)
	return fv

finalv =  (grades_variance(grades,grades_average(grades)))

def grades_std_deviation(variance):
	dev = math.sqrt(variance)
	return dev

print (grades_std_deviation(finalv))



#---------------------------------------------------------------------------------


my_dict = {"Name":"Sarah","Age":20,"Single":True}

print (my_dict.items())

for i in my_dict:
	print (i,my_dict[i])

print ("\n")

print ({x: x**2 for x in (2, 4, 6)})



#---------------------------------------------------------------------------------


to_21 = list(range(1,21))

odds  = to_21[::2]

print (odds)

middle_third = to_21[8:14]

print (middle_third)

#---------------------------------------------------------------------------------



languages = ["HTML", "JavaScript", "Python", "Ruby"]

print (filter(lambda i: i == "Python", languages))




#---------------------------------------------------------------------------------




squares = [x**2 for x in range(1,10)]

print (filter(lambda i: i>29 and i<69, squares))




#---------------------------------------------------------------------------------


movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}

print (movies.items())

#---------------------------------------------------------------------------------


threes_and_fives = [i for i in range(1,16) if i % 3 ==0 or i %5==0]

print (threes_and_fives)

#---------------------------------------------------------------------------------





garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = list (filter(lambda i:i!='X',garbled))

print (''.join(message))

def anumber(int a){


}



#---------------------------------------------------------------------------------


# Class definition
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    def hunger(self):
        if self.is_hungry:
            print("%s is hunrgy!" %(self.name))
        else:
            print("%s is not Hunrgy!" %(self.name))
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)


zebra.hunger()
giraffe.hunger()
panda.hunger()

class Animal(object):
	"""Makes cute animals."""
	is_alive = True
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def description(self):
		print ("Name of the Animal is %s, and its age is %s" %(self.name,self.age))



hippo = Animal("Blender",20)
hippo.description()


#---------------------------------------------------------------------------------




class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)



milton = PartTimeEmployee("Milton")
print (milton.full_time_wage(10))

#---------------------------------------------------------------------------------



class Triangle(object):

    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if((self.angle1 + self.angle2 + self.angle3) == 180):
            return True
        else:
            return False

class Equilateral(Triangle):
	angle = 60
	def __init__(self):
		self.angle = self.angle1
		self.angle = self.angle2
		self.angle = self.angle3




my_triangle = Triangle(60,30,90)
print (my_triangle.number_of_sides)
print (my_triangle.check_angles())


#---------------------------------------------------------------------------------



class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def display_car(self):
    	return ("This is a %s %s with %r MPG." %(self.color, self.model, self.mpg))

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):
	def __init__(self,battery_type,model,color,mpg):
		self.battery_type = battery_type
		self.model = model
		self.color = color
		self.mpg = mpg

my_car = ElectricCar("molten salt", "DeLorean", "silver", 88)
print (my_car.display_car())

#---------------------------------------------------------------------------------



class Point3D(object):
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def __repr__(self):
		return (self.x, self.y, self.z)


my_point = Point3D(1,2,3)


#---------------------------------------------------------------------------------



f = open ("C:/test.txt", 'r+')

f.write("Hello World!")

# f.close()

f = open ("C:/test.txt", 'r+')
print (f.read())

#---------------------------------------------------------------------------------

'''