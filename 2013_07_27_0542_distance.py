'''
def distance_from_zero(x):
    if((type(x) == int) or (type(x) == float)):
        return abs(x)
        print abs(x)
    else:
        return "Not an integer or float!"

distance_from_zero(123.4)
'''
x=0
def distance_from_zero(x):
    if isinstance(x, (int, float)):
        return abs(x)
    else:
        return "Not an integer or float!"

blah = input("Enter")
_return = distance_from_zero(blah)

print (_return)

