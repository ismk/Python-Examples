# A program to show my wife about programming
user_name = str(input("Hey there, what's your name?\n "))
print ("Hello {0}\n".format(user_name))

answ1 = str(input("How old are you?\n"))
print ("Don't worry I won't tell it to anyone!\n")

answ2 = str(input("Who is your favorite sister?\n "))
print ("All these secrets! I know, I know. Don't tell...\n")

answ3 = str(input("What is your phone number?\n" ))
print ("I don't recognize that area code....")


print ("""
So let's review.
Your name is {0} .
You are {1} years old.
Your favorite sister is {2} .
And your phone number is {3} .
...Oops, I blew your secrets!!!
""".format(user_name, answ1, answ2, answ3))