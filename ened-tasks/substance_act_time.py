# user inputs the activity and half life of substance. The script outputs the
# activity of the substance at corresponding times.

#imports
import math
import sys

#inputs
T_h = float(input("half-life:  "))
A0 = float(input("activity (Bq):  "))

#constant (based on input)
wl = (0.693/T_h)

#test inputs
if T_h <= 0 or A0 <= 0:
    print("invalid input")
    sys.exit()
else:
    pass

#loop & output values
for i in range(1,17):
    i = i/4
    t = i*T_h
    A = A0*math.exp((-wl)*t)
    print(f"Activity = {A} at time = {t}")
