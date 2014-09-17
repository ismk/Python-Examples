import random

number = random.randint(1,100)

counter = 0
guess = int(input("Guess a number between 1 and 100\n"))

while(guess!=number):
	if (guess<number):
		print ("try going higher")
		guess = int(input())
		counter +=1
	elif (guess>number):
		print("no no too high go lower")
		guess = int(input())
		counter += 1

print("there you go!\nand it only took you",counter,"tries")