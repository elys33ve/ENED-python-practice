#!/usr/bin/env python3

import math as m
from time import sleep

from ev3dev2.motor import OUTPUT_B, OUTPUT_D                      #motor ports
from ev3dev2.motor import LargeMotor, MoveSteering
#####################################################################
r, l = OUTPUT_D, OUTPUT_B
r_motor, l_motor = LargeMotor(r), LargeMotor(l)
#####################################################################
steer = MoveSteering(l, r)


# var
dist = 84           # distance (cm)
# constants
r = 2.75            # radius (cm)
angle = 0
speed = 40
rotations = dist / (2 * r * m.pi)


#####
steer.on_for_rotations(0, speed, rotations)



