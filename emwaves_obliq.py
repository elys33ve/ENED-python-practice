# This Python script requires the user to input values for amplitude of the
# incident wave (Ei0),intrinsic impedences (n1, n2), and phase constants
# (B1, B2). It uses the Brewster Angle, Snell's Law, and the given equations
# (4) and (5) to compute the amplitudes of reflected and transmitted waves
# for oblique incidence, and the reflected, transmitted, and incident angles.

import math as m

#inputs
n1 = float(input("Intrinsic impedance of material 1:   "))
B1 = float(input("Phase constant of material 1:   "))
n2 = float(input("Intrinsic impedance of material 2:   "))
B2 = float(input("Phase constant of material 2:   "))
Ei0 = float(input("Amplitude of the incident wave (V/m):   "))

#mathy stuff
tBA = m.asin(m.sqrt(((B2**2)*((n2**2)-(n1**2)))/(((n2**2)*(B1**2))-((n1**2)*(B2**2)))))  #Brewster angle (m^(-1))
Ti = tBA
Tr = tBA
Tt = m.acos((n1*(m.cos(tBA)))/n2)
Er0 = (((n2*m.cos(Ti))-(n1*m.cos(Tt)))/((n2*m.cos(Ti))+(n1*m.cos(Tt))))*Ei0
Et0 = (2*n2*m.cos(Ti))/((n2*m.cos(Tt))+(n1*m.cos(Ti)))*Ei0

#convert to degrees
Ti = tBA*(180/m.pi)
Tr = tBA*(180/m.pi)
Tt = Tt*(180/m.pi)

#outputs
print(f"Incident Angle: {Ti:.2f} degrees")
print(f"Reflected Angle: {Tr:.2f} degrees")
print(f"Transmitted Angle: {Tt:.2f} degrees")
print(f"Reflected Amplitude: {Er0:.2f} V/m")
print(f"Transmitted Amplitude: {Et0:.2f} V/m")
