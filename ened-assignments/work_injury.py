# Workplace Heat Related Injury (HRI) and Fall Related Injury (FRI) Indexes:
# This python script allows a user to unput; outside tempature (T), relative
# humidity (H), number of ladders (L), height of structure (h_struc), surface
# dryness (S_dry), and weather conditions (Wc). It will then calculate the
# threat of heat related injury (HRI) and fall related injury (FRI), outputting
# these values, along with the recommended action taken by the manager.

import sys

invalid = False

#str input lists
S_dryl = ['wet', '3', 'puddles', '2', 'dry', '0']
Wcl = ['sunny', '3', 'partly cloudy', '2', 'cloudy', '0']

#inputs
T = float(input("Outside tempature (F):  "))
H = float(input("Relative humidity:  "))
L = int(input("Number of ladders on site:  "))
h_struc = float(input("Height of structure (ft):  "))
S_dry = input("Surface dryness:  ")
Wc = input("Weather conditions:  ")

#test inputs
if T < -10 or T > 125:
    print("Invalid tempature")
    invalid = True
else:
    pass
if H > 1 or H < 0:
    print("Invalid humidity")
    invalid = True
else:
    pass
if L < 0:
    print("Invalid number of ladders")
    invalid = True
else:
    pass
if h_struc > 2800 or h_struc < 20:
    print("Invalid height")
    invalid = True
else:
    pass

#str inputs convert (dryness & weather)
S_dry = S_dry.lower()
Wc = Wc.lower()

if S_dry not in S_dryl:
    print("Invalid surface dryness")
    Invalid = True
elif S_dry == 'wet' or S_dry == '3':
    S_dry = 3
elif S_dry == 'puddles' or S_dry == '2':
    S_dry = 2
else:
    S_dry = 0

if Wc not in Wcl:
    print("Invalid weather conditions")
    invalid = True
elif Wc == 'sunny' or Wc == '3':
    Wc = 3
elif Wc == 'partly cloudy' or Wc == '2':
    Wc = 2
else:
    Wc = 0

#stop for invalids
if invalid == True:
    sys.exit()
else:
    pass

#determine HRI
HRI = 0.75*T + 5.0*Wc + H**2

#determine H_cat
if HRI > 75:
    H_cat = 1
else:
    H_cat = 0

#determine FRI
FRI = 0.2*L + 0.03*h_struc + 30*H_cat + 10*S_dry

#manager action
Mh_act = "x"
Mf_act = "x"

if H_cat == 1:
    Mh_act = "Allow 1 extra break"
else:
    pass
if FRI > 100:
    Mf_act = "Hold safelty session"
else:
    pass
if Mh_act == "x" and Mf_act == "x":
    M_act = "Safety is Job #1"
elif Mh_act != "x" and Mf_act == "x":
    M_act = Mh_act
elif Mh_act == "x" and Mf_act != "x":
    M_act = Mf_act
else:
    M_act = Mh_act + " and " + Mf_act.lower()

#outputs
print(f"Heat related injury (HRI): {HRI:.1f}")
print(f"Fall related injury (FRI): {FRI:.1f}")
print(f"Manager action: {M_act}")
