
# Test excercise for reguar expressions!!! ####


# import re
# print (re.search('[abc]', "Ismail"))
# print (re.sub("[abc]", "o", "Ismail"))
# numbers = [1,2,3,4,5,6,7,8,9]
# num = "12345"
# if num[0] in numbers:
# 	print("Yay!")
# else:
# 	print ("Nay!")
# alist = [2,9,5,4,8,1,6]
# for i in range(len(alist)-1):
# 	currentMin = alist[i]
# 	currentMinIndex = i
# 	j = i+1
# 	for j in range(len(alist)):
# 		if(currentMin > alist[j]):
# 			currentMin = alist[j]
# 			currentMinIndex = j
# 	if(currentMinIndex != i):
# 		alist[currentMinIndex] = alist[i]
# 		alist[i] = currentMin
# print (alist)

# f = open("C:/titles.txt", "r")
# fw = open("C:/titles2.txt", "w+")

# n=11
# for i in f:
#     fw.write(str(n)+i[2:])
#     n = n + 1

# f.close()
# fw.close()


# str = "O draconia;conian devil! Oh la;h lame sa;saint!"
# temp = str.split(';')

# new_list = []
# new_list = set(list(temp[0])).intersection(set(list(temp[1])))
# print (new_list)


# a = set("abcdeol")
# b = set("krtol")
# c = set("hflsfjg")
# if a.intersection(b):
# 	print("hello")


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


my_triangle = Triangle(60, 30, 90)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())
