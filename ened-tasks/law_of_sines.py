#script which calculates the unknown angle and side lengths for a triangle, using the inputted side length and angles

import math

#inputs
A = float(input('Angle A = '))
B = float(input('Angle B = '))
a = float(input('Side a = '))

#calculations
b = a*math.sin(B*math.pi/180)/math.sin(A*math.pi/180)
C = 180 - A - B
c = a*math.sin(C*math.pi/180)/math.sin(A*math.pi/180)

#outputs
print('Angle C = {0}'.format(C))
print('Side b = {0}'.format(b))
print('Side c = {0}'.format(c)) 
