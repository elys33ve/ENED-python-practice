# This Python script allows a user to input initial velocity (v0) and angle
# increment (incr). It checks for valid inputs and calculates the max height
# and impact time, using a repetition structure. It then outputs the maximum
# height, impact time, corresponding angle.

import math

#constants
g = 9.81

#defults
v0 = -1
incr = -1
i = 0
theta = 0

#verify input validity
while not(v0 >= 0):
    v0 = float(input("Initial velocity:  "))

while incr >= 90 or incr <= 0:
    incr = float(input("Angle incriment:  "))

#convert units
incr_r = incr*(math.pi/180)     #radians
incr_d = incr                   #degrees

#repetition structure/calculate
def calc ():
    global theta
    global i
    while theta < 90:
        i = i+1
        theta = i*incr_d
        theta_r = theta*(math.pi/180)   #radians
        if theta > 90:
            break
        else:
            theta = int(theta)
        #max height
            max_h = (v0**2)*((math.sin(theta_r))**2)/(2*g)
        #impact time
            im_t = ((2*v0)*math.sin(theta_r))/g
        #outputs
            print(f"For angle {theta} deg; Max height = {max_h:.2f} m and impact time = {im_t:.2f} s") 

calc()
