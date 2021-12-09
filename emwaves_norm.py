# This Python script reqires a user to input amplitude of incident wave (Ei0),
# permittivity (Er1, Er2), and permeability of mediums (ur1, ur2). It will
# compute the intrinsic impedences (n1, n2), and amplitudes of the
# reflected and transmitted waves (Et0, Er0).

#inputs
Er1 = float(input("Relative permittivity of medium 1:   "))
ur1 = float(input("Relative permeability of medium 1:   "))
Er2 = float(input("Relative permittivity of medium 2:   "))
ur2 = float(input("Relative permeability of medium 2:   "))
Ei0 = float(input("Amplitude of incident waves (V/m):   "))

#calculations
n1 = 377.14*(ur1/Er1)**(1/2)
n2 = 377.14*(ur2/Er2)**(1/2)
Et0 = ((2*n2)/(n1+n2))*Ei0
Er0 = ((n2-n1)/(n2+n1))*Ei0

#outputs
print(f"Intrinsic impedence of medium 1: {n1:.2f} Ohms") 
print(f"Intrinsic impedence of medium 2: {n2:.2f} Ohms") 
print(f"Amplidude of reflected waves: {Er0:.2f} V/m")
print(f"Amplitude of transmitted waves: {Et0:.2f} V/m")
