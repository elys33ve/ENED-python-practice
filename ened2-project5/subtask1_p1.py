#!/usr/bin/env python3

# Move forward a given distance and move backwards to original position 
# for a given number of laps.
##################################################
import math as m
from time import sleep

from ev3dev2.motor import OUTPUT_B, OUTPUT_D                      #motor ports

from ev3dev2.motor import LargeMotor, MoveSteering
##################################################

r = OUTPUT_D    #right motor port
l = OUTPUT_B    #left motor port
r_motor = LargeMotor(r)
l_motor = LargeMotor(l)

steer = MoveSteering(l, r)

# constants
r = 2.75                #radius (cm)
angle = 0
speed = 50

# dependent variables
dist = 120                  #distance in cm
laps = 3                    #number of laps


#####
rotations = dist / (2 * m.pi * r)   #distance / wheel circumference = num of rotations

for i in range(laps):
    steer.on_for_rotations(0, speed, rotations)         # 0=straight, -=left, +=right
    sleep(0.5)
    steer.on_for_rotations(0, speed*-1, rotations)
    sleep(0.5)
