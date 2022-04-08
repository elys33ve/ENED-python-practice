#!/usr/bin/env python3

# Move forward a given distance, turn 180 degrees and return to original
# position a given number of times.
##################################################
from time import sleep
import math as m

from ev3dev2.motor import OUTPUT_B, OUTPUT_D                      #motor ports

from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.motor import LargeMotor, MoveSteering
##################################################

MODE_GYRO_ANG = 'GYRO-ANG'          #set gryo mode to angle

gyro = GyroSensor()
gyro.reset()            #reset gyro position


r = OUTPUT_D    #right motor port
l = OUTPUT_B    #left motor port
r_motor = LargeMotor(r)                     #right motor
l_motor = LargeMotor(l)                     #left motor

lm = LargeMotor()                           #both motors
steer = MoveSteering(l, r)                  #both motors steer

# constants
r = 2.75                #radius (cm)
speed = 50
sp_l = 25           #left +
sp_r = -25          #right -

# dependent variables
dist = 90                   #distance in cm
laps = 4                    #number of laps


#####
laps = laps * 2                         #double amt laps
rotations = dist / (2.75 * 2 * m.pi)    #dist / circumference


for i in range(laps):
    steer.on_for_rotations(0, speed, rotations)         #forward for rotations
    sleep(0.5)
    gyro.reset()                                            #reset gyro
    while gyro.angle > -178:                            #until approx. 180 deg
        steer.on_for_rotations(-50, speed, rotations)       #turn to left
    steer.on_for_rotations(0, speed, rotations)
    gyro.reset()
    while gyro.angle > -178:
        steer.on_for_rotations(-50, speed, rotations)

