#calculates the heat transfer rate, using the inputs values

#constants
pr = 0.7
g = 9.81
v = 0.00001271
k = 0.25

#inputs
Th = float(input("Tempature of House (deg F): "))
Tinf = float(input("Tempature of Outside Air (deg F): "))
A = float(input("Surface Area of House (ft^2): "))
L = float(input("Height of House (ft): "))

#conversions
Th = (Th-32)*(5/9)+273.15       
Tinf = (Tinf-32)*(5/9)+273.15
A = A*0.092903
L = L*0.3048

#calculations
B = 1/Tinf
ra = (g*B*(Th-Tinf)*(L**3)*pr)/(v**2)
nu = 0.59*ra**(k)
h = (nu*(k))/L
Q = h*A*(Th-Tinf)

#output
print("The heat transfer rate is {0:.2f}W.".format(Q))







################# TRACE TABLE ####################
#           input:
#-------------------------------------------------
# Th            78
# Tinf          84
# A             2099
# L             20
#
#           output:
#-------------------------------------------------
# Q              -6349.79... -6349.79... i           
###################################################
