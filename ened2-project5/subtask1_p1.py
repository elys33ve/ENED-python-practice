#!/usr/bin/env python3

from csv import list_dialects
import os
import sys
import math as m
from time import sleep


import ev3dev2 as e
import ev3dev2.motor as em

from ev3dev2.motor import OUTPUT_B, OUTPUT_D                      #motor ports

from ev3dev2.motor import LargeMotor, MoveSteering
##################################################
# Forward, back in straigbt line


####

r = OUTPUT_D
l = OUTPUT_B
r_motor = LargeMotor(r)
l_motor = LargeMotor(l)

angle = 0
speed = 50

steer = MoveSteering(l, r)

dist = 120
laps = 3

rotations = dist / (2.75 * 2 * m.pi)

for i in range(laps):
    steer.on_for_rotations(0, speed, rotations)                 # 0=straight, -=left, +=right
    sleep(0.5)
    steer.on_for_rotations(0, speed*-1, rotations)
    sleep(0.5)
