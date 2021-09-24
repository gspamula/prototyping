#!/usr/bin/env micropython
from time import time, sleep
import os
import threading
import logging
from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MoveSteering,
                         MoveTank, SpeedPercent, follow_for_ms, MediumMotor, LargeMotor)
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.sound import Sound
from ev3dev2.button import Button

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
s = Sound()

mm_horizontal = MediumMotor(OUTPUT_D)
mm_vertical = MediumMotor(OUTPUT_A)
left_motor = LargeMotor(OUTPUT_B)
right_motor = LargeMotor(OUTPUT_C)
left_light = ColorSensor(INPUT_4)
right_light = ColorSensor(INPUT_1)
left_motor.reset()
right_motor.reset()

#Objective: Make the robot go 950 degrees @ 45 speed

# Write your program here.
#s.speak("hello from the darth rappers")

'''
def my_follow_for_degrees(tank, TargetDegrees, left_motor, right_motor):
        MeasuredAverageDegrees = (left_motor.position + right_motor.position)/2
        if TargetDegrees >= 0:
            if MeasuredAverageDegrees >= TargetDegrees:
                return False
            else:
                return True
        else:
            if MeasuredAverageDegrees <= TargetDegrees:
                return False
            else:
                return True

my_follow_for_degrees(tank, TargetDegrees, left_motor, right_motor) = robot_move_for_degrees(tank, TargetDegrees, left_motor, right_motor)
robot_move_for_degrees(tank, 950, 50, 50)
'''
robot_drive = MoveTank(OUTPUT_B, OUTPUT_C)

robot_drive.on

left_motor.on(45, brake=True, block=False)
right_motor.on(45, brake=True, block=False)

#sleep(500)


while True:
    if left_motor.position >= 950:
        left_motor.stop()
        break
    if right_motor.position >= 950:
        right_motor.stop()
        break