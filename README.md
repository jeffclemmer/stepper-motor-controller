## Multithreaded Steering Motor Controller

This code is a simple library designed to control a stepper motor being used as a steering motor for a wheeled robot.

I own two Heathkit Hero Jr. robots from the 1980s, and slowly over time, I've been modernizing one with a Raspberry PI and AVR controllers.

This particular robot has three wheels, one of which is a steering motor that is based on a large stepper motor.  I've designed a circuit that uses four darlington transistors hooked up to the RPi that directly control the movement of the stepper motor.

This is an initial library meant to be used in a bigger system to allow remote control of the robot.

![Hero Jr Rear](/hero-jr-rear.jpg)

## Running This Code

You need to have an RPi handy, with a full electronics design setup.  For example, you'll need a breadboard, power supply, transistors and associated circuit parts, wire, and an actual stepper motor.

But, if you're so inclined, you can just as easily hook up some LEDs to the proper pins (with resistors) and watch the output.

In modern times, we would probably use a Servo Motor to achieve the same results.

![Hero Jr Ad](/hero-jr-ad.jpg)
