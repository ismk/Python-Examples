import math
def poly_peri(n, r):
	return ("{0:.3f}".format(2*n*r*math.sin(math.pi/n)))


print (poly_peri(5,3.7))


#! /usr/bin/env python

from math import sin,pi

side_num, circumradius = input().split()
side_num = int(side_num)
circumradius = float(circumradius)

perimeter = 2 * sin(pi / side_num) * circumradius * side_num

print("%.3f" % perimeter)