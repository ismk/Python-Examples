def fibonacci(getn):
	n = 1
	fib = []
	for i in range(getn):
		fib.append(n)
		n += fib[i-1]
	return str(fib).strip('[]')


getn = int (input("Enter Number of fibonacci Numbers you want \n"))

print (fibonacci(90))

