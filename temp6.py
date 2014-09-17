# myArray = [6, 3, 2, 1, 4, 7, 8, 3, 1, 3, 6, 8, 9, 3, 31]

# myArray.sort()

# print(myArray)

import math


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("CracklePop")
    elif i % 5 == 0:
        print("Crackle")
    elif i % 3 == 0:
        print("Pop")
    else:
        print(i)
