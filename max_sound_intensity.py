#calculates the max allowable sound intensity using the inputs for max SPL, reference pressure, and particle velocity

#inputs
mspl = float(input("Max allowable SPL (dB): "))
rp = float(input("Reference pressure (Pa): "))
pv = float(input("Particle Velocity (m/s): "))

#math
p = 10**(mspl/20)*rp
i = p*pv

#outputs
print("The max allowable sound intensity is {0:.2f} W/m^3.".format(i))
