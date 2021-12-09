#calculates the Reynold's number using the given inputs for fluid density, dynamic viscosity, length, and velocity

#inputs
p = float(input("Fluid Density (lb/in^3): "))
u = float(input("Dynamic Viscosity of Fluid (lb/(in*s)): "))
L = float(input("Typical Length (in): "))
V = float(input("Fluid Velocity (mi/hr): "))

#conversions
V = V*0.44704
L = L*0.0254
u = u*17.8579673
p = p*27679.9

#mathy part
re = (p*V*L)/u

#output
print("The Reynold's Number is {0:.2f}.".format(re))
