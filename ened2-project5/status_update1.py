#!/usr/bin/env python3

# Move forward a given distance, turn 90 degrees, move forward another
# given distance and end at predicted position.
##################################################
from time import sleep
import math as m

from ev3dev2.motor import OUTPUT_B, OUTPUT_D                      #motor ports

from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.motor import LargeMotor, MoveSteering
##################################################

#################   --gyro setup
MODE_GYRO_ANG = 'GYRO-ANG'

gyro = GyroSensor()
gyro.reset()

#################   --motor setup
r, l = OUTPUT_D, OUTPUT_B
r_motor = LargeMotor(r)
l_motor = LargeMotor(l)

steer = MoveSteering(l, r)

#################   --constants
r = 2.75 / 2.54         #radius (in)
sp_l = 25               #left speed
sp_r = -25              #right speed
speed = 40

angle = -80
#(d2 = 96 --> ang=-90)
#(d2 = 60 --> ang=-84)
#(d2 =< 36 --> ang=-87.5)

#################   --dependent variables (distance)
d1 = 24                     # initial distance forward (in)
d2 = 22                     # final distance forward (in)

r1 = d1 / (r * 2 * m.pi)    # initial amt rotations (d/circ)
r2 = d2 / (r * 2 * m.pi)    # final amt rotations (d/circ)

#################   --move

## forward 12 in
steer.on_for_rotations(0, speed, r1)
sleep(0.5)

## turn 90 deg       (left)
gyro.reset()

while gyro.angle > angle:
        r_motor.on(sp_r)        #right motor
        l_motor.on(sp_l)        #left motor
r_motor.off()
l_motor.off()

## forward d2
steer.on_for_rotations(0, speed, r2)
sleep(0.5)


