# 
# Controls a stepper motor via a sequence of pulses to various RPi pins
# This is a threaded library, which means that you can execute a
# movement, interupt that movement, and have it start moving to a 
# different position before the first movement is complete.
# 

import threading
import time
import RPi.GPIO as GPIO

class SteeringMotorThread(threading.Thread):
    
    pins = [7,13,11,15]
    
    lock = threading.Lock()
    exitLock = threading.Lock()
    doExit = False
    wakeUp = threading.Condition()
    wantPosition = 0
    
    # outside interface to set position
    def newPosition(self, pos):
        with self.lock:
            self.wantPosition = pos
        with self.wakeUp:
            self.wakeUp.notify()
        
    def exitThread(self):
        with self.exitLock:
            self.doExit = True
        with self.wakeUp:
            self.wakeUp.notify()
        
    # thread to control motor
    def run(self):
        
        maxRange = 100
        curPosition = 0
        curPin = 0
        curDirection = 0 # 0 or 1
        localWantPos = 1
        
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
        
        # TODO: do initialization sequence where we turn the motor all the way left and all the way right to find the max steps in the range
        
        # TODO: center the wheel
        
        #execute steering turns from user
        while True:
            
            with self.wakeUp:
                self.wakeUp.wait()
            
            with self.exitLock:
                if self.doExit == True:
                    break
                    
            while True:
                
                with self.lock:
                    localWantPos = self.wantPosition
                        
                with self.exitLock:
                    if self.doExit == True:
                        # print("here4")
                        break
            
                if localWantPos != curPosition:
                    
                    if localWantPos >= 0 and localWantPos <= maxRange:
                        
                        if localWantPos < curPosition:
                            curDirection = 0
                        if localWantPos > curPosition:
                            curDirection = 1
                        
                        if curDirection == 0:
                            curPin -= 1
                            curPosition -= 1
                        if curDirection == 1:
                            curPin += 1
                            curPosition += 1
                        
                        if curPin > 3:
                            curPin = 0
                        if curPin < 0:
                            curPin = 3

                        if curPosition >= 0 and curPosition <= maxRange:
                        
                            GPIO.output(self.pins[curPin],GPIO.HIGH)
                            time.sleep(.02)
                            GPIO.output(self.pins[curPin],GPIO.LOW)
                        
                            # test max range poles GPIO inputs after each pulse
                        
                    else:
                        print("Steering position is out of bounds")
                        break
                else:
                    break
