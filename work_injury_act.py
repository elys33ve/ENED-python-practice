# This python script allows a user to input values for tempature (T), humidity
# (H), and weather condition (Wc). It then determines and outputs the action
# that should be taken by the manager.

import sys

invalid = False

#str input list
Wc_l = ['sunny', 's', 'cloudy', 'c', 'raining', 'r']

#inputs
T = float(input("Outside tempature (F):  "))
H = float(input("Relative humidity:  "))
Wc = input("Weather Condition:  ")

#test inputs
Wc = Wc.lower()

if T < -10 or T > 125:
    print(f"Invalid tempature\n{T}")
    invalid = True 
else:
    pass
if H > 1 or H < 0:
    print(f"Invalid humidity\n{H}")
    invalid = True
else:
    pass
if Wc not in Wc_l:
    print(f"Invalid weather condition\n{Wc}")
    invalid = True
else:
    if Wc == 'sunny' or Wc == 's':
        Wc = 1
    elif Wc == 'cloudy' or Wc == 'c':
        Wc = 2
    else:
        Wc = 3

#stop if invalid
if invalid == True:
    sys.exit()
else:
    pass

#main conditionals + outputs
if Wc == 3:    
    print("Work inside")
elif T >= 90:
    if H > 0.8 and Wc == 1:
        print("Two 15 minute breaks")
    elif H > 0.9 and Wc == 2:
        print("One 15 minute break")
    else:
        print("One 10 minute break")
elif T in range (81,90):
    if H > 0.9 and Wc == 1:
        print("Two 10 minute breaks")
    elif H > 0.9 or Wc == 1:
        print("One 10 minute break")
    else:
        print("No extra breaks")
else:
    print("No extra breaks")
