#!/usr/bin/env python3

import math as m
from time import sleep

from ev3dev2.motor import OUTPUT_B, OUTPUT_D                      #motor ports

from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.motor import LargeMotor, MoveSteering
##################################################
# forward in straght line, turn 180 degrees, forward for same distance

MODE_GYRO_ANG = 'GYRO-ANG'

gyro = GyroSensor()
gyro.reset()


r = OUTPUT_D
l = OUTPUT_B
r_motor = LargeMotor(r)
l_motor = LargeMotor(l)

steer = MoveSteering(l, r)
lm = LargeMotor()

speed = 50
sp_l = 25
sp_r = -25

dist = 90
laps = 4 * 2

rotations = dist / (2.75 * 2 * m.pi)

for i in range(laps):
    steer.on_for_rotations(0, speed, rotations)                 # 0=straight, -=left, +=right
    sleep(0.5)
    gyro.reset()
    while gyro.angle > -178:
        lm.on(sp_l,sp_r)

