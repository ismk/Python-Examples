# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)


# print (factorial(5))


# def factorial(n):
# 	while n >= 1:
# 		num *= n
# 		n -= 1
# 		factorial(n)
# 	return num

# print (factorial(5))

n= 5
num = 1
for i in range(n-1):
	num *= n
	n -= 1

print (num)

def fact(num):
	total = 1
	while num != 0:
		total *= num
		num -= 1
	return total

print (fact(3))
