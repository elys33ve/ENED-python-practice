#script which uses the quadratic formula to find x using the inputs of a, b, and c

import math

#inputs
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

#calculations (assuming d > 0)
d = b**2 - 4*a*c
x1 = (-b) + math.sqrt(d)
x2 = (-b) - math.sqrt(d)
D = 2*a
x1 = x1/D
x2 = x2/D

#outputs
print('Root 1 = {0}'.format(x1))
print('Root 2 = {0}'.format(x2))
