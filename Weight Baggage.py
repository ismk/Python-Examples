weight = int(input("How many pounds does your suitcase weigh? "))
   
if weight > 50:
    print("There is a $25 charge for luggage that heavy.")
    print('Is that OK ? Please press Y for yes or N for no')

    answer = str(input())
    word = answer[0]
    word = word.lower()

    if (word == "y"):
    	print("Thank you")
    elif (word == "n"):
    	print("fine asshole")
    else:
        print ("What the fuck ?! Cant answer a simple YES or a FUCKING NO question?!")

else: 
	print("Thank you for your business.")


def _checkweight(_weight):
    pass


