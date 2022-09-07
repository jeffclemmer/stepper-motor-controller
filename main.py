#! /usr/bin/python3


#
# will only run on a Raspberry PI
#


import os
import threading

import RPi.GPIO as GPIO

# import our threaded library
import SteeringMotor

# set GPIO mode
GPIO.setmode(GPIO.BOARD)

# init thread
steering = SteeringMotor.SteeringMotorThread()
steering.start()

newSteeringPos = 0

print("\n")

# do an endless loop that asks for a position from user input
# will send that user input straight into the thread and return 
# immediately for new input
while True:
    try:
        newSteeringPosStr = input("Enter a new steering position(or 'exit'): ")
        
        if newSteeringPosStr == "exit":
            break
        else:
            try:
                newSteeringPos = int( newSteeringPosStr )
            except:
                print("not a valid command")

        steering.newPosition(newSteeringPos)
        
    except KeyboardInterrupt:
        break


steering.exitThread()
steering.join()

GPIO.cleanup()

print("\n\ngood night\n\n")
